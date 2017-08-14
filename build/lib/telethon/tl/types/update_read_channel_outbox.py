from ...tl.tlobject import TLObject


class UpdateReadChannelOutbox(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    updateReadChannelOutbox#25d6c9c7 channel_id:int max_id:int = Update"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x25d6c9c7
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x9f89304e

    def __init__(self, channel_id, max_id):
        """
        :param channel_id: Telegram type: "int".
        :param max_id: Telegram type: "int".

        Constructor for Update: Instance of either UpdateNewMessage, UpdateMessageID, UpdateDeleteMessages, UpdateUserTyping, UpdateChatUserTyping, UpdateChatParticipants, UpdateUserStatus, UpdateUserName, UpdateUserPhoto, UpdateContactRegistered, UpdateContactLink, UpdateNewEncryptedMessage, UpdateEncryptedChatTyping, UpdateEncryption, UpdateEncryptedMessagesRead, UpdateChatParticipantAdd, UpdateChatParticipantDelete, UpdateDcOptions, UpdateUserBlocked, UpdateNotifySettings, UpdateServiceNotification, UpdatePrivacy, UpdateUserPhone, UpdateReadHistoryInbox, UpdateReadHistoryOutbox, UpdateWebPage, UpdateReadMessagesContents, UpdateChannelTooLong, UpdateChannel, UpdateNewChannelMessage, UpdateReadChannelInbox, UpdateDeleteChannelMessages, UpdateChannelMessageViews, UpdateChatAdmins, UpdateChatParticipantAdmin, UpdateNewStickerSet, UpdateStickerSetsOrder, UpdateStickerSets, UpdateSavedGifs, UpdateBotInlineQuery, UpdateBotInlineSend, UpdateEditChannelMessage, UpdateChannelPinnedMessage, UpdateBotCallbackQuery, UpdateEditMessage, UpdateInlineBotCallbackQuery, UpdateReadChannelOutbox, UpdateDraftMessage, UpdateReadFeaturedStickers, UpdateRecentStickers, UpdateConfig, UpdatePtsChanged, UpdateChannelWebPage, UpdateDialogPinned, UpdatePinnedDialogs, UpdateBotWebhookJSON, UpdateBotWebhookJSONQuery, UpdateBotShippingQuery, UpdateBotPrecheckoutQuery, UpdatePhoneCall, UpdateLangPackTooLong, UpdateLangPack.
        """
        super().__init__()

        self.channel_id = channel_id
        self.max_id = max_id

    def to_dict(self):
        return {
            'channel_id': self.channel_id,
            'max_id': self.max_id,
        }

    def on_send(self, writer):
        writer.write_int(UpdateReadChannelOutbox.constructor_id, signed=False)
        writer.write_int(self.channel_id)
        writer.write_int(self.max_id)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return UpdateReadChannelOutbox(None, None)

    def on_response(self, reader):
        self.channel_id = reader.read_int()
        self.max_id = reader.read_int()

    def __repr__(self):
        return 'updateReadChannelOutbox#25d6c9c7 channel_id:int max_id:int = Update'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
