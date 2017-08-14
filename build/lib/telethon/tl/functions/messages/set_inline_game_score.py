from ....tl.tlobject import TLObject
from ....utils import get_input_user


class SetInlineGameScoreRequest(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    messages.setInlineGameScore#15ad9f64 flags:# edit_message:flags.0?true force:flags.1?true id:InputBotInlineMessageID user_id:InputUser score:int = Bool"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x15ad9f64
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0xf5b399ac

    def __init__(self, id, user_id, score, edit_message=None, force=None):
        """
        :param edit_message: Telegram type: "true".
        :param force: Telegram type: "true".
        :param id: Telegram type: "InputBotInlineMessageID".
        :param user_id: Telegram type: "InputUser".
        :param score: Telegram type: "int".

        :returns Bool: This type has no constructors.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.edit_message = edit_message
        self.force = force
        self.id = id
        self.user_id = get_input_user(user_id)
        self.score = score

    def to_dict(self):
        return {
            'edit_message': self.edit_message,
            'force': self.force,
            'id': None if self.id is None else self.id.to_dict(),
            'user_id': None if self.user_id is None else self.user_id.to_dict(),
            'score': self.score,
        }

    def on_send(self, writer):
        writer.write_int(SetInlineGameScoreRequest.constructor_id, signed=False)
        # Calculate the flags. This equals to those flag arguments which are NOT None
        flags = 0
        flags |= (1 << 0) if self.edit_message else 0
        flags |= (1 << 1) if self.force else 0
        writer.write_int(flags)

        self.id.on_send(writer)
        self.user_id.on_send(writer)
        writer.write_int(self.score)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return SetInlineGameScoreRequest(None, None, None, None, None)

    def on_response(self, reader):
        self.result = reader.tgread_object()

    def __repr__(self):
        return 'messages.setInlineGameScore#15ad9f64 flags:# edit_message:flags.0?true force:flags.1?true id:InputBotInlineMessageID user_id:InputUser score:int = Bool'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
