from ....tl.tlobject import TLObject


class AdminLogResults(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    channels.adminLogResults#ed8af74d events:Vector<ChannelAdminLogEvent> chats:Vector<Chat> users:Vector<User> = channels.AdminLogResults"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0xed8af74d
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x51f076bc

    def __init__(self, events, chats, users):
        """
        :param events: Telegram type: "ChannelAdminLogEvent". Must be a list.
        :param chats: Telegram type: "Chat". Must be a list.
        :param users: Telegram type: "User". Must be a list.

        Constructor for channels.AdminLogResults: Instance of AdminLogResults.
        """
        super().__init__()

        self.events = events
        self.chats = chats
        self.users = users

    def to_dict(self):
        return {
            'events': [] if self.events is None else [None if x is None else x.to_dict() for x in self.events],
            'chats': [] if self.chats is None else [None if x is None else x.to_dict() for x in self.chats],
            'users': [] if self.users is None else [None if x is None else x.to_dict() for x in self.users],
        }

    def on_send(self, writer):
        writer.write_int(AdminLogResults.constructor_id, signed=False)
        writer.write_int(0x1cb5c415, signed=False)  # Vector's constructor ID
        writer.write_int(len(self.events))
        for _x in self.events:
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
        return AdminLogResults(None, None, None)

    def on_response(self, reader):
        reader.read_int()  # Vector's constructor ID
        self.events = []  # Initialize an empty list
        _len = reader.read_int()
        for _ in range(_len):
            _x = reader.tgread_object()
            self.events.append(_x)

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
        return 'channels.adminLogResults#ed8af74d events:Vector<ChannelAdminLogEvent> chats:Vector<Chat> users:Vector<User> = channels.AdminLogResults'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
