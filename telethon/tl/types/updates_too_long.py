from ...tl.tlobject import TLObject


class UpdatesTooLong(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    updatesTooLong#e317af7e = Updates"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0xe317af7e
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x8af52aac

    def __init__(self):
        super().__init__()

    @staticmethod
    def to_dict():
        return {}

    def on_send(self, writer):
        writer.write_int(UpdatesTooLong.constructor_id, signed=False)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return UpdatesTooLong()

    def on_response(self, reader):
        pass

    def __repr__(self):
        return 'updatesTooLong#e317af7e = Updates'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
