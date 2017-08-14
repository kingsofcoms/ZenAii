from ...tl.tlobject import TLObject


class ChatParticipant(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    chatParticipant#c8d7493e user_id:int inviter_id:int date:int = ChatParticipant"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0xc8d7493e
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x7d7c6f86

    def __init__(self, user_id, inviter_id, date):
        """
        :param user_id: Telegram type: "int".
        :param inviter_id: Telegram type: "int".
        :param date: Telegram type: "date".

        Constructor for ChatParticipant: Instance of either ChatParticipant, ChatParticipantCreator, ChatParticipantAdmin.
        """
        super().__init__()

        self.user_id = user_id
        self.inviter_id = inviter_id
        self.date = date

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'inviter_id': self.inviter_id,
            'date': self.date,
        }

    def on_send(self, writer):
        writer.write_int(ChatParticipant.constructor_id, signed=False)
        writer.write_int(self.user_id)
        writer.write_int(self.inviter_id)
        writer.tgwrite_date(self.date)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return ChatParticipant(None, None, None)

    def on_response(self, reader):
        self.user_id = reader.read_int()
        self.inviter_id = reader.read_int()
        self.date = reader.tgread_date()

    def __repr__(self):
        return 'chatParticipant#c8d7493e user_id:int inviter_id:int date:int = ChatParticipant'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
