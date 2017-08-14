from ...tl.tlobject import TLObject


class InputPhotoEmpty(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    inputPhotoEmpty#1cd7bf0d = InputPhoto"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x1cd7bf0d
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x846363e0

    def __init__(self):
        super().__init__()

    @staticmethod
    def to_dict():
        return {}

    def on_send(self, writer):
        writer.write_int(InputPhotoEmpty.constructor_id, signed=False)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return InputPhotoEmpty()

    def on_response(self, reader):
        pass

    def __repr__(self):
        return 'inputPhotoEmpty#1cd7bf0d = InputPhoto'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
