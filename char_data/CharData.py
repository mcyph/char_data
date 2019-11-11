from toolkit.encodings.surrogates import w_ord

from char_data.abstract_base_classes.formatters.FormatterBase import PropertyFormatterBase
from char_data.data_processors.DataReader import DataReader

from char_data.abstract_base_classes.PropertyAccessBase import PropertyAccessBase
from char_data.data_info_types.CharDataKeyInfo import CharDataKeyInfo


__char_data = None


def CharData():
    global __char_data
    if __char_data is None:
        __char_data = _CharData()
    return __char_data


class _CharData(PropertyAccessBase, DataReader):
    def __init__(self):
        DataReader.__init__(self)
        PropertyAccessBase.__init__(self, self)



    def __getattr__(self, item):
        return getattr(self.data_reader, item)

    def get_data_sources(self):
        """
        Get a list of the possible data sources, such as "unicodedata"
        (internal sources) or "hanzi_variants" (external sources)
        :return: a list of data sources
        """
        return [i[0] for i in self.LData]

    #=============================================================#
    #                  Get Character Data Keys                    #
    #=============================================================#

    def keys(self, data_source=None):
        """
        Get a list of the possible data source/key combinations

        :param data_source: one of the data sources returned by
                            get_data_sources (optional)
        :return: a list of ["source.key", ...]
        """
        LRtn = []

        for key, _ in self.LData:
            if data_source and data_source != key:
                continue
            o = getattr(self, key)

            for property in dir(o):
                i_o = getattr(o, property)
                if not isinstance(i_o, PropertyFormatterBase):
                    continue

                LRtn.append('%s.%s' % (key, property))

        return sorted(LRtn)

    def get_key_info(self, key):
        """
        Get information about internal key `key`,
        e.g. to allow displaying the key to humans
        (Kanjidic "freq" might be "Japanese Frequency", for instance)

        :param key: a key in the format "source.key" as returned by
                    `keys()`, or just "key" (will default to the
                    first data source with that key as returned by
                    `get_data_sources()`)
        :return: a `CharDataKeyInfo` object with key information
        """
        inst = self.get_class_by_property(key)

        if inst.index:
            from char_data.CharIndexes import CharIndexes
            char_indexes = CharIndexes(char_data=self)

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

    #=============================================================#
    #                     Get Character Data                      #
    #=============================================================#

    def raw_data(self, key, ord_):
        """
        Get the raw data from formatter instance `key`
        about character ordinal or character `ord_`

        :param key: a key in the format "source.key" as returned by
                    `keys()`, or just "key" (will default to the
                    first data source with that key as returned by
                    `get_data_sources()`)
        :param ord_: the ordinal (or string character) of the
                     character to look up
        :return: the raw data. The format may differ from source
                 to source - may be an integer, a tuple of
                 `((description, ordinal), ...)` for related
                 characters, etc.
        """
        if isinstance(ord_, str):
            ord_ = w_ord(ord_)
        
        inst = self.get_class_by_property(key)
        return inst.raw_data(ord_)

    def formatted(self, key, ord_):
        """
        Get the formatted data from formatter instance `key`
        about character ordinal or character `ord_`

        :param key: a key in the format "source.key" as returned by
                    `keys()`, or just "key" (will default to the
                    first data source with that key as returned by
                    `get_data_sources()`)
        :param ord_: the ordinal (or string character) of the
                     character to look up
        :return: the formatted data as a string
        """
        if isinstance(ord_, str):
            ord_ = w_ord(ord_)
        
        inst = self.get_class_by_property(key)
        return inst.formatted(ord_)

    def html_formatted(self, key, ord_):
        """
        Uses the formatted() method above, but also adds basic
        HTML formatting

        :param key: a key in the format "source.key" as returned by
                    `keys()`, or just "key" (will default to the
                    first data source with that key as returned by
                    `get_data_sources()`)
        :param ord_: the ordinal (or string character) of the
                     character to look up
        :return: the formatted HTML data as a string
        """

        if isinstance(ord_, str):
            ord_ = w_ord(ord_)

        inst = self.get_class_by_property(key)
        return inst.html_formatted(ord_)
