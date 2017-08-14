from ...tl.tlobject import TLObject


class MessageEmpty(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    messageEmpty#83e5de54 id:int = Message"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x83e5de54
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x790009e3

    def __init__(self, id):
        """
        :param id: Telegram type: "int".

        Constructor for Message: Instance of either MessageEmpty, Message, MessageService.
        """
        super().__init__()

        self.id = id

    def to_dict(self):
        return {
            'id': self.id,
        }

    def on_send(self, writer):
        writer.write_int(MessageEmpty.constructor_id, signed=False)
        writer.write_int(self.id)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return MessageEmpty(None)

    def on_response(self, reader):
        self.id = reader.read_int()

    def __repr__(self):
        return 'messageEmpty#83e5de54 id:int = Message'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
