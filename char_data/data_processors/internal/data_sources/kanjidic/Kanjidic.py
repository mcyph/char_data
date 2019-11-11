from char_data.data_processors.internal.property_formatters import (
    Definition, NoFormatStrings, Frequency,
    NoFormatIntegers, Indices,
    StringEnum, Readings
)
from char_data.data_processors.consts import (
    HEADER_DEFINITION, HEADER_READINGS,
    HEADER_GRADES_FREQUENCIES,
    HEADER_TOTAL_STROKES, HEADER_RADICAL_STROKES, HEADER_INPUT,
    HEADER_ENCODING, HEADER_INDICES
)
from char_data.abstract_base_classes.data_sources.InternalSourceBase import InternalSourceBase


class Kanjidic(InternalSourceBase):
    def __init__(self, char_data, load_db=True):
        InternalSourceBase.__init__(self, char_data, 'kanjidic')

        #====================================================================#
        #                            Definitions                             #
        #====================================================================#

        self.meaning = Definition(
            self, HEADER_DEFINITION, 'meaning', 'Meaning',
            LISOs=['jpn'], index_type='Fulltext'
        )
        self.meaning_es = Definition(
            self, HEADER_DEFINITION, 'meaning_es', 'Spanish Meaning',
            LISOs=['jpn'], index_type='Fulltext'
        )
        self.meaning_fr = Definition(
            self, HEADER_DEFINITION, 'meaning_fr', 'French Meaning',
            LISOs=['jpn'], index_type='Fulltext'
        )
        self.meaning_pt = Definition(
            self, HEADER_DEFINITION, 'meaning_pt', 'Portuguese Meaning',
            LISOs=['jpn'], index_type='Fulltext'
        )

        #====================================================================#
        #                             Readings                               #
        #====================================================================#

        self.rad_name = Readings(
            self, HEADER_READINGS, 'rad_name', 'Radical Name in Japanese',
            LISOs=['jpn'], index_type='CompressedNames'
        )
        self.reading_ja_kun = Readings(
            self, HEADER_READINGS, 'reading_ja_kun', 'Japanese Kun',
            LISOs=['jpn'], index_type='CompressedNames'
        )
        self.reading_ja_on = Readings(
            self, HEADER_READINGS, 'reading_ja_on', 'Japanese On',
            LISOs=['jpn'], index_type='CompressedNames'
        )
        self.reading_korean_h = Readings(
            self, HEADER_READINGS, 'reading_korean_h', 'Korean Hangul',
            LISOs=['kor'], index_type='CompressedNames'
        )
        self.reading_korean_r = Readings(
            self, HEADER_READINGS, 'reading_korean_r', 'Korean Revised Translit',
            LISOs=['kor'], index_type='CompressedNames'
        )
        self.reading_nanori = Readings(
            self, HEADER_READINGS, 'reading_nanori', 'Japanese Nanori',
            LISOs=['jpn'], index_type='CompressedNames'
        )
        self.reading_pinyin = Readings(
            self, HEADER_READINGS, 'reading_pinyin', 'Pinyin',
            LISOs=['cmn'], index_type='CompressedNames'
        )

        #====================================================================#
        #                         Grades/Frequencies                         #
        #====================================================================#

        self.freq = Frequency(
            self, HEADER_GRADES_FREQUENCIES, 'freq', 'Japanese Frequency',
            LISOs=['jpn'], index_type='IntegerKeys'
        )
        self.grade = Frequency(
            self, HEADER_GRADES_FREQUENCIES, 'grade', 'Japanese Grade',
            LISOs=['jpn'], index_type='IntegerKeys'
        )
        self.jlpt = Frequency(
            self, HEADER_GRADES_FREQUENCIES, 'jlpt', 'JLPT Level',
            LISOs=['jpn'], index_type='IntegerKeys'
        )

        #====================================================================#
        #                          Total Strokes                             #
        #====================================================================#

        self.stroke_count = NoFormatIntegers(
            self, HEADER_TOTAL_STROKES, 'stroke_count', 'Japanese Strokes',
            LISOs=['jpn'], index_type='IntegerKeys'
        )

        #====================================================================#
        #                Kangxi Radical/Additional Strokes                   #
        #====================================================================#

        self.rad_classical = NoFormatStrings(
            self, HEADER_RADICAL_STROKES, 'rad_classical',
            'KangXi Zidian Radical',
            LISOs=['All'], index_type='RadicalStrokes'
        )
        self.rad_nelson_c = NoFormatStrings(
            self, HEADER_RADICAL_STROKES, 'rad_nelson_c',
            'Nelson Modern Japanese-English Radical',
            LISOs=['jpn'], index_type='RadicalStrokes'
        )

        #====================================================================#
        #                           Input Data                               #
        #====================================================================#

        self.querycode_deroo = NoFormatStrings(
            self, HEADER_INPUT, 'querycode_deroo',
            'Bojinsha 2001 Kanji Code',
            LISOs=['jpn'], index_type='StringKeys'
        )
        self.querycode_four_corner = NoFormatStrings(
            self, HEADER_INPUT, 'querycode_four_corner',
            'Four Corner Code',
            LISOs=['cmn', 'yue', 'kor', 'vie', 'ltc'], index_type='StringKeys'
        )
        self.querycode_sh_desc = NoFormatStrings(
            self, HEADER_INPUT, 'querycode_sh_desc',
            'Tuttle the Kanji Dictionary Code',
            LISOs=['jpn'], index_type='StringKeys'
        )

        #====================================================================#
        #                            Encoding                                #
        #====================================================================#

        self.crossref_deroo = StringEnum(
            self, HEADER_ENCODING, 'crossref_deroo',
            'De Roo Number',
            LISOs=['jpn']
        )
        self.crossref_jis208 = StringEnum(
            self, HEADER_ENCODING, 'crossref_jis208',
            'JIS X 0208 Code',
            LISOs=['jpn']
        )
        self.crossref_jis212 = StringEnum(
            self, HEADER_ENCODING, 'crossref_jis212',
            'JIS X 0212 Code',
            LISOs=['jpn']
        )
        self.crossref_jis213 = StringEnum(
            self, HEADER_ENCODING, 'crossref_jis213',
            'JIS X 0213 Code',
            LISOs=['jpn']
        )
        self.crossref_nelson_c = StringEnum(
            self, HEADER_ENCODING, 'crossref_nelson_c',
            'Classic Nelson Code',
            LISOs=['jpn']
        )
        self.crossref_njecd = StringEnum(
            self, HEADER_ENCODING, 'crossref_njecd',
            'Halpern NJECD Index',
            LISOs=['jpn']
        )
        self.crossref_oneill = StringEnum(
            self, HEADER_ENCODING, 'crossref_oneill',
            'Japanese Names Code',
            LISOs=['jpn']
        )
        self.crossref_s_h = StringEnum(
            self, HEADER_ENCODING, 'crossref_s_h',
            'The Kanji Dictionary Descriptor',
            LISOs=['jpn']
        )
        self.crossref_ucs = StringEnum(
            self, HEADER_ENCODING, 'crossref_ucs',
            'Unicode UCS Code',
            LISOs=['jpn']
        )

        #====================================================================#
        #                             Indices                                #
        #====================================================================#

        self.dicref_busy_people = Indices(
            self, HEADER_INDICES, 'dicref_busy_people',
            'Japanese for Busy People',
            LISOs=['jpn']
        )
        self.dicref_crowley = Indices(
            self, HEADER_INDICES, 'dicref_crowley',
            'The Kanji Way to Japanese Language Power',
            LISOs=['jpn'], index_type='Indices'
        )
        self.dicref_gakken = Indices(
            self, HEADER_INDICES, 'dicref_gakken',
            'Gakken Kanji Dictionary',
            LISOs=['jpn'], index_type='Indices'
        )
        self.dicref_halpern_kkld = Indices(
            self, HEADER_INDICES, 'dicref_halpern_kkld',
            'Kodansha Kanji Learners Dictionary',
            LISOs=['jpn'], index_type='Indices'
        )
        self.dicref_halpern_njecd = Indices(
            self, HEADER_INDICES, 'dicref_halpern_njecd',
            'New Japanese-English Character Dictionary',
            LISOs=['jpn'], index_type='Indices'
        )
        self.dicref_heisig = Indices(
            self, HEADER_INDICES, 'dicref_heisig',
            'Remembering the Kanji',
            LISOs=['jpn'], index_type='Indices'
        )
        self.dicref_henshall = Indices(
            self, HEADER_INDICES, 'dicref_henshall',
            'A Guide to Remembering Japanese Characters',
            LISOs=['jpn'], index_type='Indices'
        )
        self.dicref_henshall3 = Indices(
            self, HEADER_INDICES, 'dicref_henshall3',
            'A Guide to Reading and Writing Japanese (Henshall)',
            LISOs=['jpn'], index_type='Indices'
        )
        self.dicref_jf_cards = Indices(
            self, HEADER_INDICES, 'dicref_jf_cards',
            'Japanese Kanji Flashcards',
            LISOs=['jpn'], index_type='Indices'
        )
        self.dicref_kanji_in_context = Indices(
            self, HEADER_INDICES, 'dicref_kanji_in_context',
            'Kanji in Context',
            LISOs=['jpn'], index_type='Indices'
        )
        self.dicref_kodansha_compact = Indices(
            self, HEADER_INDICES, 'dicref_kodansha_compact',
            'Kodansha Compact Kanji Guide',
            LISOs=['jpn'], index_type='Indices'
        )
        self.dicref_maniette = Indices(
            self, HEADER_INDICES, 'dicref_maniette',
            'Les Kanjis dans la tete',
            LISOs=['jpn'], index_type='Indices'
        )
        self.dicref_moro = Indices(
            self, HEADER_INDICES, 'dicref_moro',
            'Morohashi Daikanwajiten',
            LISOs=['jpn'], index_type='Indices'
        )
        self.dicref_nelson_c = Indices(
            self, HEADER_INDICES, 'dicref_nelson_c',
            'Modern Reader\'s Japanese - English Character Dictionary',
            LISOs=['jpn'], index_type='Indices'
        )
        self.dicref_nelson_n = Indices(
            self, HEADER_INDICES, 'dicref_nelson_n',
            'New Nelson Japanese-English Character Dictionary',
            LISOs=['jpn'], index_type='Indices'
        )
        self.dicref_oneill_kk = Indices(
            self, HEADER_INDICES, 'dicref_oneill_kk',
            'Essential Kanji',
            LISOs=['jpn'], index_type='Indices'
        )
        self.dicref_oneill_names = Indices(
            self, HEADER_INDICES, 'dicref_oneill_names',
            'Japanese Names',
            LISOs=['jpn'], index_type='Indices'
        )
        self.dicref_sakade = Indices(
            self, HEADER_INDICES, 'dicref_sakade',
            'A Guide to Reading and Writing Japanese (Sakade)',
            LISOs=['jpn'], index_type='Indices'
        )
        self.dicref_sh_kk = Indices(
            self, HEADER_INDICES, 'dicref_sh_kk',
            'Kanji and Kana',
            LISOs=['jpn'], index_type='Indices'
        )
        self.dicref_tutt_cards = Indices(
            self, HEADER_INDICES, 'dicref_tutt_cards',
            'Tuttle Kanji Cards',
            LISOs=['jpn'], index_type='Indices'
        )
