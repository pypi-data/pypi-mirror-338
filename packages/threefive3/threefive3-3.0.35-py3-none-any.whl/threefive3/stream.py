"""
Mpeg-TS Stream parsing class Stream
"""

import sys
from functools import partial
from .new_reader import reader
from .stuff import print2, blue
from .cue import Cue
from .packetdata import PacketData
from .streamtypes import streamtype_map
from .words import minusone, zero, one, two, three, four, five, six, seven, eight
from .words import nine, ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen
from .words import seventeen, twentytwo, twentyfive, twentynine
from .words import thirtytwo, sixtyfour, onetwentyeight, ninetythousand


def no_op(cue):
    """
    no_op is just a dummy func to pass to Stream.decode()
    to suppress output.
    """
    return cue


def show_cue(cue):
    """
    default function call for Stream.decode
    when a SCTE-35 packet is found.
    """
    cue.show()


def show_cue_stderr(cue):
    """
    print2 cue data to sys.stderr
    for Stream.decode_proxy
    """
    cue.show()


class ProgramInfo:
    """
    ProgramInfo is a class to
    hold Program information
    for use with Stream.show()
    """

    def __init__(self, pid=None, pcr_pid=None):
        self.pid = pid
        self.pcr_pid = pcr_pid
        self.provider = b"fu-corp"
        self.service = b"threefive3"
        self.streams = {}  # pid to stream_type mapping

    def _mk_vee(self, k):
        vee = int(self.streams[k], base=sixteen)
        if vee in streamtype_map:
            vee = f"{hex(vee)}\t{streamtype_map[vee]}"
        else:
            vee = f"{vee} Unknown"
        print2(f"\t\t{k} [{hex(k)}]\t{vee}")

    def show(self):
        """
        show print2 the Program Infomation
        in a familiar format.
        """
        serv = self.service.decode(errors="ignore")
        prov = self.provider.decode(errors="ignore")
        print2(f"\tService:  {serv}\n\tProvider: {prov}")
        print2(f"\tPMT PID:  {self.pid}\n\tPCR PID:  {self.pcr_pid}")
        print2("\tStreams:")
        # sorted_dict = {k:my_dict[k] for k in sorted(my_dict)})
        keys = sorted(self.streams)
        print2("\t\tPID:\t\tType:")
        print2("\t \t" + "-" * 44)
        for k in keys:
            self._mk_vee(k)


class Pids:
    """
    Pids holds sets of pids for pat,pcr,pmt, and scte35
    """

    SDT_PID = eleven
    PAT_PID = zero

    def __init__(self):
        self.pcr = set()
        self.pmt = set()
        self.scte35 = set()
        self.maybe_scte35 = set()
        self.tables = set()
        self.tables.add(self.PAT_PID)
        self.tables.add(self.SDT_PID)


class Maps:
    """
    Maps holds mappings
    pids mapped to continuity_counters,
    programs, partial tables and last payload.

    programs mapped to pcr and pts

    """

    def __init__(self):
        self.pid_cc = {}
        self.pid_prgm = {}
        self.prgm_pcr = {}
        self.prgm_pts = {}
        self.prgm = {}
        self.partial = {}
        self.last = {}


