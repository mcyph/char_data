
from char_data.data_processors.external.reformatters.ReformatDataFormatter import ReformatDataFormatter
from char_data.data_processors.external.reformatters.DCommonMappings import DCommonMappings
from char_data.data_processors.consts import HEADER_OTHER_SYMBOLS  # HACK!!!!

from char_data.abstract_base_classes.data_sources.ExternalSourceBase import ExternalSourceBase


class ReformattedData(ExternalSourceBase):
    def __init__(self):
        def get_filter_fn(L):
            def fn():
                if not hasattr(self, 'LCommon'):
                    self.LCommon = self.__get_by_L_block_headings('unicodedata.script', 'Common')

                LRtn = []
                for heading, LUseOnly in L:
                    LRtn.append([
                        heading,
                        self.__filter_to_only(
                            self.LCommon, LUseOnly=LUseOnly
                        )
                    ])
                return LRtn
            return fn

        self.emoji_and_other_symbols = ReformatDataFormatter(
            self, header_const=HEADER_OTHER_SYMBOLS,
            original_name='emoji and other symbols',
            short_desc="Emoji and Other Symbols",
            # Note that DCommonMappings is a SortedDict, so the keys are in order as defined in DCommonMappings.py
            get_L_data=get_filter_fn([mapping, DCommonMappings[mapping]] for mapping in DCommonMappings.keys())
        )

        self.inherited = ReformatDataFormatter(
            self, header_const=HEADER_OTHER_SYMBOLS, original_name='inherited',
            short_desc='Inherited Combining Characters (etc)',
            get_L_data=lambda: [[
                'Inherited Combining Characters (etc)',
                self.__get_by_L_block_headings(
                    'unicodedata.script', 'Inherited'
                )
            ]]
        )

        #self.ipa = ReformatData(
        #    self, header_const=HEADER_FIXME, original_name='ipa', short_desc,
        #    LData=self.__get_by_L_block_headings(FIXME)
        #)

        ExternalSourceBase.__init__(self, 'reformatted')

    def __get_by_L_block_headings(self, key, value, LUseOnly=None):
        from char_data.CharIndexes import char_indexes
        from char_data.formatters.heading_groupers.by_blocks_subblocks.BlockHeadings import get_L_block_headings

        r = get_L_block_headings(
            char_indexes.search(key, value)
        )[-1]

        if LUseOnly:
            return self.__filter_to_only(r, LUseOnly)
        else:
            return r

    def __filter_to_only(self, L, LUseOnly):
        LOut = []

        cur_block_item = None
        use_chars = False

        for item in L:
            if item[0] == 'block':
                cur_block_item = item

                if cur_block_item[1][0] in LUseOnly:
                    LOut.append(cur_block_item)
                    use_chars = True
                else:
                    use_chars = False

            elif item[0] == 'sub_block':
                assert cur_block_item

                if use_chars:
                    LOut.append(item)

            elif item[0] == 'chars':
                if use_chars:
                    LOut.append(item)

            else:
                raise Exception("Unknown value type: %s" % item[0])

        return LOut

