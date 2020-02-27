from char_data.CharIndexes import CharIndexes
from speedysvc.client_server.base_classes.ServerMethodsBase import \
    ServerMethodsBase
from speedysvc.rpc_decorators import json_method


class CharIndexServer(ServerMethodsBase):
    port = 40518
    name = 'char_idx'

    def __init__(self, logger_client, char_data=None):
        if char_data is None:
            from char_data.CharData import CharData
            char_data = CharData()

        self.char_indexes = CharIndexes(char_data=char_data)
        ServerMethodsBase.__init__(self, logger_client)

    @json_method
    def search(self, key, value, args, kw):
        return self.char_indexes.search(key, value, *args, **kw)

    @json_method
    def keys(self):
        return self.char_indexes.keys()

    @json_method
    def get_key_info(self, key):
        key_info = self.char_indexes.get_key_info(key)
        if key_info:
            return key_info.to_tuple()
        else:
            return None

    @json_method
    def values(self, key):
        return self.char_indexes.values(key)

    @json_method
    def get_value_info(self, key, value):
        value_info = self.char_indexes.get_value_info(key, value)
        if value_info:
            return value_info.to_tuple()
        else:
            return None


if __name__ == '__main__':
    from time import sleep
    server = CharIndexServer()
    while 1: sleep(10)
