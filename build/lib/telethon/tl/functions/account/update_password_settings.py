from ....tl.tlobject import TLObject


class UpdatePasswordSettingsRequest(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    account.updatePasswordSettings#fa7c4b86 current_password_hash:bytes new_settings:account.PasswordInputSettings = Bool"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0xfa7c4b86
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0xf5b399ac

    def __init__(self, current_password_hash, new_settings):
        """
        :param current_password_hash: Telegram type: "bytes".
        :param new_settings: Telegram type: "account.PasswordInputSettings".

        :returns Bool: This type has no constructors.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.current_password_hash = current_password_hash
        self.new_settings = new_settings

    def to_dict(self):
        return {
            'current_password_hash': self.current_password_hash,
            'new_settings': None if self.new_settings is None else self.new_settings.to_dict(),
        }

    def on_send(self, writer):
        writer.write_int(UpdatePasswordSettingsRequest.constructor_id, signed=False)
        writer.tgwrite_bytes(self.current_password_hash)
        self.new_settings.on_send(writer)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return UpdatePasswordSettingsRequest(None, None)

    def on_response(self, reader):
        self.result = reader.tgread_object()

    def __repr__(self):
        return 'account.updatePasswordSettings#fa7c4b86 current_password_hash:bytes new_settings:account.PasswordInputSettings = Bool'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
