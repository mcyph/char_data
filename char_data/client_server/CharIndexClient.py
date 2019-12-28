from char_data.toolkit.patterns.Singleton import Singleton
from char_data.toolkit.documentation.copydoc import copydoc
from shmrpc.rpc.base_classes.ClientMethodsBase import ClientMethodsBase
from shmrpc.rpc.shared_memory.SHMClient import SHMClient

from char_data.data_info_types.CharIndexKeyInfo import CharIndexKeyInfo
from char_data.data_info_types.CharIndexValueInfo import CharIndexValueInfo
from char_data.abstract_base_classes.CharIndexesBase import CharIndexesBase
from char_data.client_server.CharIndexServer import CharIndexServer as srv


class CharIndexClient(CharIndexesBase,
                      Singleton,
                      ClientMethodsBase
                      ):

    def __init__(self,
                 char_data=None,
                 client_provider=None): # HACK! ============================================================
        """
        A mirror of the `CharIndexes` class, but allowing separation of
        the data into a client-server arrangement, saving memory in
        multi-process setups.
        """
        if client_provider is None:
            client_provider = SHMClient(srv)
        ClientMethodsBase.__init__(self, client_provider)

    @copydoc(CharIndexesBase.search)
    def search(self, key, value, *args, **kw):
        return self.send(srv.search, [key, value, args, kw])

    keys = srv.keys.as_rpc()

    @copydoc(CharIndexesBase.get_key_info)
    def get_key_info(self, key):
        key_info = self.send(srv.get_key_info, [key])
        if key_info:
            return CharIndexKeyInfo.from_tuple(*key_info)
        else:
            return None

    values = srv.values.as_rpc()

    @copydoc(CharIndexesBase.get_value_info)
    def get_value_info(self, key, value):
        value_info = self.send(srv.get_value_info, [
            key, value
        ])
        if value_info:
            return CharIndexValueInfo.from_tuple(*value_info)
        else:
            return None


if __name__ == '__main__':
    client = CharIndexClient()
    print(client.search('cldr_alphabets.alphabets', 'bn'))
    print(client.keys())
    print(client.get_key_info('cldr_alphabets.alphabets'))
    print(client.values('cldr_alphabets.alphabets'))
    print(client.get_value_info('cldr_alphabets.alphabets', 'bn'))
