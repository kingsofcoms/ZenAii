from ....tl.tlobject import TLObject


class DialogsSlice(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    messages.dialogsSlice#71e094f3 count:int dialogs:Vector<Dialog> messages:Vector<Message> chats:Vector<Chat> users:Vector<User> = messages.Dialogs"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x71e094f3
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0xe1b52ee

    def __init__(self, count, dialogs, messages, chats, users):
        """
        :param count: Telegram type: "int".
        :param dialogs: Telegram type: "Dialog". Must be a list.
        :param messages: Telegram type: "Message". Must be a list.
        :param chats: Telegram type: "Chat". Must be a list.
        :param users: Telegram type: "User". Must be a list.

        Constructor for messages.Dialogs: Instance of either Dialogs, DialogsSlice.
        """
        super().__init__()

        self.count = count
        self.dialogs = dialogs
        self.messages = messages
        self.chats = chats
        self.users = users

    def to_dict(self):
        return {
            'count': self.count,
            'dialogs': [] if self.dialogs is None else [None if x is None else x.to_dict() for x in self.dialogs],
            'messages': [] if self.messages is None else [None if x is None else x.to_dict() for x in self.messages],
            'chats': [] if self.chats is None else [None if x is None else x.to_dict() for x in self.chats],
            'users': [] if self.users is None else [None if x is None else x.to_dict() for x in self.users],
        }

    def on_send(self, writer):
        writer.write_int(DialogsSlice.constructor_id, signed=False)
        writer.write_int(self.count)
        writer.write_int(0x1cb5c415, signed=False)  # Vector's constructor ID
        writer.write_int(len(self.dialogs))
        for _x in self.dialogs:
            _x.on_send(writer)

        writer.write_int(0x1cb5c415, signed=False)  # Vector's constructor ID
        writer.write_int(len(self.messages))
        for _x in self.messages:
            _x.on_send(writer)

        writer.write_int(0x1cb5c415, signed=False)  # Vector's constructor ID
        writer.write_int(len(self.chats))
        for _x in self.chats:
            _x.on_send(writer)

        writer.write_int(0x1cb5c415, signed=False)  # Vector's constructor ID
        writer.write_int(len(self.users))
        for _x in self.users:
            _x.on_send(writer)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return DialogsSlice(None, None, None, None, None)

    def on_response(self, reader):
        self.count = reader.read_int()
        reader.read_int()  # Vector's constructor ID
        self.dialogs = []  # Initialize an empty list
        _len = reader.read_int()
        for _ in range(_len):
            _x = reader.tgread_object()
            self.dialogs.append(_x)

        reader.read_int()  # Vector's constructor ID
        self.messages = []  # Initialize an empty list
        _len = reader.read_int()
        for _ in range(_len):
            _x = reader.tgread_object()
            self.messages.append(_x)

        reader.read_int()  # Vector's constructor ID
        self.chats = []  # Initialize an empty list
        _len = reader.read_int()
        for _ in range(_len):
            _x = reader.tgread_object()
            self.chats.append(_x)

        reader.read_int()  # Vector's constructor ID
        self.users = []  # Initialize an empty list
        _len = reader.read_int()
        for _ in range(_len):
            _x = reader.tgread_object()
            self.users.append(_x)

    def __repr__(self):
        return 'messages.dialogsSlice#71e094f3 count:int dialogs:Vector<Dialog> messages:Vector<Message> chats:Vector<Chat> users:Vector<User> = messages.Dialogs'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
