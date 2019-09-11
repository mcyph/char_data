HEADER_DEFINITION = 0
HEADER_NAMED_ALIASES = 1
HEADER_READINGS = 2
HEADER_SEE_ALSO = 3
HEADER_BLOCK_INFO = 4
HEADER_SUBBLOCK_INFO = 5
HEADER_SCRIPTS_BLOCKS = 8
HEADER_LANGUAGE_USAGE = 6
HEADER_OTHER_SYMBOLS = 7
HEADER_UNICODE_GENERAL = 9
HEADER_CASING = 10
HEADER_NORMALISATION = 11
HEADER_NUMERIC = 12
HEADER_VARIANTS = 13
HEADER_GRADES_FREQUENCIES = 14
HEADER_TOTAL_STROKES = 15
HEADER_RADICAL_STROKES = 16
HEADER_INPUT = 17
HEADER_UNICODE_LAYOUT = 18
HEADER_ENCODING = 19
HEADER_INDICES = 20
HEADER_PHONETIC_INDICES = 21
HEADER_ADOBE = 22
HEADER_FIXME = None  # TODO!!!

DHeaders = {
    HEADER_DEFINITION: 'Definition',
    HEADER_NAMED_ALIASES: 'Named Aliases',
    HEADER_READINGS: 'Readings',
    HEADER_SEE_ALSO: 'See Also',
    HEADER_BLOCK_INFO: 'Block Information',
    HEADER_SUBBLOCK_INFO: 'Subblock Information',
    HEADER_SCRIPTS_BLOCKS: "Scripts/Blocks",
    HEADER_LANGUAGE_USAGE: 'Language Usage',
    HEADER_OTHER_SYMBOLS: "Other Symbols",
    HEADER_UNICODE_GENERAL: 'Unicode General',
    HEADER_CASING: 'Casing',
    HEADER_NORMALISATION: 'Normalisation',
    HEADER_NUMERIC: 'Numeric',
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
        ('European Scripts', [
            'Armenian', 'Carian', 'Coptic', 'Cyrillic', 'Georgian', 'Greek', 'Latin',
            'Lycian', 'Lydian'
        ]),
        ('East Asian Scripts', [
            'Bopomofo', 'Han', 'Hangul', 'Hiragana', 'Katakana', 'Miao', 'Tangut', 'Yi'
        ]),
        ('Indonesia and Oceania', [
            'Balinese', 'Batak', 'Buginese', 'Buhid', 'Hanunoo', 'Nushu', 'Makasar', 'Javanese', 'Rejang',
            'Sundanese', 'Tagalog', 'Tagbanwa'
        ]),
        ('South East Asian', [
            'Cham', 'Hanifi_Rohingya', 'Kayah_Li', 'Khmer', 'Lao', 'Lisu',
            'Meetei_Mayek', 'Myanmar', 'New_Tai_Lue', 'Pahawh_Hmong', 'Tai_Le',
            'Tai_Tham', 'Tai_Viet', 'Thai'
        ]),
        #('Symbols and Punctuation', [
        #    'Currency_Signs', 'Format_Characters', 'General_Punctuation', 'Geometric_Shapes',
        #    'IPA_Alphabet', 'Letterlike_Symbols', 'Mathematical_Signs', 'Modifier_and_Combining_Characters',
        #    'Numbers', 'Pictures_and_Miscellaneous_Symbols', 'Spaces', 'Technical_Symbols'
        #]),
        ('Middle Eastern Scripts', [
            'Arabic', 'Avestan', 'Hatran', 'Hebrew',
            'Imperial_Aramaic', 'Inscriptional_Pahlavi',
            'Inscriptional_Parthian', 'Nabataean', 'Mandaic',
            'Old_South_Arabian', 'Old_Turkic', 'Palmyrene', 'Samaritan',
            'Syriac', 'Thaana'
        ]),
        ('South Asian Scripts', [
            'Ahom',
            'Bengali', 'Bhaiksuki', 'Brahmi', 'Chakma', 'Devanagari', 'Dogra',
            'Gujarati', 'Gurmukhi', 'Grantha', 'Kaithi', 'Kannada',
            'Khojki', 'Khudawadi', 'Limbu',
            'Mahajani', 'Malayalam', 'Modi', 'Mro', 'Multani', 'Newa',
            'Ol_Chiki', 'Oriya', 'Saurashtra', 'Siddham',
            'Sinhala', 'Sharada', 'Syloti_Nagri', 'Takri',
            'Tamil','Telugu', 'Tirhuta'
        ]),
        ('African Scripts', [
            'Adlam', 'Bamum', 'Bassa_Vah', 'Egyptian_Hieroglyphs',
            'Ethiopic', 'Medefaidrin', 'Mende_Kikakui', 'Nko', 'Tifinagh', 'Vai'
        ]),
        ('American Scripts', [
            'Canadian_Aboriginal', 'Cherokee', 'Deseret', 'Osage'
        ]),
        ('Central Asian Scripts', [
            'Kharoshthi', 'Lepcha', 'Manichaean', 'Marchen', 'Mongolian', 'Phags_Pa', 'Sogdian', 'Soyombo', 'Tibetan'
        ]),
        ('Ancient Scripts', [
            'Caucasian_Albanian',
            'Cuneiform', 'Cypriot', 'Elbasan', 'Gothic', 'Linear_A', 'Linear_B', 'Ogham', 'Old_Italic', 'Old_Permic', 'Old_Persian',
            'Phoenician', 'Runic', 'Ugaritic'
        ]),
        ('Miscellaneous', [
            'Braille', 'Common', 'Duployan', 'Glagolitic', 'Inherited',
            'Osmanya', 'Shavian', 'SignWriting'
        ])
    ]
}
