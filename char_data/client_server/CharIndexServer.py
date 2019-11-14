from char_data.CharIndexes import CharIndexes
from network_tools.posix_shm_sockets.SHMServer import SHMServer, json_method


class CharIndexServer(SHMServer):
    def __init__(self, char_data):
        SHMServer.__init__(self, DCmds={
            'search': self.search,
            'keys': self.keys,
            'get_key_info': self.get_key_info,
            'values': self.values,
            'get_value_info': self.get_value_info
        }, port=40518)
        self.char_indexes = CharIndexes(char_data=char_data)

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
