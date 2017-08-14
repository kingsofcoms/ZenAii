from ....tl.tlobject import TLObject


class ReceivedCallRequest(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    phone.receivedCall#17d54f61 peer:InputPhoneCall = Bool"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x17d54f61
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0xf5b399ac

    def __init__(self, peer):
        """
        :param peer: Telegram type: "InputPhoneCall".

        :returns Bool: This type has no constructors.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.peer = peer

    def to_dict(self):
        return {
            'peer': None if self.peer is None else self.peer.to_dict(),
        }

    def on_send(self, writer):
        writer.write_int(ReceivedCallRequest.constructor_id, signed=False)
        self.peer.on_send(writer)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return ReceivedCallRequest(None)

    def on_response(self, reader):
        self.result = reader.tgread_object()

    def __repr__(self):
        return 'phone.receivedCall#17d54f61 peer:InputPhoneCall = Bool'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
