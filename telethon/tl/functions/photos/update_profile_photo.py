from ....tl.tlobject import TLObject


class UpdateProfilePhotoRequest(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    photos.updateProfilePhoto#f0bb5152 id:InputPhoto = UserProfilePhoto"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0xf0bb5152
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0xc6338f7d

    def __init__(self, id):
        """
        :param id: Telegram type: "InputPhoto".

        :returns UserProfilePhoto: Instance of either UserProfilePhotoEmpty, UserProfilePhoto.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.id = id

    def to_dict(self):
        return {
            'id': None if self.id is None else self.id.to_dict(),
        }

    def on_send(self, writer):
        writer.write_int(UpdateProfilePhotoRequest.constructor_id, signed=False)
        self.id.on_send(writer)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return UpdateProfilePhotoRequest(None)

    def on_response(self, reader):
        self.result = reader.tgread_object()

    def __repr__(self):
        return 'photos.updateProfilePhoto#f0bb5152 id:InputPhoto = UserProfilePhoto'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
