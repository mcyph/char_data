from char_data.formatters.property_formatters import (
    Definition, NoFormatStrings, IRG, UnicodeHex, Frequency,
    BooleanEnum, NoFormatIntegers, Hex, Indices, RadicalStrokes
)
from char_data.formatters.listing_by_properties.property_mappings.consts import (
    HEADER_FIXME, HEADER_DEFINITION, HEADER_NUMERIC, HEADER_READINGS,
    HEADER_LANGUAGE_USAGE, HEADER_VARIANTS, HEADER_GRADES_FREQUENCIES,
    HEADER_TOTAL_STROKES, HEADER_RADICAL_STROKES, HEADER_INPUT,
    HEADER_ENCODING, HEADER_INDICES, HEADER_PHONETIC_INDICES,
    HEADER_ADOBE
)


class NamesList:
    def __init__(self, load_db=True):
        self.also_called = NoFormatStrings(
            self, HEADER_FIXME, 'also called', 'Also Called',
            LISOs=None, index=None
        )
        self.block_description = StringEnum(
            self, HEADER_FIXME, 'block description', 'Block Description',
            LISOs=None, index=None
        )
        self.block_name = StringEnum(
            self, HEADER_FIXME, 'block name', 'Block Name',
            LISOs=None, index=None
        )
        self.comments = NoFormatStrings(
            self, HEADER_FIXME, 'comments', 'Comments',
            LISOs=None, index=None
        )
        self.formally_also_called = NoFormatStrings(
            self, HEADER_FIXME, 'formally also called', 'Formally Also Called',
            LISOs=None, index=None
        )
        self.has_separator = StringEnum(
            self, HEADER_FIXME, 'has separator', 'Has Separator',
            LISOs=None, index=None
        )
        self.see_also = MappingLink(
            self, HEADER_FIXME, 'see also', 'See Also',
            LISOs=None, index=IntegerKeys
        )
        self.subblock_heading = StringEnum(
            self, HEADER_FIXME, 'subblock heading', 'Subblock Heading',
            LISOs=None, index=None
        )
        self.subblock_see_also = MappingLink(
            self, HEADER_FIXME, 'subblock see also', 'Subblock See Also',
            LISOs=None, index=IntegerKeys
        )
        self.subblock_technical_notice = StringEnum(
            self, HEADER_FIXME, 'subblock technical notice', 'Subblock Technical Notice',
            LISOs=None, index=None
        )
        self.technical_notice = NoFormatStrings(
            self, HEADER_FIXME, 'technical notice', 'Technical Notice',
            LISOs=None, index=None
        )
