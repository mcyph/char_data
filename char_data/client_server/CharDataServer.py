from char_data.CharData import char_data
from network_tools.mmap_sockets.MMapServer import MMapServer, json_method


class CharDataServer(MMapServer):
    def __init__(self):
        MMapServer.__init__(self, DCmds={
            'keys': self.keys,
            'get_key_info': self.get_key_info,
            'raw_data': self.raw_data,
            'formatted': self.formatted,
            'html_formatted': self.html_formatted
        }, port=40517)

    @json_method
    def keys(self, data_source=None):
        return char_data.keys(
            data_source=data_source
        )

    @json_method
    def get_key_info(self, key):
        key_info = char_data.get_key_info(key)
        if key_info:
            return key_info.to_tuple()
        else:
            return None

    @json_method
    def raw_data(self, key, ord_):
        return char_data.raw_data(key, ord_)

    @json_method
    def formatted(self, key, ord_):
        return char_data.formatted(key, ord_)

    @json_method
    def html_formatted(self, key, ord_):
        return char_data.html_formatted(key, ord_)


if __name__ == '__main__':
    from time import sleep
    server = CharDataServer()
    while 1: sleep(10)
