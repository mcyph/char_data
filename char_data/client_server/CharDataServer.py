from char_data.abstract_base_classes.CharDataBase import CharDataBase
from char_data.CharData import CharData

from network_tools.rpc.base_classes.ServerMethodsBase import \
    ServerMethodsBase
from network_tools.rpc_decorators import json_method


class CharDataServer(ServerMethodsBase, CharDataBase):
    port = 40517
    name = 'char_data'

    def __init__(self, char_data=None):
        if char_data is None:
            char_data = CharData()
        self.char_data = char_data

        ServerMethodsBase.__init__(self)

    @json_method
    def get_data_sources(self):
        return self.char_data.get_data_sources()

    @json_method
    def keys(self, data_source=None):
        return self.char_data.keys(
            data_source=data_source
        )

    @json_method
    def get_key_info(self, key):
        key_info = self.char_data.get_key_info(key)
        if key_info:
            return key_info.to_tuple()
        else:
            return None

    @json_method
    def get_all_data_for_codepoint(self, ord_):
        return self.char_data.get_all_data_for_codepoint(ord_)

    # Get data

    @json_method
    def raw_data(self, key, ord_):
        return self.char_data.raw_data(key, ord_)

    @json_method
    def formatted(self, key, ord_):
        return self.char_data.formatted(key, ord_)

    @json_method
    def html_formatted(self, key, ord_):
        return self.char_data.html_formatted(key, ord_)

    # Group mappings

    @json_method
    def get_two_level_mapping(self, key):
        return self.char_data.get_two_level_mapping(key)

    # Group into headings

    @json_method
    def group_by_unicode_name(self, LRanges, name=None):
        return self.char_data.group_by_unicode_name(LRanges, name)

    @json_method
    def group_by_block(self, LRanges):
        return self.char_data.group_by_block(LRanges)

    @json_method
    def group_by_alphabet(self, search, char_indexes=None):
        return self.char_data.group_by_alphabet(search, char_indexes)

    @json_method
    def group_by_chinese_frequency(self, LRanges, LSortBy):
        return self.char_data.group_by_chinese_frequency(LRanges, LSortBy)

    @json_method
    def group_by_japanese_frequency(self, LRanges):
        return self.char_data.group_by_japanese_frequency(LRanges)


if __name__ == '__main__':
    from time import sleep
    server = CharDataServer()
    while 1: sleep(10)
