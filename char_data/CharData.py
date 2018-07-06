from toolkit.encodings.surrogates import w_ord

from char_data.storage.DataReader import DData
from char_data.storage.DataBase import DataBase

#=========================================================#
#                      Basic Data                         #
#=========================================================#


class CharData(DataBase):
    def __init__(self):
        DataBase.__init__(self, DData)

    def keys(self, data_source=None):
        """
        Get a list of the possible data source/key combinations
        """
        LKeys = []
        if data_source:
            LKeys.extend((data_source, key) for key in DData[data_source])
        else:
            for i_data_source, D in DData.items():
                LKeys.extend((i_data_source, key) for key in D.keys())
        LKeys.sort()
        return LKeys

    def raw_data(self, key, ord_):
        """
        Get the raw data from formatter instance `key`
        about character ordinal or character `ord_`
        """
        if isinstance(ord_, basestring):
            ord_ = w_ord(ord_)
        
        inst = self.get_class_by_property(key)
        return inst.raw_data(ord_)

    def formatted(self, key, ord_):
        """
        Get the formatted data from formatter instance `key`
        about character ordinal or character `ord_`
        """
        if isinstance(ord_, basestring):
            ord_ = w_ord(ord_)
        
        inst = self.get_class_by_property(key)
        return inst.formatted(ord_)
