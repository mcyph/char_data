from char_data.storage.data.read.BaseClass import BaseClass
from char_data.data_sources.external.ExternalBase import ExternalBase
from char_data.data_sources.internal.InternalBase import InternalBase

from DataBase import DataBase
from CharData import char_data


#=========================================================#
#                        Indexes                          #
#=========================================================#


class CharIndexes(DataBase):
    def __init__(self):
        DataBase.__init__(self, char_data)

    def search(self, key, value, *args, **kw):
        """
        search the index key for value, 
        This could be a FullText index, a 
        Radical.AdditionalStrokes index etc
        """
        inst = self.get_class_by_property(key)
        return inst.index.search(value, *args, **kw)

    def keys(self):
        """
        Get the index keys, e.g. "Arabic Shaping Group"
        """
        LRtn = []

        for key, _ in char_data.LData:
            o = getattr(char_data, key)
            if not isinstance(o, (InternalBase, ExternalBase)):
                continue

            for property in dir(o):
                i_o = getattr(o, property)
                if not isinstance(i_o, BaseClass):  # TODO: SUPPORT EXTERNAL BASES HERE!!! =====================
                    continue
                elif not i_o.index:
                    continue

                LRtn.append((key, i_o.key, i_o.index.typ))

        return sorted(LRtn)

    def values(self, key):
        """
        Get a list of possible values in MultiIndex in RAW form
        Returns [[key, key_type], ...]
        key is the property name and key_type is e.g. "Fulltext" etc
        """
        inst = self.get_class_by_property(key)
        return inst.index.keys()


char_indexes = CharIndexes()


if __name__ == '__main__':
    from char_data.CharInfo import Indexes
    
    for key in Indexes.keys():
        LValues = Indexes.values(key)
        if not LValues:
            continue
        
        print LValues
        for value in LValues:
            print 'KEY/VALUE:', (key, value), Indexes.search(key, value)
