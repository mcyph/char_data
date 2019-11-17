from toolkit.documentation.copydoc import copydoc
from char_data.data_info_types.CharDataKeyInfo import CharDataKeyInfo
from network_tools.posix_shm_sockets.SHMClient import SHMClient
from char_data.abstract_base_classes.CharDataBase import CharDataBase


class CharDataClient(CharDataBase):
    def __init__(self):
        """
        A mirror of the `CharData` class, but allowing separation of
        the data into a client-server arrangement, saving memory in
        multi-process setups.
        """
        self.client = SHMClient(port=40517)

    @copydoc(CharDataBase.get_data_sources)
    def get_data_sources(self):
        return self.client.send_json('get_data_sources', []) # FIXME!!!!! ===================================

    @copydoc(CharDataBase.keys)
    def keys(self, data_source=None):
        return self.client.send_json('keys', [data_source])

    @copydoc(CharDataBase.get_key_info)
    def get_key_info(self, key):
        key_info = self.client.send_json('get_key_info', [key])
        if key_info:
            return CharDataKeyInfo.from_tuple(key_info)
        else:
            return None

    @copydoc(CharDataBase.get_all_data_for_codepoint)
    def get_all_data_for_codepoint(self, ord_):
        return self.client.send_json('get_all_data_for_codepoint', [ord_])

    @copydoc(CharDataBase.raw_data)
    def raw_data(self, key, ord_):
        return self.client.send_json('raw_data', [key, ord_])

    @copydoc(CharDataBase.formatted)
    def formatted(self, key, ord_):
        return self.client.send_json('formatted', [key, ord_])

    @copydoc(CharDataBase.html_formatted)
    def html_formatted(self, key, ord_):
        return self.client.send_json('html_formatted', [key, ord_])

    #=============================================================#
    #                       Get Mappings                          #
    #=============================================================#

    @copydoc(CharDataBase.get_two_level_mapping)
    def get_two_level_mapping(self, key):
        return self.client.send_json('get_two_level_mapping', [key])

    #=============================================================#
    #                Group Characters by Headings                 #
    #=============================================================#

    @copydoc(CharDataBase.group_by_unicode_name)
    def group_by_unicode_name(self, LRanges, name=None):
        return self.client.send_json('group_into_unicode_name_headings', [
            LRanges, name
        ])

    @copydoc(CharDataBase.group_by_block)
    def group_by_block(self, LRanges):
        return self.client.send_json('group_into_block_headings', [
            LRanges
        ])

    @copydoc(CharDataBase.group_by_alphabet)
    def group_by_alphabet(self, search, char_indexes=None):
        # HACK: char_indexes can't be sent!
        return self.client.send_json('group_into_alphabet_headings', [
            search, None
        ])

    @copydoc(CharDataBase.group_by_chinese_frequency)
    def group_by_chinese_frequency(self, LRanges, LSortBy):
        return self.client.send_json('group_into_chinese_frequency_headings', [
            LRanges, LSortBy
        ])

    @copydoc(CharDataBase.group_by_japanese_frequency)
    def group_by_japanese_frequency(self, LRanges):
        return self.client.send_json('group_into_japanese_frequency_headings', [
            LRanges
        ])


if __name__ == '__main__':
    client = CharDataClient()

    print(client.keys())
    print(client.get_key_info('unicodedata.general category'))
    print(client.raw_data('unicodedata.general category', 'a'))
    print(client.formatted('unicodedata.general category', 'a'))
    print(client.html_formatted('unicodedata.general category', 'a'))
