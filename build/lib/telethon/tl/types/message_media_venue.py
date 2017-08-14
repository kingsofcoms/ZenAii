from ...tl.tlobject import TLObject


class MessageMediaVenue(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    messageMediaVenue#7912b71f geo:GeoPoint title:string address:string provider:string venue_id:string = MessageMedia"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x7912b71f
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x476cbe32

    def __init__(self, geo, title, address, provider, venue_id):
        """
        :param geo: Telegram type: "GeoPoint".
        :param title: Telegram type: "string".
        :param address: Telegram type: "string".
        :param provider: Telegram type: "string".
        :param venue_id: Telegram type: "string".

        Constructor for MessageMedia: Instance of either MessageMediaEmpty, MessageMediaPhoto, MessageMediaGeo, MessageMediaContact, MessageMediaUnsupported, MessageMediaDocument, MessageMediaWebPage, MessageMediaVenue, MessageMediaGame, MessageMediaInvoice.
        """
        super().__init__()

        self.geo = geo
        self.title = title
        self.address = address
        self.provider = provider
        self.venue_id = venue_id

    def to_dict(self):
        return {
            'geo': None if self.geo is None else self.geo.to_dict(),
            'title': self.title,
            'address': self.address,
            'provider': self.provider,
            'venue_id': self.venue_id,
        }

    def on_send(self, writer):
        writer.write_int(MessageMediaVenue.constructor_id, signed=False)
        self.geo.on_send(writer)
        writer.tgwrite_string(self.title)
        writer.tgwrite_string(self.address)
        writer.tgwrite_string(self.provider)
        writer.tgwrite_string(self.venue_id)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return MessageMediaVenue(None, None, None, None, None)

    def on_response(self, reader):
        self.geo = reader.tgread_object()
        self.title = reader.tgread_string()
        self.address = reader.tgread_string()
        self.provider = reader.tgread_string()
        self.venue_id = reader.tgread_string()

    def __repr__(self):
        return 'messageMediaVenue#7912b71f geo:GeoPoint title:string address:string provider:string venue_id:string = MessageMedia'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
