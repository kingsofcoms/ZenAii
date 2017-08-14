from ....tl.tlobject import TLObject
from ....utils import get_input_channel


class DeleteChannelRequest(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    channels.deleteChannel#c0111fe3 channel:InputChannel = Updates"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0xc0111fe3
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x8af52aac

    def __init__(self, channel):
        """
        :param channel: Telegram type: "InputChannel".

        :returns Updates: Instance of either UpdatesTooLong, UpdateShortMessage, UpdateShortChatMessage, UpdateShort, UpdatesCombined, UpdatesTg, UpdateShortSentMessage.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.channel = get_input_channel(channel)

    def to_dict(self):
        return {
            'channel': None if self.channel is None else self.channel.to_dict(),
        }

    def on_send(self, writer):
        writer.write_int(DeleteChannelRequest.constructor_id, signed=False)
        self.channel.on_send(writer)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return DeleteChannelRequest(None)

    def on_response(self, reader):
        self.result = reader.tgread_object()

    def __repr__(self):
        return 'channels.deleteChannel#c0111fe3 channel:InputChannel = Updates'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
