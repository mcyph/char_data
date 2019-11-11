from char_data.CharIndexes import CharIndexes
from network_tools.mmap_sockets.MMapServer import MMapServer, json_method


class CharIndexServer(MMapServer):
    def __init__(self):
        MMapServer.__init__(self, port=40518)
        self.char_indexes = CharIndexes()

    @json_method(doc=CharIndexes.search)
    def search(self, key, value, args, kw):
        return self.char_indexes.search(key, value, *args, **kw)

    @json_method(doc=CharIndexes.keys)
    def keys(self):
        return self.char_indexes.keys()

    @json_method(doc=CharIndexes.get_value_info)
    def get_key_info(self, key):
        key_info = self.char_indexes.get_key_info(key)
        if key_info:
            return key_info.to_tuple()
        else:
            return None

    @json_method(doc=CharIndexes.values)
    def values(self, key):
        return self.char_indexes.values(key)

    @json_method(doc=CharIndexes.get_value_info)
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
