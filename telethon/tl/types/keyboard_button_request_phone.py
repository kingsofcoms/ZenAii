from ...tl.tlobject import TLObject


class KeyboardButtonRequestPhone(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    keyboardButtonRequestPhone#b16a6c29 text:string = KeyboardButton"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0xb16a6c29
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0xbad74a3

    def __init__(self, text):
        """
        :param text: Telegram type: "string".

        Constructor for KeyboardButton: Instance of either KeyboardButton, KeyboardButtonUrl, KeyboardButtonCallback, KeyboardButtonRequestPhone, KeyboardButtonRequestGeoLocation, KeyboardButtonSwitchInline, KeyboardButtonGame, KeyboardButtonBuy.
        """
        super().__init__()

        self.text = text

    def to_dict(self):
        return {
            'text': self.text,
        }

    def on_send(self, writer):
        writer.write_int(KeyboardButtonRequestPhone.constructor_id, signed=False)
        writer.tgwrite_string(self.text)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return KeyboardButtonRequestPhone(None)

    def on_response(self, reader):
        self.text = reader.tgread_string()

    def __repr__(self):
        return 'keyboardButtonRequestPhone#b16a6c29 text:string = KeyboardButton'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
