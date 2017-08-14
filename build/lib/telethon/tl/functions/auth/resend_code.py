from ....tl.tlobject import TLObject


class ResendCodeRequest(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    auth.resendCode#3ef1a9bf phone_number:string phone_code_hash:string = auth.SentCode"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x3ef1a9bf
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x6ce87081

    def __init__(self, phone_number, phone_code_hash):
        """
        :param phone_number: Telegram type: "string".
        :param phone_code_hash: Telegram type: "string".

        :returns auth.SentCode: Instance of SentCode.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.phone_number = phone_number
        self.phone_code_hash = phone_code_hash

    def to_dict(self):
        return {
            'phone_number': self.phone_number,
            'phone_code_hash': self.phone_code_hash,
        }

    def on_send(self, writer):
        writer.write_int(ResendCodeRequest.constructor_id, signed=False)
        writer.tgwrite_string(self.phone_number)
        writer.tgwrite_string(self.phone_code_hash)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return ResendCodeRequest(None, None)

    def on_response(self, reader):
        self.result = reader.tgread_object()

    def __repr__(self):
        return 'auth.resendCode#3ef1a9bf phone_number:string phone_code_hash:string = auth.SentCode'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
