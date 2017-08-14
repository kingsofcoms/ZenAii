from ...tl.tlobject import TLObject


class ShippingOption(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    shippingOption#b6213cdf id:string title:string prices:Vector<LabeledPrice> = ShippingOption"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0xb6213cdf
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0xf4e94c78

    def __init__(self, id, title, prices):
        """
        :param id: Telegram type: "string".
        :param title: Telegram type: "string".
        :param prices: Telegram type: "LabeledPrice". Must be a list.

        Constructor for ShippingOption: Instance of ShippingOption.
        """
        super().__init__()

        self.id = id
        self.title = title
        self.prices = prices

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'prices': [] if self.prices is None else [None if x is None else x.to_dict() for x in self.prices],
        }

    def on_send(self, writer):
        writer.write_int(ShippingOption.constructor_id, signed=False)
        writer.tgwrite_string(self.id)
        writer.tgwrite_string(self.title)
        writer.write_int(0x1cb5c415, signed=False)  # Vector's constructor ID
        writer.write_int(len(self.prices))
        for _x in self.prices:
            _x.on_send(writer)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return ShippingOption(None, None, None)

    def on_response(self, reader):
        self.id = reader.tgread_string()
        self.title = reader.tgread_string()
        reader.read_int()  # Vector's constructor ID
        self.prices = []  # Initialize an empty list
        _len = reader.read_int()
        for _ in range(_len):
            _x = reader.tgread_object()
            self.prices.append(_x)

    def __repr__(self):
        return 'shippingOption#b6213cdf id:string title:string prices:Vector<LabeledPrice> = ShippingOption'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
