from ....tl.tlobject import TLObject


class GetRecentStickersRequest(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    messages.getRecentStickers#5ea192c9 flags:# attached:flags.0?true hash:int = messages.RecentStickers"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x5ea192c9
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0xf76f8683

    def __init__(self, hash, attached=None):
        """
        :param attached: Telegram type: "true".
        :param hash: Telegram type: "int".

        :returns messages.RecentStickers: Instance of either RecentStickersNotModified, RecentStickers.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.attached = attached
        self.hash = hash

    def to_dict(self):
        return {
            'attached': self.attached,
            'hash': self.hash,
        }

    def on_send(self, writer):
        writer.write_int(GetRecentStickersRequest.constructor_id, signed=False)
        # Calculate the flags. This equals to those flag arguments which are NOT None
        flags = 0
        flags |= (1 << 0) if self.attached else 0
        writer.write_int(flags)

        writer.write_int(self.hash)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return GetRecentStickersRequest(None, None)

    def on_response(self, reader):
        self.result = reader.tgread_object()

    def __repr__(self):
        return 'messages.getRecentStickers#5ea192c9 flags:# attached:flags.0?true hash:int = messages.RecentStickers'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
