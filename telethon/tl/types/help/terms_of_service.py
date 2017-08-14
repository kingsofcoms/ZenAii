from ....tl.tlobject import TLObject


class TermsOfService(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    help.termsOfService#f1ee3e90 text:string = help.TermsOfService"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0xf1ee3e90
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x20ee8312

    def __init__(self, text):
        """
        :param text: Telegram type: "string".

        Constructor for help.TermsOfService: Instance of TermsOfService.
        """
        super().__init__()

        self.text = text

    def to_dict(self):
        return {
            'text': self.text,
        }

    def on_send(self, writer):
        writer.write_int(TermsOfService.constructor_id, signed=False)
        writer.tgwrite_string(self.text)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return TermsOfService(None)

    def on_response(self, reader):
        self.text = reader.tgread_string()

    def __repr__(self):
        return 'help.termsOfService#f1ee3e90 text:string = help.TermsOfService'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
