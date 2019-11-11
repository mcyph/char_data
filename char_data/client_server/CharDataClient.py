from char_data.client_server.CharDataServer import CharDataServer
from char_data.data_info_types.CharDataKeyInfo import CharDataKeyInfo
from network_tools.mmap_sockets.MMapClient import MMapClient, client


class CharDataClient:
    def __init__(self):
        self.client = MMapClient(port=40517)

    @client(CharDataServer.keys)
    def keys(self, data_source=None):
        return self.keys.send_json('keys', [
            data_source
        ])

    @client(CharDataServer.get_key_info)
    def get_key_info(self, key):
        key_info = self.get_key_info.send_json('get_key_info', [key])
        if key_info:
            return CharDataKeyInfo.from_tuple(key_info)
        else:
            return None

    @client(CharDataServer.raw_data)
    def raw_data(self, key, ord_):
        return self.client.send_json('raw_data', [
            key, ord_
        ])

    @client(CharDataServer.formatted)
    def formatted(self, key, ord_):
        return self.client.send_json('formatted', [
            key, ord_
        ])

    @client(CharDataServer.html_formatted)
    def html_formatted(self, key, ord_):
        return self.client.send_json('html_formatted', [
            key, ord_
        ])


if __name__ == '__main__':
    client = CharDataClient()

    print(client.keys())
    print(client.get_key_info('unicodedata.general category'))
    print(client.raw_data('unicodedata.general category', 'a'))
    print(client.formatted('unicodedata.general category', 'a'))
    print(client.html_formatted('unicodedata.general category', 'a'))
