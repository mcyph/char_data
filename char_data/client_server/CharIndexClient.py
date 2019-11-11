from network_tools.mmap_sockets.MMapClient import MMapClient
from char_data.data_info_types.CharIndexKeyInfo import CharIndexKeyInfo
from char_data.data_info_types.CharIndexValueInfo import CharIndexValueInfo
from char_data.CharIndexes import CharIndexes


class CharIndexClient:
    def __init__(self):
        self.client = MMapClient(port=40518)

    @use_docstring(CharIndexes.search)
    def search(self, key, value, *args, **kw):
        return self.client.send_json('search', [
            key, value, args, kw
        ])

    @use_docstring(CharIndexes.keys)
    def keys(self):
        return self.client.send_json('keys', [])

    @use_docstring(CharIndexes.get_key_info)
    def get_key_info(self, key):
        key_info = self.client.send_json('get_key_info', [key])
        if key_info:
            return CharIndexKeyInfo.from_tuple(*key_info)
        else:
            return None

    @use_docstring(CharIndexes.search)
    def values(self, key):
        return self.client.send_json('values', [
            key
        ])

    @use_docstring(CharIndexes.search)
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

