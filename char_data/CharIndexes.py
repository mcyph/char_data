from char_data.toolkit.patterns.Singleton import Singleton
from char_data.toolkit.documentation.copydoc import copydoc

from char_data.abstract_base_classes.formatters.FormatterBase import PropertyFormatterBase
from char_data.abstract_base_classes.PropertyAccessBase import PropertyAccessBase
from char_data.data_info_types.CharIndexKeyInfo import CharIndexKeyInfo
from char_data.data_info_types.CharIndexValueInfo import CharIndexValueInfo
from char_data.abstract_base_classes.CharIndexesBase import CharIndexesBase


class CharIndexes(CharIndexesBase,
                  PropertyAccessBase,
                  Singleton
                  ):
    def __init__(self, char_data):
        """
        A class that finds Unicode codepoints
        that are classified as being a certain property.
        For example, `search('script', 'Latin')` will give
        `[(65, 90), (97, 122), 170, 186, (192, 214), ..]`.

        Note that each item may either be a two-item tuple,
        signifying an inclusive codepoint range.
        In the above example 65 -> A; 90 -> Z, so (65, 90)
        means characters from A to Z inclusive.
        """
        from char_data.CharData import CharData
        assert isinstance(char_data, CharData), \
            "CharIndexes must be passed a non-network " \
            "(non-CharIndexClient) direct class of CharData"

        self.char_data = char_data

        PropertyAccessBase.__init__(self, char_data)

    #==================================================================#
    #                           Key-Related                            #
    #==================================================================#

    @copydoc(CharIndexesBase.search)
    def search(self, key, value, *args, **kw):
        inst = self.get_class_by_property(key)
        return inst.index.search(value, *args, **kw)

    @copydoc(CharIndexesBase.keys)
    def keys(self, data_source=None):
        LRtn = []

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
                LRtn.append('%s.%s' % (key, property))

        return sorted(LRtn)

    @copydoc(CharIndexesBase.get_key_info)
    def get_key_info(self, key):
        # TODO: Should this all be in `char_data`???
        inst = self.get_class_by_property(key)
        return CharIndexKeyInfo(key, inst.key, inst.index.typ)

    #==================================================================#
    #                          Value-Related                           #
    #==================================================================#

    @copydoc(CharIndexesBase.values)
    def values(self, key):
        inst = self.get_class_by_property(key)
        return list(inst.index.values())

    @copydoc(CharIndexesBase.get_value_info)
    def get_value_info(self, key, value):
        # HACK: This really should perhaps be at a "formatter" level!!!
        inst = self.get_class_by_property(key)
        formatted = inst._format_data(0, value)  # HACK HACK HACK!
        return CharIndexValueInfo(value, formatted, description=None)


if __name__ == '__main__':
    char_data = CharData()
    char_indexes = CharIndexes(char_data=char_data)
    del char_indexes
    char_indexes = CharIndexes(char_data=char_data)

    print(char_indexes.search('name', 'smile'))

    LKeys = []
    for key in list(char_indexes.keys()):
        print(key)
        ciki = char_indexes.get_key_info(key)
        cdki = char_data.get_key_info(key)
        inst = char_data.get_class_by_property(key)

        header = cdki.header_const
        LKeys.append((header, key, inst))
    LKeys.sort()

    for header, key, inst in LKeys:
        print((header, key, inst))
        continue

        LValues = char_indexes.values((source, key))
        if not LValues:
            continue
        
        print(LValues)
        for value in LValues:
            print(('KEY/VALUE:', (key, value), char_indexes.search((source, key), value)))
