from ...tl.tlobject import TLObject


class MessageEntityMention(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    messageEntityMention#fa04579d offset:int length:int = MessageEntity"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0xfa04579d
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0xcf6419dc

    def __init__(self, offset, length):
        """
        :param offset: Telegram type: "int".
        :param length: Telegram type: "int".

        Constructor for MessageEntity: Instance of either MessageEntityUnknown, MessageEntityMention, MessageEntityHashtag, MessageEntityBotCommand, MessageEntityUrl, MessageEntityEmail, MessageEntityBold, MessageEntityItalic, MessageEntityCode, MessageEntityPre, MessageEntityTextUrl, MessageEntityMentionName, InputMessageEntityMentionName.
        """
        super().__init__()

        self.offset = offset
        self.length = length

    def to_dict(self):
        return {
            'offset': self.offset,
            'length': self.length,
        }

    def on_send(self, writer):
        writer.write_int(MessageEntityMention.constructor_id, signed=False)
        writer.write_int(self.offset)
        writer.write_int(self.length)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return MessageEntityMention(None, None)

    def on_response(self, reader):
        self.offset = reader.read_int()
        self.length = reader.read_int()

    def __repr__(self):
        return 'messageEntityMention#fa04579d offset:int length:int = MessageEntity'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
