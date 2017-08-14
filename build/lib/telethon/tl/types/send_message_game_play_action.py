from ...tl.tlobject import TLObject


class SendMessageGamePlayAction(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    sendMessageGamePlayAction#dd6a8f48 = SendMessageAction"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0xdd6a8f48
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x20b2cc21

    def __init__(self):
        super().__init__()

    @staticmethod
    def to_dict():
        return {}

    def on_send(self, writer):
        writer.write_int(SendMessageGamePlayAction.constructor_id, signed=False)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return SendMessageGamePlayAction()

    def on_response(self, reader):
        pass

    def __repr__(self):
        return 'sendMessageGamePlayAction#dd6a8f48 = SendMessageAction'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
