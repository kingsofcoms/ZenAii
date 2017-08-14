from ...tl.tlobject import TLObject


class InputDocument(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    inputDocument#18798952 id:long access_hash:long = InputDocument"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x18798952
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0xf33fdb68

    def __init__(self, id, access_hash):
        """
        :param id: Telegram type: "long".
        :param access_hash: Telegram type: "long".

        Constructor for InputDocument: Instance of either InputDocumentEmpty, InputDocument.
        """
        super().__init__()

        self.id = id
        self.access_hash = access_hash

    def to_dict(self):
        return {
            'id': self.id,
            'access_hash': self.access_hash,
        }

    def on_send(self, writer):
        writer.write_int(InputDocument.constructor_id, signed=False)
        writer.write_long(self.id)
        writer.write_long(self.access_hash)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return InputDocument(None, None)

    def on_response(self, reader):
        self.id = reader.read_long()
        self.access_hash = reader.read_long()

    def __repr__(self):
        return 'inputDocument#18798952 id:long access_hash:long = InputDocument'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
