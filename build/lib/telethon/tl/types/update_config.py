from ...tl.tlobject import TLObject


class UpdateConfig(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    updateConfig#a229dd06 = Update"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0xa229dd06
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x9f89304e

    def __init__(self):
        super().__init__()

    @staticmethod
    def to_dict():
        return {}

    def on_send(self, writer):
        writer.write_int(UpdateConfig.constructor_id, signed=False)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return UpdateConfig()

    def on_response(self, reader):
        pass

    def __repr__(self):
        return 'updateConfig#a229dd06 = Update'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
