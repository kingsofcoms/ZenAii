from ...tl.tlobject import TLObject


class InputMessagesFilterUrl(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    inputMessagesFilterUrl#7ef0dd87 = MessagesFilter"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x7ef0dd87
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x8a36ec14

    def __init__(self):
        super().__init__()

    @staticmethod
    def to_dict():
        return {}

    def on_send(self, writer):
        writer.write_int(InputMessagesFilterUrl.constructor_id, signed=False)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return InputMessagesFilterUrl()

    def on_response(self, reader):
        pass

    def __repr__(self):
        return 'inputMessagesFilterUrl#7ef0dd87 = MessagesFilter'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
