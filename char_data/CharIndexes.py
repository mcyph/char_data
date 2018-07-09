from char_data.storage.DataReader import DIndexes

from DataBase import DataBase


#=========================================================#
#                        Indexes                          #
#=========================================================#


class CharIndexes(DataBase):
    def __init__(self):
        DataBase.__init__(self, DIndexes)

    def search(self, key, value, *args, **kw):
        """
        search the index key for value, 
        This could be a FullText index, a 
        Radical.AdditionalStrokes index etc
        """
        inst = self.get_class_by_property(key)
        return inst.search(value, *args, **kw)

    def keys(self):
        """
        Get the index keys, e.g. "Arabic Shaping Group"
        """
        LRtn = []
        for key, DKeys in DIndexes.items():
            for i in DKeys:
                LRtn.append((key, i, DKeys[i].typ))
        return sorted(LRtn)

    def values(self, key):
        """
        Get a list of possible values in MultiIndex in RAW form
        Returns [[key, key_type], ...]
        key is the property name and key_type is e.g. "Fulltext" etc
        """
        inst = self.get_class_by_property(key)
        return inst.keys()


if __name__ == '__main__':
    from char_data.CharInfo import Indexes
    
    for key in Indexes.keys():
        LValues = Indexes.values(key)
        if not LValues:
            continue
        
        print LValues
        for value in LValues:
            print 'KEY/VALUE:', (key, value), Indexes.search(key, value)
