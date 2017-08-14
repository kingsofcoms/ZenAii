from ....tl.tlobject import TLObject


class SaveAppLogRequest(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    help.saveAppLog#6f02f748 events:Vector<InputAppEvent> = Bool"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x6f02f748
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0xf5b399ac

    def __init__(self, events):
        """
        :param events: Telegram type: "InputAppEvent". Must be a list.

        :returns Bool: This type has no constructors.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.events = events

    def to_dict(self):
        return {
            'events': [] if self.events is None else [None if x is None else x.to_dict() for x in self.events],
        }

    def on_send(self, writer):
        writer.write_int(SaveAppLogRequest.constructor_id, signed=False)
        writer.write_int(0x1cb5c415, signed=False)  # Vector's constructor ID
        writer.write_int(len(self.events))
        for _x in self.events:
            _x.on_send(writer)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return SaveAppLogRequest(None)

    def on_response(self, reader):
        self.result = reader.tgread_object()

    def __repr__(self):
        return 'help.saveAppLog#6f02f748 events:Vector<InputAppEvent> = Bool'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
