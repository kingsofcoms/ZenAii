from ....tl.tlobject import TLObject


class PasswordRecovery(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    auth.passwordRecovery#137948a5 email_pattern:string = auth.PasswordRecovery"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x137948a5
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0xfa72d43a

    def __init__(self, email_pattern):
        """
        :param email_pattern: Telegram type: "string".

        Constructor for auth.PasswordRecovery: Instance of PasswordRecovery.
        """
        super().__init__()

        self.email_pattern = email_pattern

    def to_dict(self):
        return {
            'email_pattern': self.email_pattern,
        }

    def on_send(self, writer):
        writer.write_int(PasswordRecovery.constructor_id, signed=False)
        writer.tgwrite_string(self.email_pattern)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return PasswordRecovery(None)

    def on_response(self, reader):
        self.email_pattern = reader.tgread_string()

    def __repr__(self):
        return 'auth.passwordRecovery#137948a5 email_pattern:string = auth.PasswordRecovery'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
