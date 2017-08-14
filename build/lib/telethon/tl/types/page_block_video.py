from ...tl.tlobject import TLObject


class PageBlockVideo(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    pageBlockVideo#d9d71866 flags:# autoplay:flags.0?true loop:flags.1?true video_id:long caption:RichText = PageBlock"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0xd9d71866
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x1aca5644

    def __init__(self, video_id, caption, autoplay=None, loop=None):
        """
        :param autoplay: Telegram type: "true".
        :param loop: Telegram type: "true".
        :param video_id: Telegram type: "long".
        :param caption: Telegram type: "RichText".

        Constructor for PageBlock: Instance of either PageBlockUnsupported, PageBlockTitle, PageBlockSubtitle, PageBlockAuthorDate, PageBlockHeader, PageBlockSubheader, PageBlockParagraph, PageBlockPreformatted, PageBlockFooter, PageBlockDivider, PageBlockAnchor, PageBlockList, PageBlockBlockquote, PageBlockPullquote, PageBlockPhoto, PageBlockVideo, PageBlockCover, PageBlockEmbed, PageBlockEmbedPost, PageBlockCollage, PageBlockSlideshow, PageBlockChannel, PageBlockAudio.
        """
        super().__init__()

        self.autoplay = autoplay
        self.loop = loop
        self.video_id = video_id
        self.caption = caption

    def to_dict(self):
        return {
            'autoplay': self.autoplay,
            'loop': self.loop,
            'video_id': self.video_id,
            'caption': None if self.caption is None else self.caption.to_dict(),
        }

    def on_send(self, writer):
        writer.write_int(PageBlockVideo.constructor_id, signed=False)
        # Calculate the flags. This equals to those flag arguments which are NOT None
        flags = 0
        flags |= (1 << 0) if self.autoplay else 0
        flags |= (1 << 1) if self.loop else 0
        writer.write_int(flags)

        writer.write_long(self.video_id)
        self.caption.on_send(writer)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return PageBlockVideo(None, None, None, None)

    def on_response(self, reader):
        flags = reader.read_int()

        if (flags & (1 << 0)) != 0:
            self.autoplay = True  # Arbitrary not-None value, no need to read since it is a flag

        if (flags & (1 << 1)) != 0:
            self.loop = True  # Arbitrary not-None value, no need to read since it is a flag

        self.video_id = reader.read_long()
        self.caption = reader.tgread_object()

    def __repr__(self):
        return 'pageBlockVideo#d9d71866 flags:# autoplay:flags.0?true loop:flags.1?true video_id:long caption:RichText = PageBlock'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
