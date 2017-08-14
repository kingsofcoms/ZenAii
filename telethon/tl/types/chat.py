from ...tl.tlobject import TLObject


class Chat(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    chat#d91cdd54 flags:# creator:flags.0?true kicked:flags.1?true left:flags.2?true admins_enabled:flags.3?true admin:flags.4?true deactivated:flags.5?true id:int title:string photo:ChatPhoto participants_count:int date:int version:int migrated_to:flags.6?InputChannel = Chat"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0xd91cdd54
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0xc5af5d94

    def __init__(self, id, title, photo, participants_count, date, version, creator=None, kicked=None, left=None, admins_enabled=None, admin=None, deactivated=None, migrated_to=None):
        """
        :param creator: Telegram type: "true".
        :param kicked: Telegram type: "true".
        :param left: Telegram type: "true".
        :param admins_enabled: Telegram type: "true".
        :param admin: Telegram type: "true".
        :param deactivated: Telegram type: "true".
        :param id: Telegram type: "int".
        :param title: Telegram type: "string".
        :param photo: Telegram type: "ChatPhoto".
        :param participants_count: Telegram type: "int".
        :param date: Telegram type: "date".
        :param version: Telegram type: "int".
        :param migrated_to: Telegram type: "InputChannel".

        Constructor for Chat: Instance of either ChatEmpty, Chat, ChatForbidden, Channel, ChannelForbidden.
        """
        super().__init__()

        self.creator = creator
        self.kicked = kicked
        self.left = left
        self.admins_enabled = admins_enabled
        self.admin = admin
        self.deactivated = deactivated
        self.id = id
        self.title = title
        self.photo = photo
        self.participants_count = participants_count
        self.date = date
        self.version = version
        self.migrated_to = migrated_to

    def to_dict(self):
        return {
            'creator': self.creator,
            'kicked': self.kicked,
            'left': self.left,
            'admins_enabled': self.admins_enabled,
            'admin': self.admin,
            'deactivated': self.deactivated,
            'id': self.id,
            'title': self.title,
            'photo': None if self.photo is None else self.photo.to_dict(),
            'participants_count': self.participants_count,
            'date': self.date,
            'version': self.version,
            'migrated_to': None if self.migrated_to is None else self.migrated_to.to_dict(),
        }

    def on_send(self, writer):
        writer.write_int(Chat.constructor_id, signed=False)
        # Calculate the flags. This equals to those flag arguments which are NOT None
        flags = 0
        flags |= (1 << 0) if self.creator else 0
        flags |= (1 << 1) if self.kicked else 0
        flags |= (1 << 2) if self.left else 0
        flags |= (1 << 3) if self.admins_enabled else 0
        flags |= (1 << 4) if self.admin else 0
        flags |= (1 << 5) if self.deactivated else 0
        flags |= (1 << 6) if self.migrated_to else 0
        writer.write_int(flags)

        writer.write_int(self.id)
        writer.tgwrite_string(self.title)
        self.photo.on_send(writer)
        writer.write_int(self.participants_count)
        writer.tgwrite_date(self.date)
        writer.write_int(self.version)
        if self.migrated_to:
            self.migrated_to.on_send(writer)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return Chat(None, None, None, None, None, None, None, None, None, None, None, None, None)

    def on_response(self, reader):
        flags = reader.read_int()

        if (flags & (1 << 0)) != 0:
            self.creator = True  # Arbitrary not-None value, no need to read since it is a flag

        if (flags & (1 << 1)) != 0:
            self.kicked = True  # Arbitrary not-None value, no need to read since it is a flag

        if (flags & (1 << 2)) != 0:
            self.left = True  # Arbitrary not-None value, no need to read since it is a flag

        if (flags & (1 << 3)) != 0:
            self.admins_enabled = True  # Arbitrary not-None value, no need to read since it is a flag

        if (flags & (1 << 4)) != 0:
            self.admin = True  # Arbitrary not-None value, no need to read since it is a flag

        if (flags & (1 << 5)) != 0:
            self.deactivated = True  # Arbitrary not-None value, no need to read since it is a flag

        self.id = reader.read_int()
        self.title = reader.tgread_string()
        self.photo = reader.tgread_object()
        self.participants_count = reader.read_int()
        self.date = reader.tgread_date()
        self.version = reader.read_int()
        if (flags & (1 << 6)) != 0:
            self.migrated_to = reader.tgread_object()

    def __repr__(self):
        return 'chat#d91cdd54 flags:# creator:flags.0?true kicked:flags.1?true left:flags.2?true admins_enabled:flags.3?true admin:flags.4?true deactivated:flags.5?true id:int title:string photo:ChatPhoto participants_count:int date:int version:int migrated_to:flags.6?InputChannel = Chat'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
