"""
SCTE35 Splice Commands
"""

from .bitn import Bitn
from .base import SCTE35Base
from .stuff import red


class SpliceCommand(SCTE35Base):
    """
    Base class, not used directly.
    """

    def __init__(self, bites=None):
        self.command_length = 0
        self.command_type = None
        self.name = None
        self.bites = bites

    def decode(self):
        """
        default decode method
        """

    def _set_len(self, start, end):
        """
        _set_len sets
        self.command_length
        """
        self.command_length = (start - end) >> 3

    def encode(self, nbin=None):
        """
        encode
        """
        nbin = self._chk_nbin(nbin)
        return nbin.bites


class BandwidthReservation(SpliceCommand):
    """
    Table 12 - bandwidth_reservation()
    """

    def __init__(self, bites=None):
        super().__init__(bites)
        self.command_type = 7
        self.name = "Bandwidth Reservation"

    def decode(self):
        """
        BandwidthReservation.decode method
        """


class PrivateCommand(SpliceCommand):
    """
    Table 13 - private_command
    """

    def __init__(self, bites=None):
        super().__init__(bites)
        self.command_type = 255
        self.name = "Private Command"
        self.identifier = None
        self.private_bytes = None

    def decode(self):
        """
        PrivateCommand.decode method
        """
        self.identifier = int.from_bytes(
            self.bites[:4], byteorder="big"
        )  # 4 bytes = 32 bits
        self.private_bytes = self.bites[4:]

    def encode(self, nbin=None):
        """
        encode private command
        """
        nbin = self._chk_nbin(nbin)
        self._chk_var(int, nbin.add_int, "identifier", 32)  # 4 bytes = 32 bits
        nbin.add_bites(self.private_bytes)
        return nbin.bites


class SpliceNull(SpliceCommand):
    """
    Table 8 - splice_null()
    """

    def __init__(self, bites=None):
        super().__init__(bites)
        self.command_type = 0
        self.name = "Splice Null"


class TimeSignal(SpliceCommand):
    """
    Table 11 - time_signal()
    """

    def __init__(self, bites=None):
        super().__init__(bites)
        self.command_type = 6
        self.name = "Time Signal"
        self.time_specified_flag = None
        self.pts_time = None

    def decode(self):
        """
        TimeSignal.decode method
        """
        bitbin = Bitn(self.bites)
        start = bitbin.idx
        self._splice_time(bitbin)
        self._set_len(start, bitbin.idx)

    def encode(self, nbin=None):
        """
        encode converts TimeSignal vars
        to bytes
        """
        nbin = self._chk_nbin(nbin)
        self._encode_splice_time(nbin)
        return nbin.bites

    def _splice_time(self, bitbin):
        """
        _splice_time Table 14 - splice_time()
        """
        self.time_specified_flag = bitbin.as_flag(1)
        if self.time_specified_flag:
            bitbin.forward(6)
            pts_time_ticks = bitbin.as_int(33)
            self.pts_time = self.as_90k(pts_time_ticks)
        else:
            bitbin.forward(7)

    def _encode_splice_time(self, nbin):
        """
        _encode_splice_time Table 14 - splice_time()
        """
        self._chk_var(bool, nbin.add_flag, "time_specified_flag", 1)
        if self.time_specified_flag:
            nbin.reserve(6)
            if not isinstance(self.pts_time, float):
                red(" A float for pts_time for the splice command is required. ")
            self.pts_time = round(self.pts_time, 6)
            nbin.add_int(int(self.as_ticks(self.pts_time)), 33)
        else:
            nbin.reserve(7)


class SpliceInsert(TimeSignal):
    """
    Table 10 - splice_insert()
    """

    def __init__(self, bites=None):
        super().__init__(bites)
        self.command_type = 5
        self.name = "Splice Insert"
        self.break_auto_return = None
        self.break_duration = None
        self.splice_event_id = None
        self.splice_event_cancel_indicator = None
        self.out_of_network_indicator = None
        self.program_splice_flag = None
        self.duration_flag = None
        self.splice_immediate_flag = None
        self.event_id_compliance_flag = None
        self.unique_program_id = None
        self.avail_num = None
        self.avails_expected = None

    def decode_break_duration(self, bitbin):
        """
        break_duration Table 15 - break_duration()
        """
        self.break_auto_return = bitbin.as_flag(1)
        bitbin.forward(6)
        break_duration_ticks = bitbin.as_int(33)
        self.break_duration = self.as_90k(break_duration_ticks)

    def decode(self):
        """
        decode SpliceInsert
        """
        bitbin = Bitn(self.bites)
        start = bitbin.idx
        self.splice_event_id = bitbin.as_int(32)
        self.splice_event_cancel_indicator = bitbin.as_flag(1)
        bitbin.forward(7)
        if not self.splice_event_cancel_indicator:
            self.out_of_network_indicator = bitbin.as_flag(1)
            self.program_splice_flag = bitbin.as_flag(1)
            self.duration_flag = bitbin.as_flag(1)
            self.splice_immediate_flag = bitbin.as_flag(1)
            self.event_id_compliance_flag = bitbin.as_flag(1)
            bitbin.forward(3)
            if self.program_splice_flag:
                if not self.splice_immediate_flag:
                    self._splice_time(bitbin)
            if self.duration_flag:
                self.decode_break_duration(bitbin)
            self.unique_program_id = bitbin.as_int(16)
            self.avail_num = bitbin.as_int(8)
            self.avails_expected = bitbin.as_int(8)
        self._set_len(start, bitbin.idx)

    def encode(self, nbin=None):
        """
        SpliceInsert.encode
        """
        nbin = self._chk_nbin(nbin)
        self._chk_var(int, nbin.add_int, "splice_event_id", 32)
        self._chk_var(bool, nbin.add_flag, "splice_event_cancel_indicator", 1)
        nbin.forward(7)
        if not self.splice_event_cancel_indicator:
            self._chk_var(bool, nbin.add_flag, "out_of_network_indicator", 1)
            self._chk_var(bool, nbin.add_flag, "program_splice_flag", 1)
            self._chk_var(bool, nbin.add_flag, "duration_flag", 1)
            self._chk_var(bool, nbin.add_flag, "splice_immediate_flag", 1)
            self._chk_var(bool, nbin.add_flag, "event_id_compliance_flag", 1)
            nbin.forward(3)
            if self.program_splice_flag:
                if not self.splice_immediate_flag:
                    self._encode_splice_time(nbin)
            if self.duration_flag:
                self.encode_break_duration(nbin)
            self._chk_var(int, nbin.add_int, "unique_program_id", 16)
            self._chk_var(int, nbin.add_int, "avail_num", 8)
            self._chk_var(int, nbin.add_int, "avails_expected", 8)
        return nbin.bites

    def encode_break_duration(self, nbin):
        """
        SpliceInsert._encode_break(nbin) is called
        if SpliceInsert.duration_flag is set
        """
        self._chk_var(bool, nbin.add_flag, "break_auto_return", 1)
        nbin.forward(6)
        nbin.add_int(self.as_ticks(self.break_duration), 33)


# table 7
command_map = {
    0: SpliceNull,
    5: SpliceInsert,
    6: TimeSignal,
    7: BandwidthReservation,
    255: PrivateCommand,
}
