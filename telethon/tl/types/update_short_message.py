from ...tl.tlobject import TLObject


class UpdateShortMessage(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    updateShortMessage#914fbf11 flags:# out:flags.1?true mentioned:flags.4?true media_unread:flags.5?true silent:flags.13?true id:int user_id:int message:string pts:int pts_count:int date:int fwd_from:flags.2?MessageFwdHeader via_bot_id:flags.11?int reply_to_msg_id:flags.3?int entities:flags.7?Vector<MessageEntity> = Updates"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x914fbf11
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x8af52aac

    def __init__(self, id, user_id, message, pts, pts_count, date, out=None, mentioned=None, media_unread=None, silent=None, fwd_from=None, via_bot_id=None, reply_to_msg_id=None, entities=None):
        """
        :param out: Telegram type: "true".
        :param mentioned: Telegram type: "true".
        :param media_unread: Telegram type: "true".
        :param silent: Telegram type: "true".
        :param id: Telegram type: "int".
        :param user_id: Telegram type: "int".
        :param message: Telegram type: "string".
        :param pts: Telegram type: "int".
        :param pts_count: Telegram type: "int".
        :param date: Telegram type: "date".
        :param fwd_from: Telegram type: "MessageFwdHeader".
        :param via_bot_id: Telegram type: "int".
        :param reply_to_msg_id: Telegram type: "int".
        :param entities: Telegram type: "MessageEntity". Must be a list.

        Constructor for Updates: Instance of either UpdatesTooLong, UpdateShortMessage, UpdateShortChatMessage, UpdateShort, UpdatesCombined, UpdatesTg, UpdateShortSentMessage.
        """
        super().__init__()

        self.out = out
        self.mentioned = mentioned
        self.media_unread = media_unread
        self.silent = silent
        self.id = id
        self.user_id = user_id
        self.message = message
        self.pts = pts
        self.pts_count = pts_count
        self.date = date
        self.fwd_from = fwd_from
        self.via_bot_id = via_bot_id
        self.reply_to_msg_id = reply_to_msg_id
        self.entities = entities

    def to_dict(self):
        return {
            'out': self.out,
            'mentioned': self.mentioned,
            'media_unread': self.media_unread,
            'silent': self.silent,
            'id': self.id,
            'user_id': self.user_id,
            'message': self.message,
            'pts': self.pts,
            'pts_count': self.pts_count,
            'date': self.date,
            'fwd_from': None if self.fwd_from is None else self.fwd_from.to_dict(),
            'via_bot_id': self.via_bot_id,
            'reply_to_msg_id': self.reply_to_msg_id,
            'entities': [] if self.entities is None else [None if x is None else x.to_dict() for x in self.entities],
        }

    def on_send(self, writer):
        writer.write_int(UpdateShortMessage.constructor_id, signed=False)
        # Calculate the flags. This equals to those flag arguments which are NOT None
        flags = 0
        flags |= (1 << 1) if self.out else 0
        flags |= (1 << 4) if self.mentioned else 0
        flags |= (1 << 5) if self.media_unread else 0
        flags |= (1 << 13) if self.silent else 0
        flags |= (1 << 2) if self.fwd_from else 0
        flags |= (1 << 11) if self.via_bot_id else 0
        flags |= (1 << 3) if self.reply_to_msg_id else 0
        flags |= (1 << 7) if self.entities else 0
        writer.write_int(flags)

        writer.write_int(self.id)
        writer.write_int(self.user_id)
        writer.tgwrite_string(self.message)
        writer.write_int(self.pts)
        writer.write_int(self.pts_count)
        writer.tgwrite_date(self.date)
        if self.fwd_from:
            self.fwd_from.on_send(writer)

        if self.via_bot_id:
            writer.write_int(self.via_bot_id)

        if self.reply_to_msg_id:
            writer.write_int(self.reply_to_msg_id)

        if self.entities:
            writer.write_int(0x1cb5c415, signed=False)  # Vector's constructor ID
            writer.write_int(len(self.entities))
            for _x in self.entities:
                if _x:
                    _x.on_send(writer)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return UpdateShortMessage(None, None, None, None, None, None, None, None, None, None, None, None, None, None)

    def on_response(self, reader):
        flags = reader.read_int()

        if (flags & (1 << 1)) != 0:
            self.out = True  # Arbitrary not-None value, no need to read since it is a flag

        if (flags & (1 << 4)) != 0:
            self.mentioned = True  # Arbitrary not-None value, no need to read since it is a flag

        if (flags & (1 << 5)) != 0:
            self.media_unread = True  # Arbitrary not-None value, no need to read since it is a flag

        if (flags & (1 << 13)) != 0:
            self.silent = True  # Arbitrary not-None value, no need to read since it is a flag

        self.id = reader.read_int()
        self.user_id = reader.read_int()
        self.message = reader.tgread_string()
        self.pts = reader.read_int()
        self.pts_count = reader.read_int()
        self.date = reader.tgread_date()
        if (flags & (1 << 2)) != 0:
            self.fwd_from = reader.tgread_object()

        if (flags & (1 << 11)) != 0:
            self.via_bot_id = reader.read_int()

        if (flags & (1 << 3)) != 0:
            self.reply_to_msg_id = reader.read_int()

        if (flags & (1 << 7)) != 0:
            reader.read_int()  # Vector's constructor ID
            self.entities = []  # Initialize an empty list
            _len = reader.read_int()
            for _ in range(_len):
                _x = reader.tgread_object()
                self.entities.append(_x)

    def __repr__(self):
        return 'updateShortMessage#914fbf11 flags:# out:flags.1?true mentioned:flags.4?true media_unread:flags.5?true silent:flags.13?true id:int user_id:int message:string pts:int pts_count:int date:int fwd_from:flags.2?MessageFwdHeader via_bot_id:flags.11?int reply_to_msg_id:flags.3?int entities:flags.7?Vector<MessageEntity> = Updates'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
