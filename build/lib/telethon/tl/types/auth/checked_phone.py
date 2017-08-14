from ....tl.tlobject import TLObject


class CheckedPhone(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    auth.checkedPhone#811ea28e phone_registered:Bool = auth.CheckedPhone"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x811ea28e
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x99a3d765

    def __init__(self, phone_registered):
        """
        :param phone_registered: Telegram type: "Bool".

        Constructor for auth.CheckedPhone: Instance of CheckedPhone.
        """
        super().__init__()

        self.phone_registered = phone_registered

    def to_dict(self):
        return {
            'phone_registered': self.phone_registered,
        }

    def on_send(self, writer):
        writer.write_int(CheckedPhone.constructor_id, signed=False)
        writer.tgwrite_bool(self.phone_registered)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return CheckedPhone(None)

    def on_response(self, reader):
        self.phone_registered = reader.tgread_bool()

    def __repr__(self):
        return 'auth.checkedPhone#811ea28e phone_registered:Bool = auth.CheckedPhone'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
