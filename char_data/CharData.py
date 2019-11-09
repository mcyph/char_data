from toolkit.encodings.surrogates import w_ord

from char_data.abstract_base_classes.formatters.PropertyFormatterBase import PropertyFormatterBase
from char_data.data_processors.DataReader import DataReader

from char_data.abstract_base_classes.PropertyAccessBase import PropertyAccessBase
from char_data.data_info_types.CharDataKeyInfo import CharDataKeyInfo


#=========================================================#
#                      Basic Data                         #
#=========================================================#


class CharData(PropertyAccessBase, DataReader):
    def __init__(self):
        DataReader.__init__(self)
        PropertyAccessBase.__init__(self, self)

    def __getattr__(self, item):
        return getattr(self.data_reader, item)

    def keys(self, data_source=None):
        """
        Get a list of the possible data source/key combinations

        Returns a list of ["source.key", ...]
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
                if not isinstance(i_o, PropertyFormatterBase):  # TODO: SUPPORT EXTERNAL BASES HERE!!! =====================
                    #print('CONTINUE 2:', key, o)
                    continue

                LRtn.append('%s.%s' % (key, property))

        return sorted(LRtn)

    def get_key_info(self, key):
        """
        Get information about internal key `key`,
        e.g. to allow displaying the key to humans
        (Kanjidic "freq" might be "Japanese Frequency", for instance)
        """
        inst = self.get_class_by_property(key)
        from .CharIndexes import char_indexes

        if inst.index:
            try:
                ciki = char_indexes.get_key_info(key)
            except KeyError:
                ciki = None
        else:
            ciki = None

        source = inst.parent.key  # HACK!

        return CharDataKeyInfo(
            key, inst.key, inst.short_desc,
            inst.header_const, source, ciki
        )

    def raw_data(self, key, ord_):
        """
        Get the raw data from formatter instance `key`
        about character ordinal or character `ord_`
        """
        if isinstance(ord_, str):
            ord_ = w_ord(ord_)
        
        inst = self.get_class_by_property(key)
        return inst.raw_data(ord_)

    def formatted(self, key, ord_):
        """
        Get the formatted data from formatter instance `key`
        about character ordinal or character `ord_`
        """
        if isinstance(ord_, str):
            ord_ = w_ord(ord_)
        
        inst = self.get_class_by_property(key)
        return inst.formatted(ord_)

    def html_formatted(self, key, ord_):
        """
        Uses the formatted() method above, but also adds basic HTML formatting
        """
        if isinstance(ord_, str):
            ord_ = w_ord(ord_)

        inst = self.get_class_by_property(key)
        return inst.html_formatted(ord_)


char_data = CharData()
