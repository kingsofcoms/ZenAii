from ....tl.tlobject import TLObject


class FoundGifs(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    messages.foundGifs#450a1c0a next_offset:int results:Vector<FoundGif> = messages.FoundGifs"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x450a1c0a
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0xe799ea7

    def __init__(self, next_offset, results):
        """
        :param next_offset: Telegram type: "int".
        :param results: Telegram type: "FoundGif". Must be a list.

        Constructor for messages.FoundGifs: Instance of FoundGifs.
        """
        super().__init__()

        self.next_offset = next_offset
        self.results = results

    def to_dict(self):
        return {
            'next_offset': self.next_offset,
            'results': [] if self.results is None else [None if x is None else x.to_dict() for x in self.results],
        }

    def on_send(self, writer):
        writer.write_int(FoundGifs.constructor_id, signed=False)
        writer.write_int(self.next_offset)
        writer.write_int(0x1cb5c415, signed=False)  # Vector's constructor ID
        writer.write_int(len(self.results))
        for _x in self.results:
            _x.on_send(writer)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return FoundGifs(None, None)

    def on_response(self, reader):
        self.next_offset = reader.read_int()
        reader.read_int()  # Vector's constructor ID
        self.results = []  # Initialize an empty list
        _len = reader.read_int()
        for _ in range(_len):
            _x = reader.tgread_object()
            self.results.append(_x)

    def __repr__(self):
        return 'messages.foundGifs#450a1c0a next_offset:int results:Vector<FoundGif> = messages.FoundGifs'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
