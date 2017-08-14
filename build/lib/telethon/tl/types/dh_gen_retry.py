from ...tl.tlobject import TLObject


class DhGenRetry(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    dh_gen_retry#46dc1fb9 nonce:int128 server_nonce:int128 new_nonce_hash2:int128 = Set_client_DH_params_answer"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0x46dc1fb9
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0x55dd6cdb

    def __init__(self, nonce, server_nonce, new_nonce_hash2):
        """
        :param nonce: Telegram type: "int128".
        :param server_nonce: Telegram type: "int128".
        :param new_nonce_hash2: Telegram type: "int128".

        Constructor for Set_client_DH_params_answer: Instance of either DhGenOk, DhGenRetry, DhGenFail.
        """
        super().__init__()

        self.nonce = nonce
        self.server_nonce = server_nonce
        self.new_nonce_hash2 = new_nonce_hash2

    def to_dict(self):
        return {
            'nonce': self.nonce,
            'server_nonce': self.server_nonce,
            'new_nonce_hash2': self.new_nonce_hash2,
        }

    def on_send(self, writer):
        writer.write_int(DhGenRetry.constructor_id, signed=False)
        writer.write_large_int(self.nonce, bits=128)
        writer.write_large_int(self.server_nonce, bits=128)
        writer.write_large_int(self.new_nonce_hash2, bits=128)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return DhGenRetry(None, None, None)

    def on_response(self, reader):
        self.nonce = reader.read_large_int(bits=128)
        self.server_nonce = reader.read_large_int(bits=128)
        self.new_nonce_hash2 = reader.read_large_int(bits=128)

    def __repr__(self):
        return 'dh_gen_retry#46dc1fb9 nonce:int128 server_nonce:int128 new_nonce_hash2:int128 = Set_client_DH_params_answer'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
