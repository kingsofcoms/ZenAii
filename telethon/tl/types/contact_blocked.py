from ...tl.tlobject import TLObject


class ContactBlocked(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    contactBlocked#561bc879 user_id:int date:int = ContactBlocked"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x561bc879
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0xb12d7ac6

    def __init__(self, user_id, date):
        """
        :param user_id: Telegram type: "int".
        :param date: Telegram type: "date".

        Constructor for ContactBlocked: Instance of ContactBlocked.
        """
        super().__init__()

        self.user_id = user_id
        self.date = date

    def to_dict(self):
        return {
            'user_id': self.user_id,
            'date': self.date,
        }

    def on_send(self, writer):
        writer.write_int(ContactBlocked.constructor_id, signed=False)
        writer.write_int(self.user_id)
        writer.tgwrite_date(self.date)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return ContactBlocked(None, None)

    def on_response(self, reader):
        self.user_id = reader.read_int()
        self.date = reader.tgread_date()

    def __repr__(self):
        return 'contactBlocked#561bc879 user_id:int date:int = ContactBlocked'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
