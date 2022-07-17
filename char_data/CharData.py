from typing import Union, Optional, List, Any

from char_data.toolkit.encodings.surrogates import w_ord
from char_data.toolkit.patterns.Singleton import Singleton

from char_data.data_processors.DataReader import DataReader
from char_data.data_processors.consts import DTwoLevelMappings
from char_data.data_info_types.CharDataKeyInfo import CharDataKeyInfo
from char_data.data_info_types.CharIndexKeyInfo import CharIndexKeyInfo
from char_data.data_info_types.CharIndexValueInfo import CharIndexValueInfo
from char_data.abstract_base_classes.HeadingGrouperBase import HeadingGrouperBase
from char_data.abstract_base_classes.PropertyAccessBase import PropertyAccessBase
from char_data.abstract_base_classes.formatters.FormatterBase import PropertyFormatterBase


class CharData(PropertyAccessBase,
               DataReader,
               HeadingGrouperBase,
               Singleton,
               SpeedySVCService,
               ):

    def __init__(self):
        """
        A class that allows looking up information
        about given Unicode codepoints.

        For example, `raw_data('a', 'name')` will give
        `('LATIN SMALL LETTER A',)`.
        """
        self.data_reader = None
        self.char_indexes = None

        DataReader.__init__(self)
        PropertyAccessBase.__init__(self, self)

        from char_data.run_after_loaded import run_all
        run_all()  # HACK!

    def __hasattr__(self, item):
        if self.data_reader:
            return hasattr(self.data_reader, item) or \
                   item in self.__dict__
        else:
            return hasattr(self, item)

    def __getattr__(self, item):
        if 'data_reader' in self.__dict__:
            return getattr(self.data_reader, item)
        raise AttributeError

    @service_method()
    def data_sources(self) -> List[str]:
        """
        Get a list of the possible data sources, such as "unicodedata"
        (internal sources) or "hanzi_variants" (external sources)
        :return: a list of data sources
        """
        return [i[0] for i in self.LData]

    #=============================================================#
    #                  Get Character Data Keys                    #
    #=============================================================#

    @service_method()
    def keys(self,
             data_source: Optional[str] = None) -> List[str]:
        """
        Get a list of the possible data source/key combinations

        :param data_source: one of the data sources returned by
                            get_data_sources (optional)
        :return: a list of ["source.key", ...]
        """
        return_list = []

        for key, _ in self.LData:
            if data_source and data_source != key:
                continue
            o = getattr(self, key)

            for property in dir(o):
                i_o = getattr(o, property)
                if not isinstance(i_o, PropertyFormatterBase):
                    continue

                return_list.append('%s.%s' % (key, property))

        return sorted(return_list)

    @service_method()
    def key_info(self,
                     key: str) -> CharDataKeyInfo:
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
            if not self.char_indexes:
                from char_data.CharIndexes import CharIndexes
                self.char_indexes = CharIndexes(char_data=self)

            try:
                ciki = self.char_indexes.get_key_info(key)
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
    #                   Get Two-Level Mappings                    #
    #=============================================================#

    @service_method()
    def two_level_mapping(self, key: str):
        return DTwoLevelMappings.get(key, None)

    #=============================================================#
    #                     Get Character Data                      #
    #=============================================================#

    @service_method()
    def all_data_for_codepoint(self,
                               ord_: Union[int, chr]) -> List[Tuple[Any]]:
        """
        Get a list of all the data associated
        with this codepoint, grouped by heading.

        :param ord_: the character ordinal
        :return: a list of (heading, (property key,
                            short description,
                            html value,
                            raw data),
                            ...)
        """
        ord_ = int(ord_)
        DData = {}

        for key in list(self.keys()):
            inst = self.get_class_by_property(key)
            short_desc = inst.short_desc

            # Get the raw value, to allow linking (if relevant)
            if inst.index and inst.index.typ != 'fulltext':
                raw_data = inst.raw_data(ord_)
                if not isinstance(raw_data, str):
                    # FIXME: Add support for non-string values!
                    raw_data = None
            else:
                raw_data = None

            html_value = inst.html_formatted(ord_)
            # print('get_property_table:', key, short_desc, html_value, raw_data)

            if html_value is not None:
                DData.setdefault(inst.header_const, []).append((
                    key, short_desc, html_value, raw_data
                ))

        for k in DData:
            DData[k].sort(key=lambda i: i[1])

        # Add a "Code Point" header
        # hex_val = hex(ord_)[2:].upper()
        # hex_val = (
        #    hex_val.zfill(4) if len(hex_val) <= 4 else hex_val
        # )
        # DData[6.5] = [
        # HACK: Make it so that it's after scripts/blocks
        #    ('Unicode', 'Unicode', f'U+{hex_val}', None),
        #    ('XML/HTML', 'XML/HTML', f'&amp;#{ord_};', None)
        # ]
        # DHeaders[6.5] = 'Code Point'

        # Make sorted/output by header order
        append_LData = []
        for k in sorted(DData.keys(), key=lambda x: 65535 if x is None else x):
            i_LData = DData[k]
            append_LData.append((k, i_LData))
        return append_LData

    @service_method()
    def raw_data(self,
                 key: str,
                 ord_: Union[int, chr]) -> Union[int, str, tuple]:
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

    @service_method()
    def formatted(self,
                  key: str,
                  ord_: Union[int, chr]) -> str:
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

    @service_method()
    def html_formatted(self,
                       key: str,
                       ord_: Union[int, chr]) -> str:
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


    # === Index-related

    """
    Finds Unicode codepoints
    that are classified as being a certain property.
    For example, `search('script', 'Latin')` will give
    `[(65, 90), (97, 122), 170, 186, (192, 214), ..]`.

    Note that each item may either be a two-item tuple,
    signifying an inclusive codepoint range.
    In the above example 65 -> A; 90 -> Z, so (65, 90)
    means characters from A to Z inclusive.
    """

    #==================================================================#
    #                        Index Key-Related                         #
    #==================================================================#

    @service_method()
    def index_search(self, key, value, *args, **kw):
        """
        search the index key for value,
        This could be a FullText index, a
        Radical.AdditionalStrokes index etc

        :param key:
        :param value:
        :param args:
        :param kw:
        :return:
        """
        inst = self.get_class_by_property(key)
        return inst.index.search(value, *args, **kw)

    @service_method()
    def index_keys(self, data_source=None):
        """
        Get the index keys, e.g. "Arabic Shaping Group"

        :return: a list of keys in format "source.key"
        """
        return_list = []

        for key, _ in self.char_data.LData:
            if data_source and data_source != key:
                continue

            o = getattr(self.char_data, key)

            for property in dir(o):
                i_o = getattr(o, property)
                if not isinstance(i_o, PropertyFormatterBase):
                    continue
                elif not i_o.index:
                    continue

                # Outputs [(internal key name, display key name, index kind), ...]
                return_list.append('%s.%s' % (key, property))

        return sorted(return_list)

    @service_method()
    def index_key_info(self, key):
        """
        Get information about internal key `key`,
        e.g. to allow displaying the key to humans
        (Kanjidic "freq" might be "Japanese Frequency", for instance)

        :param key:
        :return:
        """
        # TODO: Should this all be in `char_data`???
        inst = self.get_class_by_property(key)
        return CharIndexKeyInfo(key, inst.key, inst.index.typ)

    #==================================================================#
    #                      Index Value-Related                         #
    #==================================================================#

    @service_method()
    def index_values(self, key):
        """
        Get a list of possible values in MultiIndex in RAW form
        Returns [[key, key_type], ...]
        key is the property name and key_type is e.g. "Fulltext" etc

        :param key:
        :return:
        """
        inst = self.get_class_by_property(key)
        return list(inst.index.values())

    @service_method()
    def index_value_info(self, key, value):
        """

        :param key:
        :param value:
        :return:
        """
        # HACK: This really should perhaps be at a "formatter" level!!!
        inst = self.get_class_by_property(key)
        formatted = inst._format_data(0, value)  # HACK HACK HACK!
        return CharIndexValueInfo(value, formatted, description=None)
