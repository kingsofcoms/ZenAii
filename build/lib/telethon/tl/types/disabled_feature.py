from ...tl.tlobject import TLObject


class DisabledFeature(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    disabledFeature#ae636f24 feature:string description:string = DisabledFeature"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0xae636f24
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0xcd266f94

    def __init__(self, feature, description):
        """
        :param feature: Telegram type: "string".
        :param description: Telegram type: "string".

        Constructor for DisabledFeature: Instance of DisabledFeature.
        """
        super().__init__()

        self.feature = feature
        self.description = description

    def to_dict(self):
        return {
            'feature': self.feature,
            'description': self.description,
        }

    def on_send(self, writer):
        writer.write_int(DisabledFeature.constructor_id, signed=False)
        writer.tgwrite_string(self.feature)
        writer.tgwrite_string(self.description)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return DisabledFeature(None, None)

    def on_response(self, reader):
        self.feature = reader.tgread_string()
        self.description = reader.tgread_string()

    def __repr__(self):
        return 'disabledFeature#ae636f24 feature:string description:string = DisabledFeature'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
