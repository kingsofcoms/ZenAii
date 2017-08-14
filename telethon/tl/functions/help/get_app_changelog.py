from ....tl.tlobject import TLObject


class GetAppChangelogRequest(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    help.getAppChangelog#9010ef6f prev_app_version:string = Updates"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x9010ef6f
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x8af52aac

    def __init__(self, prev_app_version):
        """
        :param prev_app_version: Telegram type: "string".

        :returns Updates: Instance of either UpdatesTooLong, UpdateShortMessage, UpdateShortChatMessage, UpdateShort, UpdatesCombined, UpdatesTg, UpdateShortSentMessage.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.prev_app_version = prev_app_version

    def to_dict(self):
        return {
            'prev_app_version': self.prev_app_version,
        }

    def on_send(self, writer):
        writer.write_int(GetAppChangelogRequest.constructor_id, signed=False)
        writer.tgwrite_string(self.prev_app_version)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return GetAppChangelogRequest(None)

    def on_response(self, reader):
        self.result = reader.tgread_object()

    def __repr__(self):
        return 'help.getAppChangelog#9010ef6f prev_app_version:string = Updates'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
