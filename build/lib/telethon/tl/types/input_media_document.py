from ...tl.tlobject import TLObject


class InputMediaDocument(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    inputMediaDocument#5acb668e flags:# id:InputDocument caption:string ttl_seconds:flags.0?int = InputMedia"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x5acb668e
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0xfaf846f4

    def __init__(self, id, caption, ttl_seconds=None):
        """
        :param id: Telegram type: "InputDocument".
        :param caption: Telegram type: "string".
        :param ttl_seconds: Telegram type: "int".

        Constructor for InputMedia: Instance of either InputMediaEmpty, InputMediaUploadedPhoto, InputMediaPhoto, InputMediaGeoPoint, InputMediaContact, InputMediaUploadedDocument, InputMediaDocument, InputMediaVenue, InputMediaGifExternal, InputMediaPhotoExternal, InputMediaDocumentExternal, InputMediaGame, InputMediaInvoice.
        """
        super().__init__()

        self.id = id
        self.caption = caption
        self.ttl_seconds = ttl_seconds

    def to_dict(self):
        return {
            'id': None if self.id is None else self.id.to_dict(),
            'caption': self.caption,
            'ttl_seconds': self.ttl_seconds,
        }

    def on_send(self, writer):
        writer.write_int(InputMediaDocument.constructor_id, signed=False)
        # Calculate the flags. This equals to those flag arguments which are NOT None
        flags = 0
        flags |= (1 << 0) if self.ttl_seconds else 0
        writer.write_int(flags)

        self.id.on_send(writer)
        writer.tgwrite_string(self.caption)
        if self.ttl_seconds:
            writer.write_int(self.ttl_seconds)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return InputMediaDocument(None, None, None)

    def on_response(self, reader):
        flags = reader.read_int()

        self.id = reader.tgread_object()
        self.caption = reader.tgread_string()
        if (flags & (1 << 0)) != 0:
            self.ttl_seconds = reader.read_int()

    def __repr__(self):
        return 'inputMediaDocument#5acb668e flags:# id:InputDocument caption:string ttl_seconds:flags.0?int = InputMedia'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
