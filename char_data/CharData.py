from toolkit.encodings.surrogates import w_ord

from DataSourceBase import DataSourceBase
from char_data.data_sources.DataReader import DataReader

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

        Returns a list of [(internal key name, display key name), ...]
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
                if not isinstance(i_o, DataSourceBase):  # TODO: SUPPORT EXTERNAL BASES HERE!!! =====================
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

    def html_formatted(self, key, ord_):
        """
        Uses the formatted() method above, but also adds basic HTML formatting
        """
        if isinstance(ord_, basestring):
            ord_ = w_ord(ord_)

        inst = self.get_class_by_property(key)
        return inst.html_formatted(ord_)


char_data = CharData()

