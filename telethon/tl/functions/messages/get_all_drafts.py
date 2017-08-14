from ....tl.tlobject import TLObject


class GetAllDraftsRequest(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    messages.getAllDrafts#6a3f8d65 = Updates"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x6a3f8d65
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x8af52aac

    def __init__(self):
        super().__init__()
        self.result = None
        self.content_related = True

    @staticmethod
    def to_dict():
        return {}

    def on_send(self, writer):
        writer.write_int(GetAllDraftsRequest.constructor_id, signed=False)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return GetAllDraftsRequest()

    def on_response(self, reader):
        self.result = reader.tgread_object()

    def __repr__(self):
        return 'messages.getAllDrafts#6a3f8d65 = Updates'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
