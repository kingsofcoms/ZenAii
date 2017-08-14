from ....tl.tlobject import TLObject


class GetNearestDcRequest(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    help.getNearestDc#1fb33026 = NearestDc"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x1fb33026
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x3877045f

    def __init__(self):
        super().__init__()
        self.result = None
        self.content_related = True

    @staticmethod
    def to_dict():
        return {}

    def on_send(self, writer):
        writer.write_int(GetNearestDcRequest.constructor_id, signed=False)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return GetNearestDcRequest()

    def on_response(self, reader):
        self.result = reader.tgread_object()

    def __repr__(self):
        return 'help.getNearestDc#1fb33026 = NearestDc'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
