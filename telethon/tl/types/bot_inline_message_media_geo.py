from ...tl.tlobject import TLObject


class BotInlineMessageMediaGeo(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    botInlineMessageMediaGeo#3a8fd8b8 flags:# geo:GeoPoint reply_markup:flags.2?ReplyMarkup = BotInlineMessage"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x3a8fd8b8
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0xc4910f88

    def __init__(self, geo, reply_markup=None):
        """
        :param geo: Telegram type: "GeoPoint".
        :param reply_markup: Telegram type: "ReplyMarkup".

        Constructor for BotInlineMessage: Instance of either BotInlineMessageMediaAuto, BotInlineMessageText, BotInlineMessageMediaGeo, BotInlineMessageMediaVenue, BotInlineMessageMediaContact.
        """
        super().__init__()

        self.geo = geo
        self.reply_markup = reply_markup

    def to_dict(self):
        return {
            'geo': None if self.geo is None else self.geo.to_dict(),
            'reply_markup': None if self.reply_markup is None else self.reply_markup.to_dict(),
        }

    def on_send(self, writer):
        writer.write_int(BotInlineMessageMediaGeo.constructor_id, signed=False)
        # Calculate the flags. This equals to those flag arguments which are NOT None
        flags = 0
        flags |= (1 << 2) if self.reply_markup else 0
        writer.write_int(flags)

        self.geo.on_send(writer)
        if self.reply_markup:
            self.reply_markup.on_send(writer)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return BotInlineMessageMediaGeo(None, None)

    def on_response(self, reader):
        flags = reader.read_int()

        self.geo = reader.tgread_object()
        if (flags & (1 << 2)) != 0:
            self.reply_markup = reader.tgread_object()

    def __repr__(self):
        return 'botInlineMessageMediaGeo#3a8fd8b8 flags:# geo:GeoPoint reply_markup:flags.2?ReplyMarkup = BotInlineMessage'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
