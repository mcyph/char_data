class UnicodeData:
    def __init__(self):
        self.age = StringEnum(
            self, HEADER_FIXME, 'age', 'Age',
            LISOs=None, index=StringKeys
        )
        self.also_called = Definition(
            self, HEADER_FIXME, 'also called', 'Also Called',
            LISOs=None, index=Fulltext
        )
        self.arabic_shaping_group = StringEnum(
            self, HEADER_FIXME, 'arabic shaping group', 'Arabic Shaping Group',
            LISOs=None, index=StringKeys
        )
        self.arabic_shaping_type = StringEnum(
            self, HEADER_FIXME, 'arabic shaping type', 'Arabic Shaping Type',
            LISOs=None, index=StringKeys
        )
        self.bidi_mirroring = StringEnum(
            self, HEADER_FIXME, 'bidi mirroring', 'Bidi Mirroring',
            LISOs=None, index=None
        )
        self.bidirectional_category = StringEnum(
            self, HEADER_FIXME, 'bidirectional category', 'Bidirectional Category',
            LISOs=None, index=StringKeys
        )
        self.block = StringEnum(
            self, HEADER_FIXME, 'block', 'Block',
            LISOs=None, index=StringKeys
        )
        self.block_description = Definition(
            self, HEADER_FIXME, 'block description', 'Block Description',
            LISOs=None, index=FIXME
        )
        self.block_name = Definition(
            self, HEADER_FIXME, 'block name', 'Block Name',
            LISOs=None, index=FIXME
        )
        self.canonical_combining_classes = StringEnum(
            self, HEADER_FIXME, 'canonical combining classes', 'Canonical Combining Classes',
            LISOs=None, index=StringKeys
        )
        self.case_folding = UnicodeHex(
            self, HEADER_FIXME, 'case folding', 'Case Folding',
            LISOs=None, index=None
        )
        self.case_folding_status = StringEnum(
            self, HEADER_FIXME, 'case folding status', 'Case Folding Status',
            LISOs=None, index=StringKeys
        )
        self.changes_when_nfkc_casefolded = BooleanEnum(
            self, HEADER_FIXME, 'changes when NFKC casefolded', 'Changes When Nfkc Casefolded',
            LISOs=None, index=None
        )
        self.comments = Definition(
            self, HEADER_FIXME, 'comments', 'Comments',
            LISOs=None, index=Fulltext
        )
        self.compatibility_mapping = MappingLink(
            self, HEADER_FIXME, 'compatibility mapping', 'Compatibility Mapping',
            LISOs=None, index=FIXME
        )
        self.composition_exclusions = StringEnum(
            self, HEADER_FIXME, 'composition exclusions', 'Composition Exclusions',
            LISOs=None, index=None
        )
        self.conscript_blocks = StringEnum(
            self, HEADER_FIXME, 'conscript blocks', 'Conscript Blocks',
            LISOs=None, index=StringKeys
        )
        self.conscript_name = Definition(
            self, HEADER_FIXME, 'conscript name', 'Conscript Name',
            LISOs=None, index=Fulltext
        )
        self.core_properties = StringEnum(
            self, HEADER_FIXME, 'core properties', 'Core Properties',
            LISOs=None, index=StringKeys
        )
        self.decimal_digit_value = NoFormatStrings(
            self, HEADER_FIXME, 'decimal digit value', 'Decimal Digit Value',
            LISOs=None, index=StringKeys
        )
        self.decomposed_form = MappingLink(
            self, HEADER_FIXME, 'decomposed form', 'Decomposed Form',
            LISOs=None, index=FIXME
        )
        self.digit_value = NoFormatStrings(
            self, HEADER_FIXME, 'digit value', 'Digit Value',
            LISOs=None, index=StringKeys
        )
        self.east_asian_width = StringEnum(
            self, HEADER_FIXME, 'east asian width', 'East Asian Width',
            LISOs=None, index=StringKeys
        )
        self.expands_on_nfc = BooleanEnum(
            self, HEADER_FIXME, 'expands on NFC', 'Expands On Nfc',
            LISOs=None, index=None
        )
        self.expands_on_nfd = BooleanEnum(
            self, HEADER_FIXME, 'expands on NFD', 'Expands On Nfd',
            LISOs=None, index=None
        )
        self.expands_on_nfkc = BooleanEnum(
            self, HEADER_FIXME, 'expands on NFKC', 'Expands On Nfkc',
            LISOs=None, index=None
        )
        self.expands_on_nfkd = BooleanEnum(
            self, HEADER_FIXME, 'expands on NFKD', 'Expands On Nfkd',
            LISOs=None, index=None
        )
        self.fc_nfkc_closure = UnicodeHex(
            self, HEADER_FIXME, 'FC NFKC closure', 'Fc Nfkc Closure',
            LISOs=None, index=StringKeys
        )
        self.formally_also_called = Definition(
            self, HEADER_FIXME, 'formally also called', 'Formally Also Called',
            LISOs=None, index=Fulltext
        )
        self.full_composition_exclusion = BooleanEnum(
            self, HEADER_FIXME, 'full composition exclusion', 'Full Composition Exclusion',
            LISOs=None, index=None
        )
        self.general_category = StringEnum(
            self, HEADER_FIXME, 'general category', 'General Category',
            LISOs=None, index=StringKeys
        )
        self.grapheme_break = StringEnum(
            self, HEADER_FIXME, 'grapheme break', 'Grapheme Break',
            LISOs=None, index=StringKeys
        )
        self.joining_type = StringEnum(
            self, HEADER_FIXME, 'joining type', 'Joining Type',
            LISOs=None, index=StringKeys
        )
        self.line_break = StringEnum(
            self, HEADER_FIXME, 'line break', 'Line Break',
            LISOs=None, index=StringKeys
        )
        self.lowercase = UnicodeHex(
            self, HEADER_FIXME, 'lowercase', 'Lowercase',
            LISOs=None, index=None
        )
        self.mirrored = StringEnum(
            self, HEADER_FIXME, 'mirrored', 'Mirrored',
            LISOs=None, index=None
        )
        self.name = Definition(
            self, HEADER_FIXME, 'name', 'Name',
            LISOs=None, index=Fulltext
        )
        self.named_aliases = Definition(
            self, HEADER_FIXME, 'named aliases', 'Named Aliases',
            LISOs=None, index=Fulltext
        )
        self.nfc_quick_check = StringEnum(
            self, HEADER_FIXME, 'NFC quick check', 'Nfc Quick Check',
            LISOs=None, index=None
        )
        self.nfd_quick_check = StringEnum(
            self, HEADER_FIXME, 'NFD quick check', 'Nfd Quick Check',
            LISOs=None, index=None
        )
        self.nfkc_casefold = UnicodeHex(
            self, HEADER_FIXME, 'NFKC casefold', 'Nfkc Casefold',
            LISOs=None, index=StringKeys
        )
        self.nfkc_quick_check = StringEnum(
            self, HEADER_FIXME, 'NFKC quick check', 'Nfkc Quick Check',
            LISOs=None, index=None
        )
        self.nfkd_quick_check = StringEnum(
            self, HEADER_FIXME, 'NFKD quick check', 'Nfkd Quick Check',
            LISOs=None, index=None
        )
        self.normalization_corrections_corrected = UnicodeHex(
            self, HEADER_FIXME, 'normalization corrections corrected', 'Normalization Corrections Corrected',
            LISOs=None, index=None
        )
        self.normalization_corrections_errors = UnicodeHex(
            self, HEADER_FIXME, 'normalization corrections errors', 'Normalization Corrections Errors',
            LISOs=None, index=None
        )
        self.numeric_value = NoFormatStrings(
            self, HEADER_FIXME, 'numeric value', 'Numeric Value',
            LISOs=None, index=StringKeys
        )
        self.property_list = StringEnum(
            self, HEADER_FIXME, 'property list', 'Property List',
            LISOs=None, index=StringKeys
        )
        self.script = StringEnum(
            self, HEADER_FIXME, 'script', 'Script',
            LISOs=None, index=StringKeys
        )
        self.see_also = MappingLink(
            self, HEADER_FIXME, 'see also', 'See Also',
            LISOs=None, index=FIXME
        )
        self.sentence_break = StringEnum(
            self, HEADER_FIXME, 'sentence break', 'Sentence Break',
            LISOs=None, index=StringKeys
        )
        self.special_casing_condition_list = NoFormatStrings(
            self, HEADER_FIXME, 'special casing condition list', 'Special Casing Condition List',
            LISOs=None, index=None
        )
        self.special_casing_lower = UnicodeHex(
            self, HEADER_FIXME, 'special casing lower', 'Special Casing Lower',
            LISOs=None, index=None
        )
        self.special_casing_title = UnicodeHex(
            self, HEADER_FIXME, 'special casing title', 'Special Casing Title',
            LISOs=None, index=None
        )
        self.special_casing_upper = UnicodeHex(
            self, HEADER_FIXME, 'special casing upper', 'Special Casing Upper',
            LISOs=None, index=None
        )
        self.subblock_heading = Definition(
            self, HEADER_FIXME, 'subblock heading', 'Subblock Heading',
            LISOs=None, index=FIXME
        )
        self.subblock_see_also = MappingLink(
            self, HEADER_FIXME, 'subblock see also', 'Subblock See Also',
            LISOs=None, index=FIXME
        )
        self.subblock_technical_notice = Definition(
            self, HEADER_FIXME, 'subblock technical notice', 'Subblock Technical Notice',
            LISOs=None, index=FIXME
        )
        self.technical_notice = Definition(
            self, HEADER_FIXME, 'technical notice', 'Technical Notice',
            LISOs=None, index=Fulltext
        )
        self.titlecase = UnicodeHex(
            self, HEADER_FIXME, 'titlecase', 'Titlecase',
            LISOs=None, index=None
        )
        self.unicode_1_0_name = Definition(
            self, HEADER_FIXME, 'Unicode 1.0 name', 'Unicode 1.0 Name',
            LISOs=None, index=Fulltext
        )
        self.uppercase = UnicodeHex(
            self, HEADER_FIXME, 'uppercase', 'Uppercase',
            LISOs=None, index=None
        )
        self.word_break = StringEnum(
            self, HEADER_FIXME, 'word break', 'Word Break',
            LISOs=None, index=StringKeys
        )
