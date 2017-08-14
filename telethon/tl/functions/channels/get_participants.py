from ....tl.tlobject import TLObject
from ....utils import get_input_channel


class GetParticipantsRequest(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    channels.getParticipants#24d98f92 channel:InputChannel filter:ChannelParticipantsFilter offset:int limit:int = channels.ChannelParticipants"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x24d98f92
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0xe60a6e64

    def __init__(self, channel, filter, offset, limit):
        """
        :param channel: Telegram type: "InputChannel".
        :param filter: Telegram type: "ChannelParticipantsFilter".
        :param offset: Telegram type: "int".
        :param limit: Telegram type: "int".

        :returns channels.ChannelParticipants: Instance of ChannelParticipants.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.channel = get_input_channel(channel)
        self.filter = filter
        self.offset = offset
        self.limit = limit

    def to_dict(self):
        return {
            'channel': None if self.channel is None else self.channel.to_dict(),
            'filter': None if self.filter is None else self.filter.to_dict(),
            'offset': self.offset,
            'limit': self.limit,
        }

    def on_send(self, writer):
        writer.write_int(GetParticipantsRequest.constructor_id, signed=False)
        self.channel.on_send(writer)
        self.filter.on_send(writer)
        writer.write_int(self.offset)
        writer.write_int(self.limit)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return GetParticipantsRequest(None, None, None, None)

    def on_response(self, reader):
        self.result = reader.tgread_object()

    def __repr__(self):
        return 'channels.getParticipants#24d98f92 channel:InputChannel filter:ChannelParticipantsFilter offset:int limit:int = channels.ChannelParticipants'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
