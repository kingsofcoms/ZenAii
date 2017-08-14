from ...tl.tlobject import TLObject


class InputPeerNotifySettings(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    inputPeerNotifySettings#38935eb2 flags:# show_previews:flags.0?true silent:flags.1?true mute_until:int sound:string = InputPeerNotifySettings"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x38935eb2
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x90db0b0d

    def __init__(self, mute_until, sound, show_previews=None, silent=None):
        """
        :param show_previews: Telegram type: "true".
        :param silent: Telegram type: "true".
        :param mute_until: Telegram type: "int".
        :param sound: Telegram type: "string".

        Constructor for InputPeerNotifySettings: Instance of InputPeerNotifySettings.
        """
        super().__init__()

        self.show_previews = show_previews
        self.silent = silent
        self.mute_until = mute_until
        self.sound = sound

    def to_dict(self):
        return {
            'show_previews': self.show_previews,
            'silent': self.silent,
            'mute_until': self.mute_until,
            'sound': self.sound,
        }

    def on_send(self, writer):
        writer.write_int(InputPeerNotifySettings.constructor_id, signed=False)
        # Calculate the flags. This equals to those flag arguments which are NOT None
        flags = 0
        flags |= (1 << 0) if self.show_previews else 0
        flags |= (1 << 1) if self.silent else 0
        writer.write_int(flags)

        writer.write_int(self.mute_until)
        writer.tgwrite_string(self.sound)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return InputPeerNotifySettings(None, None, None, None)

    def on_response(self, reader):
        flags = reader.read_int()

        if (flags & (1 << 0)) != 0:
            self.show_previews = True  # Arbitrary not-None value, no need to read since it is a flag

        if (flags & (1 << 1)) != 0:
            self.silent = True  # Arbitrary not-None value, no need to read since it is a flag

        self.mute_until = reader.read_int()
        self.sound = reader.tgread_string()

    def __repr__(self):
        return 'inputPeerNotifySettings#38935eb2 flags:# show_previews:flags.0?true silent:flags.1?true mute_until:int sound:string = InputPeerNotifySettings'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
