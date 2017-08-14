from ....tl.tlobject import TLObject
from ....utils import get_input_peer


class ReadHistoryRequest(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    messages.readHistory#0e306d3a peer:InputPeer max_id:int = messages.AffectedMessages"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0xe306d3a
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0xced3c06e

    def __init__(self, peer, max_id):
        """
        :param peer: Telegram type: "InputPeer".
        :param max_id: Telegram type: "int".

        :returns messages.AffectedMessages: Instance of AffectedMessages.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.peer = get_input_peer(peer)
        self.max_id = max_id

    def to_dict(self):
        return {
            'peer': None if self.peer is None else self.peer.to_dict(),
            'max_id': self.max_id,
        }

    def on_send(self, writer):
        writer.write_int(ReadHistoryRequest.constructor_id, signed=False)
        self.peer.on_send(writer)
        writer.write_int(self.max_id)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return ReadHistoryRequest(None, None)

    def on_response(self, reader):
        self.result = reader.tgread_object()

    def __repr__(self):
        return 'messages.readHistory#0e306d3a peer:InputPeer max_id:int = messages.AffectedMessages'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
