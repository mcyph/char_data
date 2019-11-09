from char_data.data_info_types.CharIndexKeyInfo import CharIndexKeyInfo
from network_tools.mmap_sockets.MMapClient import MMapClient
from char_data.data_info_types.CharIndexValueInfo import CharIndexValueInfo


class CharIndexClient:
    def __init__(self):
        self.client = MMapClient(port=40518)

    def search(self, key, value, *args, **kw):
        return self.client.send_json('search', [
            key, value, args, kw
        ])

    def keys(self):
        return self.client.send_json('keys', [])

    def get_key_info(self, key):
        key_info = self.client.send_json('get_key_info', [key])
        if key_info:
            return CharIndexKeyInfo.from_tuple(*key_info)
        else:
            return None

    def values(self, key):
        return self.client.send_json('values', [
            key
        ])

    def get_value_info(self, key, value):
        value_info = self.client.send_json('get_value_info', [
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

