from toolkit.json_tools.JSON import load

from char_data.data_sources.get_key_name import get_key_name
from char_data.data_paths import data_path


class InternalBase:
    def __init__(self, key):
        self.key = key

        self.f_base_data, self.DBaseJSON = self.__get_file_and_D_config(
            key, append_idx=False
        )
        self.f_index_data, self.DIndexJSON = self.__get_file_and_D_config(
            key, append_idx=True
        )

    def __get_file_and_D_config(self, key, append_idx=False):
        DRtn = {}
        output_path = data_path('chardata', '%s/output/%s' % (key, key))

        if append_idx:
            DKeys = load(output_path + '-idx.json')
            f = open('%s-idx.bin' % output_path, 'r+b')
        else:
            DKeys = load(output_path + '.json')
            f = open('%s.bin' % output_path, 'r+b')

        for key, DJSON in list(DKeys.items()):
            set_key_to = get_key_name(key)
            assert not set_key_to in DRtn
            DRtn[set_key_to] = DJSON

        return f, DRtn
