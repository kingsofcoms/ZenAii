from ...tl.tlobject import TLObject


class ServerDHInnerData(TLObject):
    """Class generated by TLObjects' generator. All changes will be ERASED. TL definition below.
    server_DH_inner_data#b5890dba nonce:int128 server_nonce:int128 g:int dh_prime:string g_a:string server_time:int = Server_DH_inner_data"""

    # Telegram's constructor (U)ID for this class
    constructor_id = 0xb5890dba
    # Also the ID of its resulting type for fast checks
    subclass_of_id = 0xc69a67bc

    def __init__(self, nonce, server_nonce, g, dh_prime, g_a, server_time):
        """
        :param nonce: Telegram type: "int128".
        :param server_nonce: Telegram type: "int128".
        :param g: Telegram type: "int".
        :param dh_prime: Telegram type: "string".
        :param g_a: Telegram type: "string".
        :param server_time: Telegram type: "int".

        Constructor for Server_DH_inner_data: Instance of ServerDHInnerData.
        """
        super().__init__()

        self.nonce = nonce
        self.server_nonce = server_nonce
        self.g = g
        self.dh_prime = dh_prime
        self.g_a = g_a
        self.server_time = server_time

    def to_dict(self):
        return {
            'nonce': self.nonce,
            'server_nonce': self.server_nonce,
            'g': self.g,
            'dh_prime': self.dh_prime,
            'g_a': self.g_a,
            'server_time': self.server_time,
        }

    def on_send(self, writer):
        writer.write_int(ServerDHInnerData.constructor_id, signed=False)
        writer.write_large_int(self.nonce, bits=128)
        writer.write_large_int(self.server_nonce, bits=128)
        writer.write_int(self.g)
        writer.tgwrite_string(self.dh_prime)
        writer.tgwrite_string(self.g_a)
        writer.write_int(self.server_time)

    @staticmethod
    def empty():
        """Returns an "empty" instance (attributes=None)"""
        return ServerDHInnerData(None, None, None, None, None, None)

    def on_response(self, reader):
        self.nonce = reader.read_large_int(bits=128)
        self.server_nonce = reader.read_large_int(bits=128)
        self.g = reader.read_int()
        self.dh_prime = reader.tgread_string()
        self.g_a = reader.tgread_string()
        self.server_time = reader.read_int()

    def __repr__(self):
        return 'server_DH_inner_data#b5890dba nonce:int128 server_nonce:int128 g:int dh_prime:string g_a:string server_time:int = Server_DH_inner_data'

    def __str__(self):
        return TLObject.pretty_format(self)

    def stringify(self):
        return TLObject.pretty_format(self, indent=0)
