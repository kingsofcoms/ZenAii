from ....tl.tlobject import TLObject


class ClearSavedInfoRequest(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    payments.clearSavedInfo#d83d70c1 flags:# credentials:flags.0?true info:flags.1?true = Bool"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0xd83d70c1
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0xf5b399ac

    def __init__(self, credentials=None, info=None):
        """
        :param credentials: Telegram type: "true".
        :param info: Telegram type: "true".

        :returns Bool: This type has no constructors.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.credentials = credentials
        self.info = info

    def to_dict(self):
        return {
            'credentials': self.credentials,
            'info': self.info,
        }

    def on_send(self, writer):
        writer.write_int(ClearSavedInfoRequest.constructor_id, signed=False)
        # Calculate the flags. This equals to those flag arguments which are NOT None
        flags = 0
        flags |= (1 << 0) if self.credentials else 0
        flags |= (1 << 1) if self.info else 0
        writer.write_int(flags)


    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return ClearSavedInfoRequest(None, None)

    def on_response(self, reader):
        self.result = reader.tgread_object()

    def __repr__(self):
        return 'payments.clearSavedInfo#d83d70c1 flags:# credentials:flags.0?true info:flags.1?true = Bool'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
