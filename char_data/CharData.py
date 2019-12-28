from char_data.toolkit.encodings.surrogates import w_ord
from char_data.toolkit.patterns.Singleton import Singleton
from char_data.toolkit.documentation.copydoc import copydoc

from char_data.data_processors.DataReader import DataReader
from char_data.data_info_types.CharDataKeyInfo import CharDataKeyInfo
from char_data.abstract_base_classes.CharDataBase import CharDataBase
from char_data.abstract_base_classes.PropertyAccessBase import PropertyAccessBase
from char_data.abstract_base_classes.formatters.FormatterBase import PropertyFormatterBase
from char_data.abstract_base_classes.HeadingGrouperBase import HeadingGrouperBase
from char_data.data_processors.consts import DTwoLevelMappings


class CharData(PropertyAccessBase,
               DataReader,
               HeadingGrouperBase,
               CharDataBase,
               Singleton,
               ):

    def __init__(self):
        """
        A class that allows looking up information
        about given Unicode codepoints.

        For example, `raw_data('a', 'name')` will give
        `('LATIN SMALL LETTER A',)`.
        """
        self.char_indexes = None

        DataReader.__init__(self)
        PropertyAccessBase.__init__(self, self)

        from char_data.run_after_loaded import run_all
        run_all()  # HACK!

    def __getattr__(self, item):
        return getattr(self.data_reader, item)

    @copydoc(CharDataBase.get_data_sources)
    def get_data_sources(self):
        return [i[0] for i in self.LData]

    #=============================================================#
    #                  Get Character Data Keys                    #
    #=============================================================#

    @copydoc(CharDataBase.keys)
    def keys(self, data_source=None):
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

    @copydoc(CharDataBase.get_key_info)
    def get_key_info(self, key):
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

    @copydoc(CharDataBase.get_two_level_mapping)
    def get_two_level_mapping(self, key):
        return DTwoLevelMappings.get(key, None)

    #=============================================================#
    #                     Get Character Data                      #
    #=============================================================#

    @copydoc(CharDataBase.get_all_data_for_codepoint)
    def get_all_data_for_codepoint(self, ord_):
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

    @copydoc(CharDataBase.raw_data)
    def raw_data(self, key, ord_):
        if isinstance(ord_, str):
            ord_ = w_ord(ord_)
        
        inst = self.get_class_by_property(key)
        return inst.raw_data(ord_)

    @copydoc(CharDataBase.formatted)
    def formatted(self, key, ord_):
        if isinstance(ord_, str):
            ord_ = w_ord(ord_)
        
        inst = self.get_class_by_property(key)
        return inst.formatted(ord_)

    @copydoc(CharDataBase.html_formatted)
    def html_formatted(self, key, ord_):
        if isinstance(ord_, str):
            ord_ = w_ord(ord_)

        inst = self.get_class_by_property(key)
        return inst.html_formatted(ord_)
