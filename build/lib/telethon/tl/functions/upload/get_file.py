from ....tl.tlobject import TLObject


class GetFileRequest(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    upload.getFile#e3a6cfb5 location:InputFileLocation offset:int limit:int = upload.File"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0xe3a6cfb5
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x6c9bd728

    def __init__(self, location, offset, limit):
        """
        :param location: Telegram type: "InputFileLocation".
        :param offset: Telegram type: "int".
        :param limit: Telegram type: "int".

        :returns upload.File: Instance of either File, FileCdnRedirect.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.location = location
        self.offset = offset
        self.limit = limit

    def to_dict(self):
        return {
            'location': None if self.location is None else self.location.to_dict(),
            'offset': self.offset,
            'limit': self.limit,
        }

    def on_send(self, writer):
        writer.write_int(GetFileRequest.constructor_id, signed=False)
        self.location.on_send(writer)
        writer.write_int(self.offset)
        writer.write_int(self.limit)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return GetFileRequest(None, None, None)

    def on_response(self, reader):
        self.result = reader.tgread_object()

    def __repr__(self):
        return 'upload.getFile#e3a6cfb5 location:InputFileLocation offset:int limit:int = upload.File'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
