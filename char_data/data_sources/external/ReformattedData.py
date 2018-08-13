
from char_data.data_sources.external.property_formatters.reformatters.ReformatData import ReformatData
from char_data.data_sources.consts import HEADER_UNICODE_GENERAL  # HACK!!!!

from ExternalBase import ExternalBase


class ReformattedData(ExternalBase):
    def __init__(self):
        self.common = ReformatData(
            self, header_const=HEADER_UNICODE_GENERAL, original_name='common',
            short_desc='Common symbols and emojis etc',
            get_L_data=lambda: self.__get_by_L_block_headings(
                'unicodedata.script', 'Common'
            )
        )

        self.inherited = ReformatData(
            self, header_const=HEADER_UNICODE_GENERAL, original_name='inherited',
            short_desc='Inherited Combining Characters (etc)',
            get_L_data=lambda: self.__get_by_L_block_headings(
                'unicodedata.script', 'Inherited'
            )
        )

        #self.ipa = ReformatData(
        #    self, header_const=HEADER_FIXME, original_name='ipa', short_desc,
        #    LData=self.__get_by_L_block_headings(FIXME)
        #)

        ExternalBase.__init__(self, 'reformatted')

    def __get_by_L_block_headings(self, key, value):
        from char_data import char_indexes
        from char_data.formatters.heading_groupers.by_blocks_subblocks.BlockHeadings import get_L_block_headings

        return get_L_block_headings(
            char_indexes.search(key, value)
        )[-1]

