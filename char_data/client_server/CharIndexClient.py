from toolkit.documentation.copydoc import copydoc
from network_tools.posix_shm_sockets.SHMClient import SHMClient
from char_data.data_info_types.CharIndexKeyInfo import CharIndexKeyInfo
from char_data.data_info_types.CharIndexValueInfo import CharIndexValueInfo
from char_data.abstract_base_classes.CharIndexesBase import CharIndexesBase


class CharIndexClient(CharIndexesBase):
    def __init__(self, char_data=None): # HACK! ============================================================
        """
        A mirror of the `CharIndexes` class, but allowing separation of
        the data into a client-server arrangement, saving memory in
        multi-process setups.
        """
        self.client = SHMClient(port=40518)

    @copydoc(CharIndexesBase.search)
    def search(self, key, value, *args, **kw):
        return self.client.send_json('search', [
            key, value, args, kw
        ])

    @copydoc(CharIndexesBase.keys)
    def keys(self):
        return self.client.send_json('keys', [])

    @copydoc(CharIndexesBase.get_key_info)
    def get_key_info(self, key):
        key_info = self.client.send_json('get_key_info', [key])
        if key_info:
            return CharIndexKeyInfo.from_tuple(*key_info)
        else:
            return None

    @copydoc(CharIndexesBase.values)
    def values(self, key):
        return self.client.send_json('values', [
            key
        ])

    @copydoc(CharIndexesBase.get_value_info)
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
