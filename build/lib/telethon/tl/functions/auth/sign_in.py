from ....tl.tlobject import TLObject


class SignInRequest(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    auth.signIn#bcd51581 phone_number:string phone_code_hash:string phone_code:string = auth.Authorization"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0xbcd51581
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0xb9e04e39

    def __init__(self, phone_number, phone_code_hash, phone_code):
        """
        :param phone_number: Telegram type: "string".
        :param phone_code_hash: Telegram type: "string".
        :param phone_code: Telegram type: "string".

        :returns auth.Authorization: Instance of Authorization.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.phone_number = phone_number
        self.phone_code_hash = phone_code_hash
        self.phone_code = phone_code

    def to_dict(self):
        return {
            'phone_number': self.phone_number,
            'phone_code_hash': self.phone_code_hash,
            'phone_code': self.phone_code,
        }

    def on_send(self, writer):
        writer.write_int(SignInRequest.constructor_id, signed=False)
        writer.tgwrite_string(self.phone_number)
        writer.tgwrite_string(self.phone_code_hash)
        writer.tgwrite_string(self.phone_code)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return SignInRequest(None, None, None)

    def on_response(self, reader):
        self.result = reader.tgread_object()

    def __repr__(self):
        return 'auth.signIn#bcd51581 phone_number:string phone_code_hash:string phone_code:string = auth.Authorization'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
