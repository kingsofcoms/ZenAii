from ...tl.tlobject import TLObject


class InputPeerChat(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    inputPeerChat#179be863 chat_id:int = InputPeer"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x179be863
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0xc91c90b6

    def __init__(self, chat_id):
        """
        :param chat_id: Telegram type: "int".

        Constructor for InputPeer: Instance of either InputPeerEmpty, InputPeerSelf, InputPeerChat, InputPeerUser, InputPeerChannel.
        """
        super().__init__()

        self.chat_id = chat_id

    def to_dict(self):
        return {
            'chat_id': self.chat_id,
        }

    def on_send(self, writer):
        writer.write_int(InputPeerChat.constructor_id, signed=False)
        writer.write_int(self.chat_id)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return InputPeerChat(None)

    def on_response(self, reader):
        self.chat_id = reader.read_int()

    def __repr__(self):
        return 'inputPeerChat#179be863 chat_id:int = InputPeer'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
