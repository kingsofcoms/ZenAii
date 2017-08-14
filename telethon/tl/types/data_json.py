from ...tl.tlobject import TLObject


class DataJSON(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    dataJSON#7d748d04 data:string = DataJSON"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x7d748d04
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0xad0352e8

    def __init__(self, data):
        """
        :param data: Telegram type: "string".

        Constructor for DataJSON: Instance of DataJSON.
        """
        super().__init__()

        self.data = data

    def to_dict(self):
        return {
            'data': self.data,
        }

    def on_send(self, writer):
        writer.write_int(DataJSON.constructor_id, signed=False)
        writer.tgwrite_string(self.data)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return DataJSON(None)

    def on_response(self, reader):
        self.data = reader.tgread_string()

    def __repr__(self):
        return 'dataJSON#7d748d04 data:string = DataJSON'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
