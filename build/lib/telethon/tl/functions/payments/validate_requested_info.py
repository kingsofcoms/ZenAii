from ....tl.tlobject import TLObject


class ValidateRequestedInfoRequest(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    payments.validateRequestedInfo#770a8e74 flags:# save:flags.0?true msg_id:int info:PaymentRequestedInfo = payments.ValidatedRequestedInfo"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x770a8e74
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x8f8044b7

    def __init__(self, msg_id, info, save=None):
        """
        :param save: Telegram type: "true".
        :param msg_id: Telegram type: "int".
        :param info: Telegram type: "PaymentRequestedInfo".

        :returns payments.ValidatedRequestedInfo: Instance of ValidatedRequestedInfo.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.save = save
        self.msg_id = msg_id
        self.info = info

    def to_dict(self):
        return {
            'save': self.save,
            'msg_id': self.msg_id,
            'info': None if self.info is None else self.info.to_dict(),
        }

    def on_send(self, writer):
        writer.write_int(ValidateRequestedInfoRequest.constructor_id, signed=False)
        # Calculate the flags. This equals to those flag arguments which are NOT None
        flags = 0
        flags |= (1 << 0) if self.save else 0
        writer.write_int(flags)

        writer.write_int(self.msg_id)
        self.info.on_send(writer)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return ValidateRequestedInfoRequest(None, None, None)

    def on_response(self, reader):
        self.result = reader.tgread_object()

    def __repr__(self):
        return 'payments.validateRequestedInfo#770a8e74 flags:# save:flags.0?true msg_id:int info:PaymentRequestedInfo = payments.ValidatedRequestedInfo'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
