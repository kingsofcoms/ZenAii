from ....tl.tlobject import TLObject


class TmpPassword(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    account.tmpPassword#db64fd34 tmp_password:bytes valid_until:int = account.TmpPassword"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0xdb64fd34
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0xb064992d

    def __init__(self, tmp_password, valid_until):
        """
        :param tmp_password: Telegram type: "bytes".
        :param valid_until: Telegram type: "int".

        Constructor for account.TmpPassword: Instance of TmpPassword.
        """
        super().__init__()

        self.tmp_password = tmp_password
        self.valid_until = valid_until

    def to_dict(self):
        return {
            'tmp_password': self.tmp_password,
            'valid_until': self.valid_until,
        }

    def on_send(self, writer):
        writer.write_int(TmpPassword.constructor_id, signed=False)
        writer.tgwrite_bytes(self.tmp_password)
        writer.write_int(self.valid_until)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return TmpPassword(None, None)

    def on_response(self, reader):
        self.tmp_password = reader.tgread_bytes()
        self.valid_until = reader.read_int()

    def __repr__(self):
        return 'account.tmpPassword#db64fd34 tmp_password:bytes valid_until:int = account.TmpPassword'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
