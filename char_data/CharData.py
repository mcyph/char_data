from toolkit.encodings.surrogates import w_ord

from char_data.storage.data.read.BaseClass import BaseClass
from char_data.data_sources.external.property_formatters import ExternalBaseClass
from char_data.data_sources.external.ExternalBase import ExternalBase
from char_data.data_sources.internal.InternalBase import InternalBase
from char_data.data_sources import DataReader

from DataBase import DataBase


#=========================================================#
#                      Basic Data                         #
#=========================================================#


class CharData(DataBase, DataReader):
    def __init__(self):
        DataReader.__init__(self)
        DataBase.__init__(self, self)

    def __getattr__(self, item):
        return getattr(self.data_reader, item)

    def keys(self, data_source=None):
        """
        Get a list of the possible data source/key combinations
        """
        LRtn = []

        for key, _ in self.LData:
            if data_source and data_source != key:
                continue

            o = getattr(self, key)
            #if not isinstance(o, (InternalBase, ExternalBase)):
                #print('CONTINUE:', key, o)
            #    continue

            for property in dir(o):
                i_o = getattr(o, property)
                if not isinstance(i_o, (BaseClass, ExternalBaseClass)):  # TODO: SUPPORT EXTERNAL BASES HERE!!! =====================
                    #print('CONTINUE 2:', key, o)
                    continue
                LRtn.append((key, i_o.key))

        return sorted(LRtn)

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


char_data = CharData()

