from ...tl.tlobject import TLObject


class InputUser(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    inputUser#d8292816 user_id:int access_hash:long = InputUser"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0xd8292816
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0xe669bf46

    def __init__(self, user_id, access_hash):
        """
        :param user_id: Telegram type: "int".
        :param access_hash: Telegram type: "long".

        Constructor for InputUser: Instance of either InputUserEmpty, InputUserSelf, InputUser.
        """
        super().__init__()

        self.user_id = user_id
        self.access_hash = access_hash

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'access_hash': self.access_hash,
        }

    def on_send(self, writer):
        writer.write_int(InputUser.constructor_id, signed=False)
        writer.write_int(self.user_id)
        writer.write_long(self.access_hash)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return InputUser(None, None)

    def on_response(self, reader):
        self.user_id = reader.read_int()
        self.access_hash = reader.read_long()

    def __repr__(self):
        return 'inputUser#d8292816 user_id:int access_hash:long = InputUser'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
