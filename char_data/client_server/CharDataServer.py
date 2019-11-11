from char_data.CharData import CharData
from network_tools.mmap_sockets.MMapServer import MMapServer, json_method


class CharDataServer(MMapServer):
    def __init__(self, char_data=None):
        if char_data is None:
            char_data = CharData()
        self.char_data = char_data

        MMapServer.__init__(self, port=40517)

    @json_method(doc=CharData.keys)
    def keys(self, data_source=None):
        return self.char_data.keys(
            data_source=data_source
        )

    @json_method(doc=CharData.get_key_info)
    def get_key_info(self, key):
        key_info = self.char_data.get_key_info(key)
        if key_info:
            return key_info.to_tuple()
        else:
            return None

    @json_method(doc=CharData.raw_data)
    def raw_data(self, key, ord_):
        return self.char_data.raw_data(key, ord_)

    @json_method(doc=CharData.formatted)
    def formatted(self, key, ord_):
        return self.char_data.formatted(key, ord_)

    @json_method(doc=CharData.html_formatted)
    def html_formatted(self, key, ord_):
        return self.char_data.html_formatted(key, ord_)


if __name__ == '__main__':
    from time import sleep
    server = CharDataServer()
    while 1: sleep(10)
