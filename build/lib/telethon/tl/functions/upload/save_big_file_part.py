from ....tl.tlobject import TLObject


class SaveBigFilePartRequest(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    upload.saveBigFilePart#de7b673d file_id:long file_part:int file_total_parts:int bytes:bytes = Bool"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0xde7b673d
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0xf5b399ac

    def __init__(self, file_id, file_part, file_total_parts, bytes):
        """
        :param file_id: Telegram type: "long".
        :param file_part: Telegram type: "int".
        :param file_total_parts: Telegram type: "int".
        :param bytes: Telegram type: "bytes".

        :returns Bool: This type has no constructors.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.file_id = file_id
        self.file_part = file_part
        self.file_total_parts = file_total_parts
        self.bytes = bytes

    def to_dict(self):
        return {
            'file_id': self.file_id,
            'file_part': self.file_part,
            'file_total_parts': self.file_total_parts,
            'bytes': self.bytes,
        }

    def on_send(self, writer):
        writer.write_int(SaveBigFilePartRequest.constructor_id, signed=False)
        writer.write_long(self.file_id)
        writer.write_int(self.file_part)
        writer.write_int(self.file_total_parts)
        writer.tgwrite_bytes(self.bytes)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return SaveBigFilePartRequest(None, None, None, None)

    def on_response(self, reader):
        self.result = reader.tgread_object()

    def __repr__(self):
        return 'upload.saveBigFilePart#de7b673d file_id:long file_part:int file_total_parts:int bytes:bytes = Bool'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
