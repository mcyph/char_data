
from char_data.storage.data.read import Boolean, StringData

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
    def formatted(self, ord_):
        data = self.raw_data(ord_)
        
        if self.key in DEnum:
            return DEnum[self.key][unicode(data)]
        else: 
            return data # HACK!


class StringEnum(StringData, Enum):
    def __init__(self, key, f, DJSON):
        """
        Provides expansion of strings to provide more meaning, 
        e.g. a "General Category" of "Lm" might be converted to 
        "Letter, Modifier"
        """
        StringData.__init__(self, key, f, DJSON)


class BooleanEnum(Boolean, Enum):
    def __init__(self, key, f, DJSON):
        """
        Same as StringEnum, except only `True`/`False` allowed,
        used for e.g. IICore to indicate whether a character is
        common in East Asia or not
        """
        Boolean.__init__(self, key, f, DJSON)
