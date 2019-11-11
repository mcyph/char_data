from char_data.CharData import CharData
from char_data.abstract_base_classes.formatters.FormatterBase import PropertyFormatterBase
from char_data.abstract_base_classes.PropertyAccessBase import PropertyAccessBase
from char_data.data_info_types.CharIndexKeyInfo import CharIndexKeyInfo
from char_data.data_info_types.CharIndexValueInfo import CharIndexValueInfo


__char_indexes = None


def CharIndexes(char_data=None):
    global __char_indexes
    if __char_indexes is None:
        __char_indexes = _CharIndexes(char_data=char_data)
    return __char_indexes


class _CharIndexes(PropertyAccessBase):
    #=========================================================#
    #                        Indexes                          #
    #=========================================================#

    def __init__(self, char_data=None):
        if char_data is None:
            char_data = CharData()
        self.char_data = char_data

        PropertyAccessBase.__init__(self, char_data)

    #==================================================================#
    #                           Key-Related                            #
    #==================================================================#

    def search(self, key, value, *args, **kw):
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

    def keys(self, data_source=None):
        """
        Get the index keys, e.g. "Arabic Shaping Group"

        :return: a list of keys in format "source.key"
        """
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

    def get_key_info(self, key):
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
    #                          Value-Related                           #
    #==================================================================#

    def values(self, key):
        """
        Get a list of possible values in MultiIndex in RAW form
        Returns [[key, key_type], ...]
        key is the property name and key_type is e.g. "Fulltext" etc

        :param key:
        :return:
        """
        inst = self.get_class_by_property(key)
        return list(inst.index.values())

    def get_value_info(self, key, value):
        """

        :param key:
        :param value:
        :return:
        """
        # HACK: This really should perhaps be at a "formatter" level!!!

        inst = self.get_class_by_property(key)
        formatted = inst._format_data(0, value)  # HACK HACK HACK!
        return CharIndexValueInfo(value, formatted, description=None)


if __name__ == '__main__':
    char_data = CharData()
    char_indexes = CharIndexes(char_data=char_data)

    print(char_indexes.search('general name', 'smile'))

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
