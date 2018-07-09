from toolkit.py_ini import read_D_ini
from char_data.data_paths import data_path


def get_D_rev_enum():
    DRevEnum = {}
    for key, i_D in DEnum.items():
        DRevEnum[key] = dict((value.split('(')[0].strip(), key) 
                             for key, value in i_D.items())
    print DRevEnum
    return DRevEnum


DEnum = read_D_ini(data_path('chardata', 'EnumKeys.ini'))
DRevEnum = get_D_rev_enum()


class Enum:
    def _format_data(self, ord_, data):
        if self.key in DEnum:
            return DEnum[self.key][unicode(data)]
        else: 
            return data # HACK!
