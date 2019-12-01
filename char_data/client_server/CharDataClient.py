from toolkit.patterns.Singleton import Singleton
from toolkit.documentation.copydoc import copydoc
from network_tools.rpc.base_classes.ClientMethodsBase import ClientMethodsBase
from network_tools.rpc.posix_shm_sockets.SHMClient import SHMClient

from char_data.data_info_types.CharDataKeyInfo import CharDataKeyInfo
from char_data.abstract_base_classes.CharDataBase import CharDataBase
from char_data.client_server.CharDataServer import CharDataServer as srv


class CharDataClient(CharDataBase,
                     Singleton,
                     ClientMethodsBase
                     ):

    def __init__(self, client_provider=None):
        """
        A mirror of the `CharData` class, but allowing separation of
        the data into a client-server arrangement, saving memory in
        multi-process setups.
        """
        if client_provider is None:
            client_provider = SHMClient(srv)
        ClientMethodsBase.__init__(self, client_provider)

    get_data_sources = srv.get_data_sources.as_rpc()
    keys = srv.keys.as_rpc()

    @copydoc(CharDataBase.get_key_info)
    def get_key_info(self, key):
        key_info = self.send(srv.get_key_info, [key])
        if key_info:
            return CharDataKeyInfo.from_tuple(key_info)
        else:
            return None

    get_all_data_for_codepoint = srv.get_all_data_for_codepoint.as_rpc()
    raw_data = srv.raw_data.as_rpc()
    formatted = srv.formatted.as_rpc()
    html_formatted = srv.html_formatted.as_rpc()

    #=============================================================#
    #                       Get Mappings                          #
    #=============================================================#

    get_two_level_mapping = srv.get_two_level_mapping.as_rpc()

    #=============================================================#
    #                Group Characters by Headings                 #
    #=============================================================#

    group_by_unicode_name = srv.group_by_unicode_name.as_rpc()
    group_by_block = srv.group_by_block.as_rpc()

    @copydoc(CharDataBase.group_by_alphabet)
    def group_by_alphabet(self, search, char_indexes=None):
        # HACK: char_indexes can't be sent!
        return self.send(srv.group_by_alphabet, [
            search, None
        ])

    group_by_chinese_frequency = srv.group_by_chinese_frequency.as_rpc()
    group_by_japanese_frequency = srv.group_by_japanese_frequency.as_rpc()


if __name__ == '__main__':
    client = CharDataClient()

    print(client.keys())
    print(client.get_key_info('unicodedata.general category'))
    print(client.raw_data('unicodedata.general category', 'a'))
    print(client.formatted('unicodedata.general category', 'a'))
    print(client.html_formatted('unicodedata.general category', 'a'))
