from ....tl.tlobject import TLObject
from ....utils import get_input_user


class BlockRequest(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    contacts.block#332b49fc id:InputUser = Bool"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x332b49fc
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0xf5b399ac

    def __init__(self, id):
        """
        :param id: Telegram type: "InputUser".

        :returns Bool: This type has no constructors.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.id = get_input_user(id)

    def to_dict(self):
        return {
            'id': None if self.id is None else self.id.to_dict(),
        }

    def on_send(self, writer):
        writer.write_int(BlockRequest.constructor_id, signed=False)
        self.id.on_send(writer)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return BlockRequest(None)

    def on_response(self, reader):
        self.result = reader.tgread_object()

    def __repr__(self):
        return 'contacts.block#332b49fc id:InputUser = Bool'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
