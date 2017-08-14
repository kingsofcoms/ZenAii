from ...tl.tlobject import TLObject


class UserStatusOnline(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    userStatusOnline#edb93949 expires:int = UserStatus"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0xedb93949
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x5b0b743e

    def __init__(self, expires):
        """
        :param expires: Telegram type: "date".

        Constructor for UserStatus: Instance of either UserStatusEmpty, UserStatusOnline, UserStatusOffline, UserStatusRecently, UserStatusLastWeek, UserStatusLastMonth.
        """
        super().__init__()

        self.expires = expires

    def to_dict(self):
        return {
            'expires': self.expires,
        }

    def on_send(self, writer):
        writer.write_int(UserStatusOnline.constructor_id, signed=False)
        writer.tgwrite_date(self.expires)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return UserStatusOnline(None)

    def on_response(self, reader):
        self.expires = reader.tgread_date()

    def __repr__(self):
        return 'userStatusOnline#edb93949 expires:int = UserStatus'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
