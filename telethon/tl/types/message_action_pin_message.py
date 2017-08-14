from ...tl.tlobject import TLObject


class MessageActionPinMessage(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    messageActionPinMessage#94bd38ed = MessageAction"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x94bd38ed
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x8680d126

    def __init__(self):
        super().__init__()

    @staticmethod
    def to_dict():
        return {}

    def on_send(self, writer):
        writer.write_int(MessageActionPinMessage.constructor_id, signed=False)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return MessageActionPinMessage()

    def on_response(self, reader):
        pass

    def __repr__(self):
        return 'messageActionPinMessage#94bd38ed = MessageAction'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
