from ....tl.tlobject import TLObject


class BindTempAuthKeyRequest(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    auth.bindTempAuthKey#cdd42a05 perm_auth_key_id:long nonce:long expires_at:int encrypted_message:bytes = Bool"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0xcdd42a05
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0xf5b399ac

    def __init__(self, perm_auth_key_id, nonce, expires_at, encrypted_message):
        """
        :param perm_auth_key_id: Telegram type: "long".
        :param nonce: Telegram type: "long".
        :param expires_at: Telegram type: "date".
        :param encrypted_message: Telegram type: "bytes".

        :returns Bool: This type has no constructors.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.perm_auth_key_id = perm_auth_key_id
        self.nonce = nonce
        self.expires_at = expires_at
        self.encrypted_message = encrypted_message

    def to_dict(self):
        return {
            'perm_auth_key_id': self.perm_auth_key_id,
            'nonce': self.nonce,
            'expires_at': self.expires_at,
            'encrypted_message': self.encrypted_message,
        }

    def on_send(self, writer):
        writer.write_int(BindTempAuthKeyRequest.constructor_id, signed=False)
        writer.write_long(self.perm_auth_key_id)
        writer.write_long(self.nonce)
        writer.tgwrite_date(self.expires_at)
        writer.tgwrite_bytes(self.encrypted_message)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return BindTempAuthKeyRequest(None, None, None, None)

    def on_response(self, reader):
        self.result = reader.tgread_object()

    def __repr__(self):
        return 'auth.bindTempAuthKey#cdd42a05 perm_auth_key_id:long nonce:long expires_at:int encrypted_message:bytes = Bool'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
