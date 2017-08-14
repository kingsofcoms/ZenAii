from ...tl.tlobject import TLObject


class ReplyKeyboardHide(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    replyKeyboardHide#a03e5b85 flags:# selective:flags.2?true = ReplyMarkup"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0xa03e5b85
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0xe2e10ef2

    def __init__(self, selective=None):
        """
        :param selective: Telegram type: "true".

        Constructor for ReplyMarkup: Instance of either ReplyKeyboardHide, ReplyKeyboardForceReply, ReplyKeyboardMarkup, ReplyInlineMarkup.
        """
        super().__init__()

        self.selective = selective

    def to_dict(self):
        return {
            'selective': self.selective,
        }

    def on_send(self, writer):
        writer.write_int(ReplyKeyboardHide.constructor_id, signed=False)
        # Calculate the flags. This equals to those flag arguments which are NOT None
        flags = 0
        flags |= (1 << 2) if self.selective else 0
        writer.write_int(flags)


    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return ReplyKeyboardHide(None)

    def on_response(self, reader):
        flags = reader.read_int()

        if (flags & (1 << 2)) != 0:
            self.selective = True  # Arbitrary not-None value, no need to read since it is a flag

    def __repr__(self):
        return 'replyKeyboardHide#a03e5b85 flags:# selective:flags.2?true = ReplyMarkup'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
