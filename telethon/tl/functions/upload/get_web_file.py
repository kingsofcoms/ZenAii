from ....tl.tlobject import TLObject


class GetWebFileRequest(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    upload.getWebFile#24e6818d location:InputWebFileLocation offset:int limit:int = upload.WebFile"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x24e6818d
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x68f17f51

    def __init__(self, location, offset, limit):
        """
        :param location: Telegram type: "InputWebFileLocation".
        :param offset: Telegram type: "int".
        :param limit: Telegram type: "int".

        :returns upload.WebFile: Instance of WebFile.
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
        writer.write_int(GetWebFileRequest.constructor_id, signed=False)
        self.location.on_send(writer)
        writer.write_int(self.offset)
        writer.write_int(self.limit)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return GetWebFileRequest(None, None, None)

    def on_response(self, reader):
        self.result = reader.tgread_object()

    def __repr__(self):
        return 'upload.getWebFile#24e6818d location:InputWebFileLocation offset:int limit:int = upload.WebFile'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
