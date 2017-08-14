from ...tl.tlobject import TLObject


class InputReportReasonViolence(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    inputReportReasonViolence#1e22c78d = ReportReason"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x1e22c78d
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x8401bd27

    def __init__(self):
        super().__init__()

    @staticmethod
    def to_dict():
        return {}

    def on_send(self, writer):
        writer.write_int(InputReportReasonViolence.constructor_id, signed=False)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return InputReportReasonViolence()

    def on_response(self, reader):
        pass

    def __repr__(self):
        return 'inputReportReasonViolence#1e22c78d = ReportReason'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
