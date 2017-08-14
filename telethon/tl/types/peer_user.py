from ...tl.tlobject import TLObject


class PeerUser(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    peerUser#9db1bc6d user_id:int = Peer"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x9db1bc6d
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x2d45687

    def __init__(self, user_id):
        """
        :param user_id: Telegram type: "int".

        Constructor for Peer: Instance of either PeerUser, PeerChat, PeerChannel.
        """
        super().__init__()

        self.user_id = user_id

    def to_dict(self):
        return {
            'user_id': self.user_id,
        }

    def on_send(self, writer):
        writer.write_int(PeerUser.constructor_id, signed=False)
        writer.write_int(self.user_id)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return PeerUser(None)

    def on_response(self, reader):
        self.user_id = reader.read_int()

    def __repr__(self):
        return 'peerUser#9db1bc6d user_id:int = Peer'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
