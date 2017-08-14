from ....tl.tlobject import TLObject
from ....utils import get_input_user


class EditChatAdminRequest(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    messages.editChatAdmin#a9e69f2e chat_id:int user_id:InputUser is_admin:Bool = Bool"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0xa9e69f2e
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0xf5b399ac

    def __init__(self, chat_id, user_id, is_admin):
        """
        :param chat_id: Telegram type: "int".
        :param user_id: Telegram type: "InputUser".
        :param is_admin: Telegram type: "Bool".

        :returns Bool: This type has no constructors.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.chat_id = chat_id
        self.user_id = get_input_user(user_id)
        self.is_admin = is_admin

    def to_dict(self):
        return {
            'chat_id': self.chat_id,
            'user_id': None if self.user_id is None else self.user_id.to_dict(),
            'is_admin': self.is_admin,
        }

    def on_send(self, writer):
        writer.write_int(EditChatAdminRequest.constructor_id, signed=False)
        writer.write_int(self.chat_id)
        self.user_id.on_send(writer)
        writer.tgwrite_bool(self.is_admin)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return EditChatAdminRequest(None, None, None)

    def on_response(self, reader):
        self.result = reader.tgread_object()

    def __repr__(self):
        return 'messages.editChatAdmin#a9e69f2e chat_id:int user_id:InputUser is_admin:Bool = Bool'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
