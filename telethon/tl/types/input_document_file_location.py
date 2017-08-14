from ...tl.tlobject import TLObject


class InputDocumentFileLocation(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    inputDocumentFileLocation#430f0724 id:long access_hash:long version:int = InputFileLocation"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x430f0724
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x1523d462

    def __init__(self, id, access_hash, version):
        """
        :param id: Telegram type: "long".
        :param access_hash: Telegram type: "long".
        :param version: Telegram type: "int".

        Constructor for InputFileLocation: Instance of either InputFileLocation, InputEncryptedFileLocation, InputDocumentFileLocation.
        """
        super().__init__()

        self.id = id
        self.access_hash = access_hash
        self.version = version

    def to_dict(self):
        return {
            'id': self.id,
            'access_hash': self.access_hash,
            'version': self.version,
        }

    def on_send(self, writer):
        writer.write_int(InputDocumentFileLocation.constructor_id, signed=False)
        writer.write_long(self.id)
        writer.write_long(self.access_hash)
        writer.write_int(self.version)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return InputDocumentFileLocation(None, None, None)

    def on_response(self, reader):
        self.id = reader.read_long()
        self.access_hash = reader.read_long()
        self.version = reader.read_int()

    def __repr__(self):
        return 'inputDocumentFileLocation#430f0724 id:long access_hash:long version:int = InputFileLocation'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
