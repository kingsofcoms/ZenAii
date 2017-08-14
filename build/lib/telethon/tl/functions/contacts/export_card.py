from ....tl.tlobject import TLObject


class ExportCardRequest(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    contacts.exportCard#84e53737 = Vector<int>"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x84e53737
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x5026710f

    def __init__(self):
        super().__init__()
        self.result = None
        self.content_related = True

    @staticmethod
    def to_dict():
        return {}

    def on_send(self, writer):
        writer.write_int(ExportCardRequest.constructor_id, signed=False)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return ExportCardRequest()

    def on_response(self, reader):
        reader.read_int()  # Vector id
        count = reader.read_int()
        self.result = [reader.read_int() for _ in range(count)]

    def __repr__(self):
        return 'contacts.exportCard#84e53737 = Vector<int>'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
