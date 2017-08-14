from ...tl.tlobject import TLObject


class PeerChannel(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    peerChannel#bddde532 channel_id:int = Peer"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0xbddde532
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x2d45687

    def __init__(self, channel_id):
        """
        :param channel_id: Telegram type: "int".

        Constructor for Peer: Instance of either PeerUser, PeerChat, PeerChannel.
        """
        super().__init__()

        self.channel_id = channel_id

    def to_dict(self):
        return {
            'channel_id': self.channel_id,
        }

    def on_send(self, writer):
        writer.write_int(PeerChannel.constructor_id, signed=False)
        writer.write_int(self.channel_id)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return PeerChannel(None)

    def on_response(self, reader):
        self.channel_id = reader.read_int()

    def __repr__(self):
        return 'peerChannel#bddde532 channel_id:int = Peer'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
