from ...tl.tlobject import TLObject


class BotInlineMessageMediaContact(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    botInlineMessageMediaContact#35edb4d4 flags:# phone_number:string first_name:string last_name:string reply_markup:flags.2?ReplyMarkup = BotInlineMessage"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x35edb4d4
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0xc4910f88

    def __init__(self, phone_number, first_name, last_name, reply_markup=None):
        """
        :param phone_number: Telegram type: "string".
        :param first_name: Telegram type: "string".
        :param last_name: Telegram type: "string".
        :param reply_markup: Telegram type: "ReplyMarkup".

        Constructor for BotInlineMessage: Instance of either BotInlineMessageMediaAuto, BotInlineMessageText, BotInlineMessageMediaGeo, BotInlineMessageMediaVenue, BotInlineMessageMediaContact.
        """
        super().__init__()

        self.phone_number = phone_number
        self.first_name = first_name
        self.last_name = last_name
        self.reply_markup = reply_markup

    def to_dict(self):
        return {
            'phone_number': self.phone_number,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'reply_markup': None if self.reply_markup is None else self.reply_markup.to_dict(),
        }

    def on_send(self, writer):
        writer.write_int(BotInlineMessageMediaContact.constructor_id, signed=False)
        # Calculate the flags. This equals to those flag arguments which are NOT None
        flags = 0
        flags |= (1 << 2) if self.reply_markup else 0
        writer.write_int(flags)

        writer.tgwrite_string(self.phone_number)
        writer.tgwrite_string(self.first_name)
        writer.tgwrite_string(self.last_name)
        if self.reply_markup:
            self.reply_markup.on_send(writer)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return BotInlineMessageMediaContact(None, None, None, None)

    def on_response(self, reader):
        flags = reader.read_int()

        self.phone_number = reader.tgread_string()
        self.first_name = reader.tgread_string()
        self.last_name = reader.tgread_string()
        if (flags & (1 << 2)) != 0:
            self.reply_markup = reader.tgread_object()

    def __repr__(self):
        return 'botInlineMessageMediaContact#35edb4d4 flags:# phone_number:string first_name:string last_name:string reply_markup:flags.2?ReplyMarkup = BotInlineMessage'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
