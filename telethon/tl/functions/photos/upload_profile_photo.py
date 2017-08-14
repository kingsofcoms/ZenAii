from ....tl.tlobject import TLObject


class UploadProfilePhotoRequest(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    photos.uploadProfilePhoto#4f32c098 file:InputFile = photos.Photo"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x4f32c098
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0xc292bd24

    def __init__(self, file):
        """
        :param file: Telegram type: "InputFile".

        :returns photos.Photo: Instance of Photo.
        """
        super().__init__()
        self.result = None
        self.content_related = True

        self.file = file

    def to_dict(self):
        return {
            'file': None if self.file is None else self.file.to_dict(),
        }

    def on_send(self, writer):
        writer.write_int(UploadProfilePhotoRequest.constructor_id, signed=False)
        self.file.on_send(writer)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return UploadProfilePhotoRequest(None)

    def on_response(self, reader):
        self.result = reader.tgread_object()

    def __repr__(self):
        return 'photos.uploadProfilePhoto#4f32c098 file:InputFile = photos.Photo'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
