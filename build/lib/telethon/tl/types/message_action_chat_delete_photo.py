from ...tl.tlobject import TLObject


class MessageActionChatDeletePhoto(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    messageActionChatDeletePhoto#95e3fbef = MessageAction"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x95e3fbef
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x8680d126

    def __init__(self):
        super().__init__()

    @staticmethod
    def to_dict():
        return {}

    def on_send(self, writer):
        writer.write_int(MessageActionChatDeletePhoto.constructor_id, signed=False)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return MessageActionChatDeletePhoto()

    def on_response(self, reader):
        pass

    def __repr__(self):
        return 'messageActionChatDeletePhoto#95e3fbef = MessageAction'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
