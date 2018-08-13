
class ReformatIndex:
    typ = 'reformatted'

    def __init__(self, original_name, get_L_data):
        """
        Provides a way to browse headings and subheadings as if they were
        categories/scripts

        e.g. the "Common" Unicode script has many emojis and symbols etc,
        but we may want to find the "crocodile symbol" under:
            "Miscellaneous Symbols and Pictographs" ->
            "Animal Symbols" (using NamesList data to categorise)

        it's not always convenient to browse "Common" all as a big list,
        so it makes sense to break it up into categories/subcategories
        """
        self.original_name = original_name
        from char_data.data_sources.get_key_name import get_key_name
        self.key = get_key_name(original_name)
        self._get_L_data = get_L_data

        from char_data.run_after_loaded import register
        register(self.__add_to_two_level_mappings)

    def get_L_data(self):
        if not hasattr(self, 'LData'):
            self.LData = self._get_L_data()
        return self.LData

    def __add_to_two_level_mappings(self):
        # TODO: ADD TO DTwoLevelMappings!!!
        LOut = []

        cur_block = None
        LData = self.get_L_data()
        print 'LDATA:', LData

        for item in LData:
            print item

            if item[0] == 'block':
                cur_block = item[1]
                LOut.append((cur_block[0], []))

            elif item[0] == 'sub_block':
                assert cur_block
                LOut[-1][-1].append('%s.%s' % (cur_block[0], item[1][0]))

            elif item[0] == 'chars':
                pass

            else:
                raise Exception("Unknown value type: %s" % item[0])

        from char_data.data_sources.consts import DTwoLevelMappings
        DTwoLevelMappings['reformatted.%s' % self.key] = LOut  # HACK!

    def values(self):
        L = []

        cur_block = None
        for item in self.get_L_data():
            if item[0] == 'block':
                cur_block = item[1]

            if item[0] == 'sub_block':
                assert cur_block
                L.append('%s.%s' % (cur_block[0], item[1][0]))

        return L

    def get_value_info(self, value):
        from char_data.data_sources.internal.indexes.read.CharIndexValueInfo import CharIndexValueInfo
        return CharIndexValueInfo(value, unicode(value.partition('.')[-1]))  # FIXME!!!! ==========================================

    def search(self, search):
        LOut = []

        cur_block_item = None
        use_chars = False

        for item in self.get_L_data():
            if item[0] == 'block':
                cur_block_item = item

            elif item[0] == 'sub_block':
                assert cur_block_item

                if '%s.%s' % (
                    cur_block_item[1][0], item[1][0]
                ) == search:

                    #LOut.append(cur_block_item)
                    #LOut.append(item)

                    use_chars = True
                else:
                    use_chars = False

            elif item[0] == 'chars':
                if use_chars:
                    LOut.extend(item[1])

            else:
                raise Exception("Unknown value type: %s" % item[0])

        return LOut