class Stream:
    """
    Stream class for parsing MPEG-TS data.
    """

    PACKET_SIZE = _PACKET_SIZE = 188
    PMT_TID = _PMT_TID = b"\x02"
    ROLLOVER = 8589934591
    ROLLOVER9K = 95443.717678
    SCTE35_PES_START = b"\x00\x00\x01\xfc"
    SCTE35_TID = _SCTE35_TID = b"\xfc"
    SDT_TID = _SDT_TID = b"\x42"
    SYNC_BYTE = _SYNC_BYTE = 0x47

    def __init__(self, tsdata, show_null=True):
        """
        tsdata is an file or http/https url
        set show_null=False to exclude Splice Nulls

        Use like...

        from threefive3 import Stream
        strm = Stream("vid.ts",show_null=False)
        strm.decode()

        """
        if isinstance(tsdata, str):
            self._tsdata = reader(tsdata)
        else:
            self._tsdata = tsdata
        self.show_null = show_null
        self.start = {}
        self.info = False
        self.the_scte35_pids = []
        self.pids = Pids()
        self.maps = Maps()
        self.pmt_payloads = set()
        self.pmt_count = 0

    def __repr__(self):
        return str(self.__dict__)

    @staticmethod
    def as_90k(ticks):
        """
        as_90k returns ticks as 90k clock time
        """
        return round((ticks / ninetythousand), six)

    @staticmethod
    def _pusi_flag(pkt):
        return pkt[one] & sixtyfour

    @staticmethod
    def _afc_flag(pkt):
        return pkt[three] & thirtytwo

    @staticmethod
    def _pcr_flag(pkt):
        return pkt[five] & sixteen

    @staticmethod
    def _spi_flag(pkt):
        return pkt[five] & thirtytwo

    @staticmethod
    def _pts_flag(pay):
        # uses pay not pkt
        return pay[seven] & onetwentyeight

    @staticmethod
    def _parse_length(byte1, byte2):
        """
        parse a 12 bit length value
        """
        return (byte1 & fifteen) << eight | byte2

    @staticmethod
    def _parse_pid(byte1, byte2):
        """
        parse a 13 bit pid value
        """
        pid = (byte1 & fifteen) << eight | byte2
        return pid

    @staticmethod
    def _parse_program(byte1, byte2):
        """
        parse a 16 bit program number value
        """
        return (byte1 << eight) | byte2

    @staticmethod
    def _split_by_idx(pay, marker):
        try:
            return pay[pay.index(marker) :]
        except (LookupError, TypeError, ValueError):
            return False

    def _find_start(self):
        """
        _find_start locates the first SYNC_BYTE
        parses 1 packet and returns True
        if SYNC_BYTE is found.
        """
        while self._tsdata:
            bite = self._tsdata.read(one)
            if bite:
                if bite[zero] == self.SYNC_BYTE:
                    tail = self._tsdata.read(self.PACKET_SIZE - one)
                    self._parse(bite + tail)
                    return True
        print2("No Stream Found\n")
        return False

    def iter_pkts(self, num_pkts=one):
        """
        iter_pkts iterates a mpegts stream into packets
        """
        if self._find_start():
            return iter(partial(self._tsdata.read, self.PACKET_SIZE * num_pkts), b"")
        return False

    def _mk_pkts(self, chunk):
        return [
            self._parse(chunk[i : i + self.PACKET_SIZE])
            for i in range(0, len(chunk), self.PACKET_SIZE)
        ]

    def _decode2cues(self, chunk, func):
        _ = [func(cue) for cue in self._mk_pkts(chunk) if cue]

    def decode(self, func=show_cue):
        """
        Stream.decode reads self.tsdata to find SCTE35 packets.
        func can be set to a custom function that accepts
        a threefive3.Cue instance as it's only argument.
        """
        num_pkts = 1400
        for chunk in self.iter_pkts(num_pkts=num_pkts):
            self._decode2cues(chunk, func)
        return False

    def decode_next(self):
        """
        Stream.decode_next returns the next
        SCTE35 cue as a threefive3.Cue instance.
        """
        for pkt in self.iter_pkts():
            cue = self._parse(pkt)
            if cue:
                return cue
        return False

    def decode_pids(self, scte35_pids=[], func=show_cue):
        """
        Stream.decode_pids takes a list of SCTE-35 Pids parse
        and an optional call back function to run when a Cue is found.
        if scte35_pids is not set, all threefive3 pids will be parsed.
        """
        self.the_scte35_pids = scte35_pids
        return self.decode(func)

    def decode_start_time(self):
        """
        decode_start_time
        """
        self.decode(func=no_op)
        if len(self.start.values()) > zero:
            return self.start.popitem()[one]
        return False

    def proxy(self, func=show_cue_stderr):
        """
        Stream.decode_proxy writes all ts packets are written to stdout
        for piping into another program like mplayer.
        SCTE-35 cues are print2`ed to stderr.
        """
        num_pkts = 1400
        for chunk in self.iter_pkts(num_pkts=num_pkts):
            self._decode2cues(chunk, func)
            sys.stdout.buffer.write(chunk)
        return False

    def show(self):
        """
        displays streams that will be
        parsed for SCTE-35.
        """
        self.info = True
        for pkt in self.iter_pkts():
            self._parse(pkt)
            if self.pmt_count > len(self.pmt_payloads) << one:
                blue(f"PMT Count: {self.pmt_count}")
                break
        if self.maps.prgm.keys():
            sopro = sorted(self.maps.prgm.items())
            for k, vee in sopro:
                print2(f"\nProgram: {k}")
                vee.show()

    def show_pts(self):
        """
        show_pts displays current pts by pid.
        """
        print("\tPrgm\tPTS")
        last_pts = None
        for pkt in self.iter_pkts():
            pid = self._parse_info(pkt)
            # if pid in self.pids.pcr:
            self._chk_pts(pkt, pid)
            pts = self.pid2pts(pid)
            if pts:
                if pts != last_pts:
                    print(f"\t{self.pid2prgm(pid)}\t{pts}")
                last_pts = pts

    def pts(self):
        """
        pts returns a dict of  program:pts
        """
        return self.maps.prgm_pts

    def pid2prgm(self, pid):
        """
        pid2prgm takes a pid,
        returns the program
        """
        prgm = one
        if pid in self.maps.pid_prgm:
            prgm = self.maps.pid_prgm[pid]
        return prgm

    def pid2pts(self, pid):
        """
        pid2pts takes a pid
        returns the current pts
        """
        prgm = self.pid2prgm(pid)
        if prgm in self.maps.prgm_pts:
            return self.as_90k(self.maps.prgm_pts[prgm])
        return False

    def pid2pcr(self, pid):
        """
        pid2pcr takes a pid
        returns the current pcr
        """
        prgm = self.pid2prgm(pid)
        if prgm in self.maps.prgm_pcr:
            return self.as_90k(self.maps.prgm_pcr[prgm])
        return False

    def _unpad(self, bites=b""):
        return bites.strip(b"\xff")

    def _mk_packet_data(self, pid):
        prgm = self.maps.pid_prgm[pid]
        pdata = PacketData(pid, prgm)
        pdata.mk_pcr(self.maps.prgm_pcr)
        pdata.mk_pts(self.maps.prgm_pts)
        return pdata

    def _parse_cc(self, pkt, pid):
        last_cc = None
        c_c = pkt[three] & fifteen
        if pid in self.maps.pid_cc:
            last_cc = self.maps.pid_cc[pid]
            good = (last_cc, ((last_cc + one) % sixteen))
            if c_c not in good:
                print2(f" # BAD --> pid:\t{hex(pid)}\tlast cc:\t{last_cc}\tcc:\t{c_c}")
        self.maps.pid_cc[pid] = c_c

    def _parse_pts(self, pkt, pid):
        """
        parse pts and store by program key
        in the dict Stream._pid_pts
        """
        payload = self._parse_payload(pkt)
        if len(payload) > thirteen:
            if self._pts_flag(payload):
                pts = (payload[nine] & fourteen) << twentynine
                pts |= payload[ten] << twentytwo
                pts |= (payload[eleven] >> one) << fifteen
                pts |= payload[twelve] << seven
                pts |= payload[thirteen] >> one
                prgm = self.pid2prgm(pid)
                self.maps.prgm_pts[prgm] = pts
                if prgm not in self.start:
                    self.start[prgm] = pts

    def _parse_pcr(self, pkt, pid):
        if self._afc_flag(pkt):
            pcr = pkt[six] << twentyfive
            pcr |= pkt[seven] << seventeen
            pcr |= pkt[eight] << nine
            pcr |= pkt[nine] << one
            pcr |= pkt[ten] >> seven
            prgm = self.pid2prgm(pid)
            self.maps.prgm_pcr[prgm] = pcr

    def _parse_payload(self, pkt):
        """
        _parse_payload returns the packet payload
        """
        head_size = four
        if self._afc_flag(pkt):
            pkt = pkt[:four] + self._unpad(pkt[four:])
            afl = pkt[four]
            head_size += afl + one  # +one for afl byte
        return pkt[head_size:]

    def _pmt_pid(self, pay, pid):
        self.pmt_count += one
        if pay in self.pmt_payloads:
            if self.pmt_count > len(self.pmt_payloads) << one:
                return
        self.pmt_payloads.add(pay)
        self._parse_pmt(pay, pid)

    def _pat_pid(self, pay, pid):
        if pid == self.pids.PAT_PID:
            self._parse_pat(pay)

    def _sdt_pid(self, pay, pid):
        if pid == self.pids.SDT_PID:
            self._parse_sdt(pay)

    def _parse_tables(self, pkt, pid):
        """
        _parse_tables parse for
        PAT, PMT,  and SDT tables
        based on pid of the pkt
        """
        pay = self._parse_payload(pkt)
        if pid in self.pids.pmt:
            self._pmt_pid(pay, pid)
            return
        if not self._same_as_last(pay, pid):
            self._pat_pid(pay, pid)
            self._sdt_pid(pay, pid)

    def _parse_info(self, pkt):
        """
        _parse_info parses the packet for tables
        and returns the pid
        """
        pid = self._parse_pid(pkt[one], pkt[two])
        if pid in self.pids.tables:
            self._parse_tables(pkt, pid)
        return pid

    def _chk_pcr(self, pkt, pid):
        if self._pcr_flag(pkt):
            self._parse_pcr(pkt, pid)

    def _chk_pts(self, pkt, pid):
        if pid in self.pids.pcr:
            self._parse_pts(pkt, pid)

    def _parse(self, pkt):
        cue = False
        pid = self._parse_info(pkt)
        if self._pusi_flag(pkt):
            self._chk_pts(pkt, pid)
        if self._pid_has_scte35(pid):
            cue = self._parse_scte35(pkt, pid)
        return cue

    def _pid_has_scte35(self, pid):
        #  return pid in self.pids.scte35.union(self.pids.maybe_scte35) #   union sucks. Worst
        # return (pid in self.pids.scte35 or pid in self.pids.maybe_scte35) # Good
        return pid in (self.pids.scte35 or self.pids.maybe_scte35)  # Best
        # return pid in (self.pids.scte35|self.pids.maybe_scte35)  # wtf? Bad

    def _chk_partial(self, pay, pid, sep):
        if pid in self.maps.partial:
            pay = self.maps.partial.pop(pid) + pay
        return self._split_by_idx(pay, sep)

    def _same_as_last(self, pay, pid):
        last = False
        if pid in self.maps.last:
            last = self.maps.last[pid]
        self.maps.last[pid] = pay
        return last

    def _section_incomplete(self, pay, pid, seclen):
        # + 3 for the bytes before section starts
        if len(pay) > (seclen + three):
            return False
        #   if (seclen + three) > len(pay):
        self.maps.partial[pid] = pay
        return True

    def _parse_cue(self, pay, pid):
        packet_data = None
        packet_data = self._mk_packet_data(pid)
        cue = Cue(pay, packet_data)
        if cue.bites:
            return cue
        return False

    def _strip_scte35_pes(self, pkt):
        pay = self._parse_payload(pkt)
        if self.SCTE35_PES_START in pay:
            pay = pay.split(self.SCTE35_PES_START, 1)[minusone]
            peslen = pay[four] + five  # PES header length
            pay = pay[peslen:]
        return pay

    def _pop_maybe_pid(self, pid):
        if pid in self.pids.maybe_scte35:
            self.pids.maybe_scte35.remove(pid)

    def _chk_maybe_pid(self, pay, pid):
        pay = self._chk_partial(pay, pid, self.SCTE35_TID)
        if not pay:
            self._pop_maybe_pid(pid)
            return False
        if pay[thirteen] == self.show_null:
            return False
        return pay

    def _mk_scte35_payload(self, pkt, pid):
        pay = self._strip_scte35_pes(pkt)
        if not pay:
            return False
        return self._chk_maybe_pid(pay, pid)

    def _parse_scte35(self, pkt, pid):
        """
        parse a threefive3 cue from one or more packets
        """
        pay = self._mk_scte35_payload(pkt, pid)
        if not pay:
            return False
        seclen = self._parse_length(pay[one], pay[two])
        if self._section_incomplete(pay, pid, seclen):
            return False
        pay = pay[: seclen + three]
        cue = self._parse_cue(pay, pid)
        return cue

    def _mk_pinfo(self, service_id, pn, sn):
        if service_id not in self.maps.prgm:
            self.maps.prgm[service_id] = ProgramInfo()
        pinfo = self.maps.prgm[service_id]
        pinfo.provider = pn
        pinfo.service = sn

    def _parse_sdt(self, pay):
        """
        _parse_sdt parses the SDT for program metadata
        """
        pay = self._chk_partial(pay, self.pids.SDT_PID, self.SDT_TID)
        if not pay:
            return False
        seclen = self._parse_length(pay[one], pay[two])
        if self._section_incomplete(pay, self.pids.SDT_PID, seclen):
            return False
        idx = eleven
        while idx < seclen + three:
            service_id = self._parse_program(pay[idx], pay[idx + one])
            blue(service_id)
            idx += three
            dloop_len = self._parse_length(pay[idx], pay[idx + one])
            idx += two
            i = zero
            while i < dloop_len:
                if pay[idx] == 0x48:
                    i += three
                    spnl = pay[idx + i]
                    i += one
                    provider_name = pay[idx + i : idx + i + spnl]
                    i += spnl
                    snl = pay[idx + i]
                    i += one
                    service_name = pay[idx + i : idx + i + snl]
                    i += snl
                    blue(f"{provider_name} {len(provider_name)}")
                    self._mk_pinfo(service_id, provider_name, service_name)
                i = dloop_len
                idx += i
                return True
        return False

    def _parse_pat(self, pay):
        """
        parse program association table
        for program to pmt_pid mappings.
        """
        pay = self._chk_partial(pay, self.pids.PAT_PID, b"")
        seclen = self._parse_length(pay[two], pay[three])
        if self._section_incomplete(pay, self.pids.PAT_PID, seclen):
            return False
        seclen -= five  # pay bytes 4,5,6,7,8
        idx = nine
        chunk_size = four
        while seclen > four:  #  4 bytes for crc
            program_number = self._parse_program(pay[idx], pay[idx + one])
            if program_number > zero:
                pmt_pid = self._parse_pid(pay[idx + two], pay[idx + three])
                self.pids.pmt.add(pmt_pid)
                self.pids.tables.add(pmt_pid)
            seclen -= chunk_size
            idx += chunk_size
        return True

    def _parse_pmt(self, pay, pid):
        """
        parse program maps for streams
        """
        pay = self._chk_partial(pay, pid, self.PMT_TID)
        if not pay:
            return False
        seclen = self._parse_length(pay[one], pay[two])
        if self._section_incomplete(pay, pid, seclen):
            return False
        program_number = self._parse_program(pay[three], pay[four])
        if not program_number:
            return False
        pcr_pid = self._parse_pid(pay[eight], pay[nine])
        if program_number not in self.maps.prgm:
            self.maps.prgm[program_number] = ProgramInfo()
        pinfo = self.maps.prgm[program_number]
        pinfo.pid = pid
        pinfo.pcr_pid = pcr_pid
        self.pids.pcr.add(pcr_pid)
        self.maps.pid_prgm[pcr_pid] = program_number
        proginfolen = self._parse_length(pay[ten], pay[eleven])
        idx = twelve + proginfolen
        si_len = seclen - (nine + proginfolen)
        self._parse_program_streams(si_len, pay, idx, program_number)
        return True

    def _parse_program_streams(self, si_len, pay, idx, program_number):
        """
        parse the elementary streams
        from a program
        """
        # 5 bytes for stream_type info
        chunk_size = five
        end_idx = (idx + si_len) - four
        while end_idx - chunk_size >= idx:
            stream_type, pid, ei_len = self._parse_stream_type(pay, idx)
            pinfo = self.maps.prgm[program_number]
            pinfo.streams[pid] = stream_type
            idx += chunk_size + ei_len
            self.maps.pid_prgm[pid] = program_number

    def _parse_stream_type(self, pay, idx):
        """
        extract stream pid and type
        """
        stream_type = hex(pay[idx])
        el_pid = self._parse_pid(pay[idx + one], pay[idx + two])
        ei_len = self._parse_length(pay[idx + three], pay[idx + four])
        self._set_scte35_pids(el_pid, stream_type)
        return stream_type, el_pid, ei_len

    def _set_scte35_pids(self, pid, stream_type):
        """
        if stream_type is 0x06 or 0x86
        add it to self._scte35_pids.
        """
        if stream_type in ["0x86"]:
            self.pids.scte35.add(pid)
        if stream_type in ["0x06", "0x6"]:
            self.pids.maybe_scte35.add(pid)
