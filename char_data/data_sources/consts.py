HEADER_DEFINITION = 0
HEADER_NAMED_ALIASES = 1
HEADER_READINGS = 2
HEADER_SEE_ALSO = 3
HEADER_BLOCK_INFO = 4
HEADER_SUBBLOCK_INFO = 5
HEADER_SCRIPTS_BLOCKS = 6
HEADER_UNICODE_GENERAL = 7
HEADER_CASING = 8
HEADER_NORMALISATION = 9
HEADER_NUMERIC = 10
HEADER_LANGUAGE_USAGE = 11
HEADER_VARIANTS = 12
HEADER_GRADES_FREQUENCIES = 13
HEADER_TOTAL_STROKES = 14
HEADER_RADICAL_STROKES = 15
HEADER_INPUT = 16
HEADER_ENCODING = 17
HEADER_UNICODE_LAYOUT = 18
HEADER_INDICES = 19
HEADER_PHONETIC_INDICES = 20
HEADER_ADOBE = 21
HEADER_FIXME = None  # TODO!!!

DHeaders = {
    HEADER_DEFINITION: 'Definition',
    HEADER_NAMED_ALIASES: 'Named Aliases',
    HEADER_READINGS: 'Readings',
    HEADER_SEE_ALSO: 'See Also',
    HEADER_BLOCK_INFO: 'Block Information',
    HEADER_SUBBLOCK_INFO: 'Subblock Information',
    HEADER_SCRIPTS_BLOCKS: "Scripts/Blocks",
    HEADER_UNICODE_GENERAL: 'Unicode General',
    HEADER_CASING: 'Casing',
    HEADER_NORMALISATION: 'Normalisation',
    HEADER_NUMERIC: 'Numeric',
    HEADER_LANGUAGE_USAGE: 'Language Usage',
    HEADER_VARIANTS: 'Variants',
    HEADER_GRADES_FREQUENCIES: 'Grades/Frequencies',
    HEADER_TOTAL_STROKES: 'Total Strokes',
    HEADER_RADICAL_STROKES: 'Radical/Additional Strokes',
    HEADER_INPUT: 'Input',
    HEADER_ENCODING: 'Encoding',
    HEADER_UNICODE_LAYOUT: 'Unicode Layout',
    HEADER_INDICES: 'Indices',
    HEADER_PHONETIC_INDICES: 'Phonetic Indices',
    HEADER_ADOBE: 'Adobe',
    None: 'HEADER_FIXME'
}

DTwoLevelMappings = {
    'unicodedata.script': [
        ('East Asian Scripts', [
            'Bopomofo', 'CJK_Symbols', 'Han', 'Hangul', 'Hiragana', 'Katakana', 'Yi'
        ]),
        ('Symbols and Punctuation', [
            'Currency_Signs', 'Format_Characters', 'General_Punctuation', 'Geometric_Shapes',
            'IPA_Alphabet', 'Letterlike_Symbols', 'Mathematical_Signs', 'Modifier_and_Combining_Characters',
            'Numbers', 'Pictures_and_Miscellaneous_Symbols', 'Spaces', 'Technical_Symbols'
        ]),
        ('European Scripts', [
            'Armenian', 'Carian', 'Coptic', 'Cyrillic', 'Georgian', 'Greek', 'Latin',
            'Lycian', 'Lydian'
        ]),
        ('Middle Eastern Scripts', [
            'Arabic', 'Avestan', 'Hebrew', 'Imperial_Aramaic', 'Inscriptional_Pahlavi',
            'Inscriptional_Parthian', 'Old_South_Arabian', 'Old_Turkic', 'Samaritan',
            'Syriac', 'Thaana'
        ]),
        ('Indic Scripts', [
            'Bengali', 'Devanagari', 'Gujarati', 'Gurmukhi', 'Kaithi', 'Kannada', 'Limbu',
            'Malayalam', 'Ol_Chiki', 'Oriya', 'Saurashtra', 'Sinhala', 'Syloti_Nagri',
            'Tamil','Telugu'
        ]),
        ('South East Asian', [
            'Balinese', 'Buginese', 'Cham', 'Javanese', 'Kayah_Li', 'Khmer', 'Lao', 'Lisu',
            'Meetei_Mayek', 'Myanmar', 'New_Tai_Lue', 'Rejang', 'Sundanese', 'Tai_Le',
            'Tai_Tham', 'Tai_Viet', 'Thai'
        ]),
        ('African Scripts', [
            'Bamum', 'Egyptian_Hieroglyphs', 'Ethiopic', 'Nko', 'Tifinagh', 'Vai'
        ]),
        ('American Scripts', [
            'Canadian_Aboriginal', 'Cherokee', 'Deseret'
        ]),
        ('Central Asian Scripts', [
            'Kharoshthi', 'Lepcha', 'Mongolian', 'Phags_Pa', 'Tibetan'
        ]),
        ('Phillipine Scripts', [
            'Buhid', 'Hanunoo', 'Tagalog', 'Tagbanwa'
        ]),
        ('Ancient Scripts', [
            'Cuneiform', 'Cypriot', 'Gothic', 'Linear_B', 'Ogham', 'Old_Italic', 'Old_Persian',
            'Phaistos_Disc', 'Phoenician', 'Runic', 'Ugaritic'
        ]),
        ('Miscellaneous', [
            'Braille', 'Common', 'Control_Characters', 'Glagolitic', 'Inherited',
            'Musical_Symbols', 'Osmanya','Shavian'
        ])
    ]
}
