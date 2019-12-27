
from char_data.data_processors.internal.property_formatters.mappings.MappingLink import MappingLink
from char_data.data_processors.internal.property_formatters.noformat.NoFormatStrings import NoFormatStrings
from char_data.data_processors.internal.property_formatters.enum.BooleanEnum import BooleanEnum
from char_data.data_processors.internal.property_formatters.enum.StringEnum import StringEnum
from char_data.data_processors.internal.property_formatters.definition.Definition import Definition
from char_data.data_processors.internal.property_formatters.hex.UnicodeHex import UnicodeHex


from char_data.data_processors.consts import (
    HEADER_DEFINITION, HEADER_NUMERIC,
    HEADER_NAMED_ALIASES, HEADER_SCRIPTS_BLOCKS,
    HEADER_UNICODE_GENERAL, HEADER_CASING, HEADER_NORMALISATION,
    HEADER_UNICODE_LAYOUT, HEADER_SUBBLOCK_INFO, HEADER_SEE_ALSO
)
from char_data.abstract_base_classes.data_sources.InternalSourceBase import InternalSourceBase


class UnicodeData(InternalSourceBase):
    def __init__(self, char_data):
        InternalSourceBase.__init__(self, char_data, 'unidata')

        #====================================================================#
        #                            Definitions                             #
        #====================================================================#

        self.name = Definition(
            self, HEADER_DEFINITION, 'name', 'Name',
            LISOs=None, index_type='Fulltext'
        )
        self.conscript_name = Definition(
            self, HEADER_DEFINITION, 'conscript name', 'Conscript Name',
            LISOs=None, index_type='Fulltext'
        )
        self.named_aliases = Definition(
            self, HEADER_DEFINITION, 'named aliases', 'Named Aliases',
            LISOs=None, index_type='Fulltext'
        )
        self.unicode_1_0_name = Definition(
            self, HEADER_DEFINITION, 'Unicode 1.0 name', 'Unicode 1.0 Name',
            LISOs=None, index_type='Fulltext'
        )
        self.technical_notice = Definition(
            self, HEADER_DEFINITION, 'technical notice', 'Technical Notice',
            LISOs=None, index_type='Fulltext'
        )
        self.comments = Definition(
            self, HEADER_DEFINITION, 'comments', 'Comments',
            LISOs=None, index_type='Fulltext'
        )

        #====================================================================#
        #                           Named Aliases                            #
        #====================================================================#

        self.also_called = Definition(
            self, HEADER_NAMED_ALIASES, 'also called', 'Also Called',
            LISOs=None, index_type='Fulltext'
        )
        self.formally_also_called = Definition(
            self, HEADER_NAMED_ALIASES, 'formally also called', 'Formally Also Called',
            LISOs=None, index_type='Fulltext'
        )

        #====================================================================#
        #                            See Also                                #
        #====================================================================#

        self.see_also = MappingLink(
            self, HEADER_SEE_ALSO, 'see also', 'See Also',
            LISOs=None, index_type='FIXME'
        )
        self.subblock_see_also = MappingLink(
            self, HEADER_SEE_ALSO, 'subblock see also', 'Subblock See Also',
            LISOs=None, index_type='FIXME'
        )

        #====================================================================#
        #                          Scripts/Blocks                            #
        #====================================================================#

        self.block = StringEnum(
            self, HEADER_SCRIPTS_BLOCKS, 'block', 'Block',
            LISOs=None, index_type='StringKeys'
        )
        self.conscript_blocks = StringEnum(
            self, HEADER_SCRIPTS_BLOCKS, 'conscript blocks', 'Conscript Blocks',
            LISOs=None, index_type='StringKeys'
        )
        self.script = StringEnum(
            self, HEADER_SCRIPTS_BLOCKS, 'script', 'Script',
            LISOs=None, index_type='StringKeys'
        )
        self.block_name = Definition(
            self, HEADER_SCRIPTS_BLOCKS, 'block name', 'Block Name',
            LISOs=None, index_type='FIXME'
        )
        self.block_description = Definition(
            self, HEADER_SCRIPTS_BLOCKS, 'block description', 'Block Description',
            LISOs=None, index_type='FIXME'
        )

        #====================================================================#
        #                            Subblocks                               #
        #====================================================================#

        self.subblock_heading = Definition(
            self, HEADER_SUBBLOCK_INFO, 'subblock heading', 'Subblock Heading',
            LISOs=None, index_type='StringKeys'
        )
        self.subblock_technical_notice = Definition(
            self, HEADER_SUBBLOCK_INFO, 'subblock technical notice', 'Subblock Technical Notice',
            LISOs=None, index_type='StringKeys'
        )

        #====================================================================#
        #                     General Unicode Properties                     #
        #====================================================================#

        self.age = StringEnum(
            self, HEADER_UNICODE_GENERAL, 'age', 'Age',
            LISOs=None, index_type='StringKeys'
        )
        self.case_folding_status = StringEnum(
            self, HEADER_UNICODE_GENERAL, 'case folding status', 'Case Folding Status',
            LISOs=None, index_type='StringKeys'
        )
        self.core_properties = StringEnum(
            self, HEADER_UNICODE_GENERAL, 'core properties', 'Core Properties',
            LISOs=None, index_type='StringKeys'
        )
        self.east_asian_width = StringEnum(
            self, HEADER_UNICODE_GENERAL, 'east asian width', 'East Asian Width',
            LISOs=None, index_type='StringKeys'
        )
        self.general_category = StringEnum(
            self, HEADER_UNICODE_GENERAL, 'general category', 'General Category',
            LISOs=None, index_type='StringKeys'
        )
        self.property_list = StringEnum(
            self, HEADER_UNICODE_GENERAL, 'property list', 'Property List',
            LISOs=None, index_type='StringKeys'
        )

        #====================================================================#
        #                               Casing                               #
        #====================================================================#

        self.case_folding = UnicodeHex(
            self, HEADER_CASING, 'case folding', 'Case Folding',
            LISOs=None
        )
        self.lowercase = UnicodeHex(
            self, HEADER_CASING, 'lowercase', 'Lowercase',
            LISOs=None
        )
        self.special_casing_condition_list = NoFormatStrings(
            self, HEADER_CASING, 'special casing condition list', 'Special Casing Condition List',
            LISOs=None
        )
        self.special_casing_lower = UnicodeHex(
            self, HEADER_CASING, 'special casing lower', 'Special Casing Lower',
            LISOs=None
        )
        self.special_casing_title = UnicodeHex(
            self, HEADER_CASING, 'special casing title', 'Special Casing Title',
            LISOs=None
        )
        self.special_casing_upper = UnicodeHex(
            self, HEADER_CASING, 'special casing upper', 'Special Casing Upper',
            LISOs=None
        )
        self.titlecase = UnicodeHex(
            self, HEADER_CASING, 'titlecase', 'Titlecase',
            LISOs=None
        )
        self.uppercase = UnicodeHex(
            self, HEADER_CASING, 'uppercase', 'Uppercase',
            LISOs=None
        )

        #====================================================================#
        #                          Normalisation                             #
        #====================================================================#

        self.changes_when_nfkc_casefolded = BooleanEnum(
            self, HEADER_NORMALISATION, 'changes when NFKC casefolded', 'Changes When Nfkc Casefolded',
            LISOs=None
        )
        self.compatibility_mapping = MappingLink(
            self, HEADER_NORMALISATION, 'compatibility mapping', 'Compatibility Mapping',
            LISOs=None, index_type='FIXME'
        )
        self.decomposed_form = MappingLink(
            self, HEADER_NORMALISATION, 'decomposed form', 'Decomposed Form',
            LISOs=None, index_type='FIXME'
        )
        self.expands_on_nfc = BooleanEnum(
            self, HEADER_NORMALISATION, 'expands on NFC', 'Expands On Nfc',
            LISOs=None
        )
        self.expands_on_nfd = BooleanEnum(
            self, HEADER_NORMALISATION, 'expands on NFD', 'Expands On Nfd',
            LISOs=None
        )
        self.expands_on_nfkc = BooleanEnum(
            self, HEADER_NORMALISATION, 'expands on NFKC', 'Expands On Nfkc',
            LISOs=None
        )
        self.expands_on_nfkd = BooleanEnum(
            self, HEADER_NORMALISATION, 'expands on NFKD', 'Expands On Nfkd',
            LISOs=None
        )
        self.fc_nfkc_closure = UnicodeHex(
            self, HEADER_NORMALISATION, 'FC NFKC closure', 'Fc Nfkc Closure',
            LISOs=None, index_type='StringKeys'
        )
        self.full_composition_exclusion = BooleanEnum(
            self, HEADER_NORMALISATION, 'full composition exclusion', 'Full Composition Exclusion',
            LISOs=None
        )
        self.nfc_quick_check = StringEnum(
            self, HEADER_NORMALISATION, 'NFC quick check', 'Nfc Quick Check',
            LISOs=None
        )
        self.nfd_quick_check = StringEnum(
            self, HEADER_NORMALISATION, 'NFD quick check', 'Nfd Quick Check',
            LISOs=None
        )
        self.nfkc_casefold = UnicodeHex(
            self, HEADER_NORMALISATION, 'NFKC casefold', 'Nfkc Casefold',
            LISOs=None, index_type='StringKeys'
        )
        self.nfkc_quick_check = StringEnum(
            self, HEADER_NORMALISATION, 'NFKC quick check', 'Nfkc Quick Check',
            LISOs=None
        )
        self.nfkd_quick_check = StringEnum(
            self, HEADER_NORMALISATION, 'NFKD quick check', 'Nfkd Quick Check',
            LISOs=None
        )
        self.normalization_corrections_corrected = UnicodeHex(
            self, HEADER_NORMALISATION, 'normalization corrections corrected',
            'Normalization Corrections Corrected',
            LISOs=None
        )
        self.normalization_corrections_errors = UnicodeHex(
            self, HEADER_NORMALISATION, 'normalization corrections errors',
            'Normalization Corrections Errors',
            LISOs=None
        )

        #====================================================================#
        #                              Numeric                               #
        #====================================================================#

        self.decimal_digit_value = NoFormatStrings(
            self, HEADER_NUMERIC, 'decimal digit value', 'Decimal Digit Value',
            LISOs=None, index_type='StringKeys'
        )
        self.digit_value = NoFormatStrings(
            self, HEADER_NUMERIC, 'digit value', 'Digit Value',
            LISOs=None, index_type='StringKeys'
        )
        self.numeric_value = NoFormatStrings(
            self, HEADER_NUMERIC, 'numeric value', 'Numeric Value',
            LISOs=None, index_type='StringKeys'
        )

        #====================================================================#
        #                          Unicode Layout                            #
        #====================================================================#

        self.arabic_shaping_group = StringEnum(
            self, HEADER_UNICODE_LAYOUT, 'arabic shaping group', 'Arabic Shaping Group',
            LISOs=None, index_type='StringKeys'
        )
        self.arabic_shaping_type = StringEnum(
            self, HEADER_UNICODE_LAYOUT, 'arabic shaping type', 'Arabic Shaping Type',
            LISOs=None, index_type='StringKeys'
        )
        self.bidi_mirroring = StringEnum(
            self, HEADER_UNICODE_LAYOUT, 'bidi mirroring', 'Bidi Mirroring',
            LISOs=None
        )
        self.bidirectional_category = StringEnum(
            self, HEADER_UNICODE_LAYOUT, 'bidirectional category', 'Bidirectional Category',
            LISOs=None, index_type='StringKeys'
        )
        self.canonical_combining_classes = StringEnum(
            self, HEADER_UNICODE_LAYOUT, 'canonical combining classes', 'Canonical Combining Classes',
            LISOs=None, index_type='StringKeys'
        )
        self.composition_exclusions = StringEnum(
            self, HEADER_UNICODE_LAYOUT, 'composition exclusions', 'Composition Exclusions',
            LISOs=None
        )
        self.grapheme_break = StringEnum(
            self, HEADER_UNICODE_LAYOUT, 'grapheme break', 'Grapheme Break',
            LISOs=None, index_type='StringKeys'
        )
        self.joining_type = StringEnum(
            self, HEADER_UNICODE_LAYOUT, 'joining type', 'Joining Type',
            LISOs=None, index_type='StringKeys'
        )
        self.line_break = StringEnum(
            self, HEADER_UNICODE_LAYOUT, 'line break', 'Line Break',
            LISOs=None, index_type='StringKeys'
        )
        self.mirrored = StringEnum(
            self, HEADER_UNICODE_LAYOUT, 'mirrored', 'Mirrored',
            LISOs=None
        )
        self.sentence_break = StringEnum(
            self, HEADER_UNICODE_LAYOUT, 'sentence break', 'Sentence Break',
            LISOs=None, index_type='StringKeys'
        )
        self.word_break = StringEnum(
            self, HEADER_UNICODE_LAYOUT, 'word break', 'Word Break',
            LISOs=None, index_type='StringKeys'
        )
