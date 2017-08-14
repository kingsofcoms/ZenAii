from ....tl.tlobject import TLObject
from ....utils import get_input_user, get_input_peer


class GetInlineBotResultsRequest(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    messages.getInlineBotResults#514e999d flags:# bot:InputUser peer:InputPeer geo_point:flags.0?InputGeoPoint query:string offset:string = messages.BotResults"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x514e999d
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x3ed4d9c9

    def __init__(self, bot, peer, query, offset, geo_point=None):
        """
        :param bot: Telegram type: "InputUser".
        :param peer: Telegram type: "InputPeer".
        :param geo_point: Telegram type: "InputGeoPoint".
        :param query: Telegram type: "string".
        :param offset: Telegram type: "string".

        :returns messages.BotResults: Instance of BotResults.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.bot = get_input_user(bot)
        self.peer = get_input_peer(peer)
        self.geo_point = geo_point
        self.query = query
        self.offset = offset

    def to_dict(self):
        return {
            'bot': None if self.bot is None else self.bot.to_dict(),
            'peer': None if self.peer is None else self.peer.to_dict(),
            'geo_point': None if self.geo_point is None else self.geo_point.to_dict(),
            'query': self.query,
            'offset': self.offset,
        }

    def on_send(self, writer):
        writer.write_int(GetInlineBotResultsRequest.constructor_id, signed=False)
        # Calculate the flags. This equals to those flag arguments which are NOT None
        flags = 0
        flags |= (1 << 0) if self.geo_point else 0
        writer.write_int(flags)

        self.bot.on_send(writer)
        self.peer.on_send(writer)
        if self.geo_point:
            self.geo_point.on_send(writer)

        writer.tgwrite_string(self.query)
        writer.tgwrite_string(self.offset)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return GetInlineBotResultsRequest(None, None, None, None, None)

    def on_response(self, reader):
        self.result = reader.tgread_object()

    def __repr__(self):
        return 'messages.getInlineBotResults#514e999d flags:# bot:InputUser peer:InputPeer geo_point:flags.0?InputGeoPoint query:string offset:string = messages.BotResults'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
