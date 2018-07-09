from toolkit.encodings.surrogates import w_ord

from char_data.storage import data_reader
from char_data.storage.data.read.BaseClass import BaseClass
from char_data.data_sources.external.ExternalBase import ExternalBase
from char_data.data_sources.internal.InternalBase import InternalBase

from DataBase import DataBase


#=========================================================#
#                      Basic Data                         #
#=========================================================#


class CharData(DataBase):
    def __init__(self):
        DataBase.__init__(self, data_reader)

    def keys(self, data_source=None):
        """
        Get a list of the possible data source/key combinations
        """
        LRtn = []

        for key, _ in data_reader.LData:
            o = getattr(data_reader, key)
            if not isinstance(o, (InternalBase, ExternalBase)):
                continue

            for property in dir(o):
                i_o = getattr(o, property)
                if not isinstance(i_o, BaseClass):  # TODO: SUPPORT EXTERNAL BASES HERE!!! =====================
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
