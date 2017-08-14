from ...tl.tlobject import TLObject


class ChannelParticipantsBots(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    channelParticipantsBots#b0d1865b = ChannelParticipantsFilter"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0xb0d1865b
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0xbf4e2753

    def __init__(self):
        super().__init__()

    @staticmethod
    def to_dict():
        return {}

    def on_send(self, writer):
        writer.write_int(ChannelParticipantsBots.constructor_id, signed=False)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return ChannelParticipantsBots()

    def on_response(self, reader):
        pass

    def __repr__(self):
        return 'channelParticipantsBots#b0d1865b = ChannelParticipantsFilter'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
