from char_data.CharDataKeyInfo import CharDataKeyInfo
from network_tools.mmap_sockets.MMapClient import MMapClient


class CharDataClient:
    def __init__(self):
        self.client = MMapClient(port=40517)

    def keys(self, data_source=None):
        return self.client.send_json('keys', [
            data_source
        ])

    def get_key_info(self, key):
        key_info = self.client.send_json('get_key_info', [key])
        if key_info:
            return CharDataKeyInfo.from_tuple(key_info)
        else:
            return None

    def raw_data(self, key, ord_):
        return self.client.send_json('raw_data', [
            key, ord_
        ])

    def formatted(self, key, ord_):
        return self.client.send_json('formatted', [
            key, ord_
        ])

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
