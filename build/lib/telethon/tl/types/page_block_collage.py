from ...tl.tlobject import TLObject


class PageBlockCollage(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    pageBlockCollage#08b31c4f items:Vector<PageBlock> caption:RichText = PageBlock"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x8b31c4f
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x1aca5644

    def __init__(self, items, caption):
        """
        :param items: Telegram type: "PageBlock". Must be a list.
        :param caption: Telegram type: "RichText".

        Constructor for PageBlock: Instance of either PageBlockUnsupported, PageBlockTitle, PageBlockSubtitle, PageBlockAuthorDate, PageBlockHeader, PageBlockSubheader, PageBlockParagraph, PageBlockPreformatted, PageBlockFooter, PageBlockDivider, PageBlockAnchor, PageBlockList, PageBlockBlockquote, PageBlockPullquote, PageBlockPhoto, PageBlockVideo, PageBlockCover, PageBlockEmbed, PageBlockEmbedPost, PageBlockCollage, PageBlockSlideshow, PageBlockChannel, PageBlockAudio.
        """
        super().__init__()

        self.items = items
        self.caption = caption

    def to_dict(self):
        return {
            'items': [] if self.items is None else [None if x is None else x.to_dict() for x in self.items],
            'caption': None if self.caption is None else self.caption.to_dict(),
        }

    def on_send(self, writer):
        writer.write_int(PageBlockCollage.constructor_id, signed=False)
        writer.write_int(0x1cb5c415, signed=False)  # Vector's constructor ID
        writer.write_int(len(self.items))
        for _x in self.items:
            _x.on_send(writer)

        self.caption.on_send(writer)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return PageBlockCollage(None, None)

    def on_response(self, reader):
        reader.read_int()  # Vector's constructor ID
        self.items = []  # Initialize an empty list
        _len = reader.read_int()
        for _ in range(_len):
            _x = reader.tgread_object()
            self.items.append(_x)

        self.caption = reader.tgread_object()

    def __repr__(self):
        return 'pageBlockCollage#08b31c4f items:Vector<PageBlock> caption:RichText = PageBlock'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
