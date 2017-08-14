from ...tl.tlobject import TLObject


class InputBotInlineResultDocument(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    inputBotInlineResultDocument#fff8fdc4 flags:# id:string type:string title:flags.1?string description:flags.2?string document:InputDocument send_message:InputBotInlineMessage = InputBotInlineResult"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0xfff8fdc4
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x80a4a3de

    def __init__(self, id, type, document, send_message, title=None, description=None):
        """
        :param id: Telegram type: "string".
        :param type: Telegram type: "string".
        :param title: Telegram type: "string".
        :param description: Telegram type: "string".
        :param document: Telegram type: "InputDocument".
        :param send_message: Telegram type: "InputBotInlineMessage".

        Constructor for InputBotInlineResult: Instance of either InputBotInlineResult, InputBotInlineResultPhoto, InputBotInlineResultDocument, InputBotInlineResultGame.
        """
        super().__init__()

        self.id = id
        self.type = type
        self.title = title
        self.description = description
        self.document = document
        self.send_message = send_message

    def to_dict(self):
        return {
            'id': self.id,
            'type': self.type,
            'title': self.title,
            'description': self.description,
            'document': None if self.document is None else self.document.to_dict(),
            'send_message': None if self.send_message is None else self.send_message.to_dict(),
        }

    def on_send(self, writer):
        writer.write_int(InputBotInlineResultDocument.constructor_id, signed=False)
        # Calculate the flags. This equals to those flag arguments which are NOT None
        flags = 0
        flags |= (1 << 1) if self.title else 0
        flags |= (1 << 2) if self.description else 0
        writer.write_int(flags)

        writer.tgwrite_string(self.id)
        writer.tgwrite_string(self.type)
        if self.title:
            writer.tgwrite_string(self.title)

        if self.description:
            writer.tgwrite_string(self.description)

        self.document.on_send(writer)
        self.send_message.on_send(writer)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return InputBotInlineResultDocument(None, None, None, None, None, None)

    def on_response(self, reader):
        flags = reader.read_int()

        self.id = reader.tgread_string()
        self.type = reader.tgread_string()
        if (flags & (1 << 1)) != 0:
            self.title = reader.tgread_string()

        if (flags & (1 << 2)) != 0:
            self.description = reader.tgread_string()

        self.document = reader.tgread_object()
        self.send_message = reader.tgread_object()

    def __repr__(self):
        return 'inputBotInlineResultDocument#fff8fdc4 flags:# id:string type:string title:flags.1?string description:flags.2?string document:InputDocument send_message:InputBotInlineMessage = InputBotInlineResult'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
