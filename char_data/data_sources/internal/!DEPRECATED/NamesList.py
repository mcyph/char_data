from char_data.data_sources.internal.property_formatters import (
    NoFormatStrings, MappingLink, StringEnum
)
from char_data.data_sources.consts import (
    HEADER_FIXME, HEADER_DEFINITION,
    HEADER_SEE_ALSO, HEADER_BLOCK_INFO, HEADER_SUBBLOCK_INFO
)


class NamesList:
    def __init__(self, load_db=True):
        self.has_separator = StringEnum(
            self, HEADER_FIXME, 'has separator', 'Has Separator'
        )

        #====================================================================#
        #                            Definitions                             #
        #====================================================================#

        self.comments = NoFormatStrings(
            self, HEADER_DEFINITION, 'comments', 'Comments'
        )
        self.formally_also_called = NoFormatStrings(
            self, HEADER_DEFINITION, 'formally also called', 'Formally Also Called'
        )
        self.also_called = NoFormatStrings(
            self, HEADER_DEFINITION, 'also called', 'Also Called'
        )
        self.technical_notice = NoFormatStrings(
            self, HEADER_DEFINITION, 'technical notice', 'Technical Notice'
        )

        #====================================================================#
        #                             See Also                               #
        #====================================================================#

        self.see_also = MappingLink(
            self, HEADER_SEE_ALSO, 'see also', 'See Also',
            index='IntegerKeys'
        )
        self.subblock_see_also = MappingLink(
            self, HEADER_SEE_ALSO, 'subblock see also', 'Subblock See Also',
            index='IntegerKeys'
        )

        #====================================================================#
        #                        Block Information                           #
        #====================================================================#

        self.block_description = StringEnum(
            self, HEADER_BLOCK_INFO, 'block description', 'Block Description'
        )
        self.block_name = StringEnum(
            self, HEADER_BLOCK_INFO, 'block name', 'Block Name'
        )

        #====================================================================#
        #                      Subblock Information                          #
        #====================================================================#

        self.subblock_heading = StringEnum(
            self, HEADER_SUBBLOCK_INFO, 'subblock heading', 'Subblock Heading'
        )
        self.subblock_technical_notice = StringEnum(
            self, HEADER_SUBBLOCK_INFO, 'subblock technical notice', 'Subblock Technical Notice',
        )
