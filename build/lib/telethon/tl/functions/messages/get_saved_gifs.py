from ....tl.tlobject import TLObject


class GetSavedGifsRequest(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    messages.getSavedGifs#83bf3d52 hash:int = messages.SavedGifs"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x83bf3d52
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0xa68b61f5

    def __init__(self, hash):
        """
        :param hash: Telegram type: "int".

        :returns messages.SavedGifs: Instance of either SavedGifsNotModified, SavedGifs.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.hash = hash

    def to_dict(self):
        return {
            'hash': self.hash,
        }

    def on_send(self, writer):
        writer.write_int(GetSavedGifsRequest.constructor_id, signed=False)
        writer.write_int(self.hash)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return GetSavedGifsRequest(None)

    def on_response(self, reader):
        self.result = reader.tgread_object()

    def __repr__(self):
        return 'messages.getSavedGifs#83bf3d52 hash:int = messages.SavedGifs'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
