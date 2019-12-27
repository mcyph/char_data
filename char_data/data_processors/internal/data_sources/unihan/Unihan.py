from char_data.data_processors.internal.property_formatters.enum.BooleanEnum import BooleanEnum
from char_data.data_processors.internal.property_formatters.hex.UnicodeHex import UnicodeHex
from char_data.data_processors.internal.property_formatters.mappings.Frequency import Frequency
from char_data.data_processors.internal.property_formatters.noformat.NoFormatIntegers import NoFormatIntegers
from char_data.data_processors.internal.property_formatters.mappings.Indices import Indices
from char_data.data_processors.internal.property_formatters.definition.Definition import Definition
from char_data.data_processors.internal.property_formatters.noformat.NoFormatStrings import NoFormatStrings
from char_data.data_processors.internal.property_formatters.hex.Hex import Hex
from char_data.data_processors.internal.property_formatters.radicals.RadicalStrokes import RadicalStrokes
from char_data.data_processors.internal.property_formatters.encoding.IRG import IRG

from char_data.data_processors.consts import (
    HEADER_FIXME, HEADER_DEFINITION, HEADER_NUMERIC, HEADER_READINGS,
    HEADER_LANGUAGE_USAGE, HEADER_VARIANTS, HEADER_GRADES_FREQUENCIES,
    HEADER_TOTAL_STROKES, HEADER_RADICAL_STROKES, HEADER_INPUT,
    HEADER_ENCODING, HEADER_INDICES, HEADER_PHONETIC_INDICES,
    HEADER_ADOBE
)
from char_data.abstract_base_classes.data_sources.InternalSourceBase import InternalSourceBase


class Unihan(InternalSourceBase):
    def __init__(self, char_data):
        InternalSourceBase.__init__(self, char_data, 'unihan')

        #====================================================================#
        #                            Definitions                             #
        #====================================================================#

        self.cheungbauer = Definition(
            self, HEADER_FIXME, 'CheungBauer', 'Cheung Bauer Data',
            LISOs=['yue']
        )
        self.fenn = Definition(
            self, HEADER_FIXME, 'Fenn', 'Fenn Dictionary Phonetic/Frequency Data',
            LISOs=['yue', 'cmn']
        )
        self.hdzradbreak = Definition(
            self, HEADER_FIXME, 'HDZRadBreak', 'HDZRadBreak'
        )
        self.definition = Definition(
            self, HEADER_DEFINITION, 'Definition', 'Chinese Definition',
            LISOs=['cmn', 'yue', 'kor', 'vie', 'ltc'], index_type='Fulltext'
        )

        #====================================================================#
        #                             Numeric                                #
        #====================================================================#

        self.accountingnumeric = NoFormatStrings(
            self, HEADER_NUMERIC, 'AccountingNumeric', 'Accounting Numeric',
            index_type='IntegerKeys'
        )
        self.othernumeric = NoFormatStrings(
            self, HEADER_NUMERIC, 'OtherNumeric', 'Other Numeric',
            index_type='IntegerKeys'
        )
        self.primarynumeric = NoFormatStrings(
            self, HEADER_NUMERIC, 'PrimaryNumeric', 'Primary Numeric',
            index_type='IntegerKeys'
        )

        #====================================================================#
        #                             Readings                               #
        #====================================================================#

        self.cantonese = Definition(
            self, HEADER_READINGS, 'Cantonese', 'Cantonese Readings',
            LISOs=['yue'], index_type='CompressedNames'
        )
        self.hangul = Definition(
            self, HEADER_READINGS, 'Hangul', 'Hangul Readings',
            LISOs=['kor'], index_type='CompressedNames'
        )
        self.hanyupinlu = Definition(
            self, HEADER_READINGS, 'HanyuPinlu', 'Xiandai Hanyu Pinlu',
            LISOs=['cmn'], index_type='CompressedNames'
        )
        self.hanyupinyin = Definition(
            self, HEADER_READINGS, 'HanyuPinyin', 'Hanyu Pinyin',
            LISOs=['cmn'], index_type='CompressedNames'
        )
        self.japanesekun = Definition(
            self, HEADER_READINGS, 'JapaneseKun', 'JapaneseKun',
            LISOs=['jpn'], index_type='CompressedNames'
        )
        self.japaneseon = Definition(
            self, HEADER_READINGS, 'JapaneseOn', 'JapaneseOn',
            LISOs=['jpn'], index_type='CompressedNames'
        )
        self.korean = Definition(
            self, HEADER_READINGS, 'Korean', 'Korean',
            LISOs=['kor'], index_type='CompressedNames'
        )
        self.mandarin = Definition(
            self, HEADER_READINGS, 'Mandarin', 'Mandarin',
            LISOs=['cmn'], index_type='CompressedNames'
        )
        self.tang = Definition(
            self, HEADER_READINGS, 'Tang', 'Tang',
            LISOs=['ltc'], index_type='CompressedNames'
        )
        self.vietnamese = Definition(
            self, HEADER_READINGS, 'Vietnamese', 'Vietnamese',
            LISOs=['vie'], index_type='CompressedNames'
        )
        self.xhc1983 = Definition(
            self, HEADER_READINGS, 'XHC1983', 'XHC Mandarin Readings',
            LISOs=['cmn'], index_type='CompressedNames'
        )

        #====================================================================#
        #                        Language Usage Data                         #
        #====================================================================#

        self.irg_gsource = IRG(
            self, HEADER_LANGUAGE_USAGE, 'IRG_GSource', 'PRC and Singapore',
            LISOs=['yue', 'cmn']
        )
        self.irg_hsource = IRG(
            self, HEADER_LANGUAGE_USAGE, 'IRG_HSource', 'Hong Kong',
            LISOs=['yue', 'cmn']
        )
        self.irg_jsource = IRG(
            self, HEADER_LANGUAGE_USAGE, 'IRG_JSource', 'Japan',
            LISOs=['jpn']
        )
        self.irg_kpsource = IRG(
            self, HEADER_LANGUAGE_USAGE, 'IRG_KPSource', 'North Korea',
            LISOs=['kor']
        )
        self.irg_ksource = IRG(
            self, HEADER_LANGUAGE_USAGE, 'IRG_KSource', 'South Korea',
            LISOs=['kor']
        )
        self.irg_msource = IRG(
            self, HEADER_LANGUAGE_USAGE, 'IRG_MSource', 'Macau',
            LISOs=['yue', 'cmn']
        )
        self.irg_tsource = IRG(
            self, HEADER_LANGUAGE_USAGE, 'IRG_TSource', 'Taiwan',
            LISOs=['yue', 'cmn']
        )
        self.irg_usource = IRG(
            self, HEADER_LANGUAGE_USAGE, 'IRG_USource', 'Compatibility Ideographs',
            LISOs=['jpn', 'cmn', 'yue', 'kor', 'vie', 'ltc']
        )
        self.irg_vsource = IRG(
            self, HEADER_LANGUAGE_USAGE, 'IRG_VSource', 'Vietnam',
            LISOs=['vie']
        )
        self.irgdaejaweon = IRG(
            self, HEADER_LANGUAGE_USAGE, 'IRGDaeJaweon', 'IRGDaeJaweon',
            LISOs=['kor']
        )
        self.irgdaikanwaziten = IRG(
            self, HEADER_LANGUAGE_USAGE, 'IRGDaiKanwaZiten', 'IRGDaiKanwaZiten',
            LISOs=['yue', 'cmn']
        )
        self.irghanyudazidian = IRG(
            self, HEADER_LANGUAGE_USAGE, 'IRGHanyuDaZidian', 'IRGHanyuDaZidian',
            LISOs=['yue', 'cmn']
        )
        self.irgkangxi = IRG(
            self, HEADER_LANGUAGE_USAGE, 'IRGKangXi', 'IRGKangXi',
            
        )

        #====================================================================#
        #                              Variants                              #
        #====================================================================#

        self.compatibilityvariant = UnicodeHex(
            self, HEADER_VARIANTS, 'CompatibilityVariant', 'Compatibility Variant'
        )
        self.semanticvariant = UnicodeHex(
            self, HEADER_VARIANTS, 'SemanticVariant', 'Semantic Variant'
        )
        self.simplifiedvariant = UnicodeHex(
            self, HEADER_VARIANTS, 'SimplifiedVariant', 'Simplified Variant'
        )
        self.specializedsemanticvariant = UnicodeHex(
            self, HEADER_VARIANTS, 'SpecializedSemanticVariant', 'Specialized Semantic Variant'
        )
        self.traditionalvariant = UnicodeHex(
            self, HEADER_VARIANTS, 'TraditionalVariant', 'Traditional Variant'
        )
        self.zvariant = UnicodeHex(
            self, HEADER_VARIANTS, 'ZVariant', 'Z Variant'
        )

        #====================================================================#
        #                         Grades/Frequencies                         #
        #====================================================================#

        self.frequency = Frequency(
            self, HEADER_GRADES_FREQUENCIES, 'Frequency', 'Chinese Frequency',
            LISOs=['cmn', 'yue', 'kor', 'vie', 'ltc'], index_type='IntegerKeys'
        )
        self.gradelevel = Frequency(
            self, HEADER_GRADES_FREQUENCIES, 'GradeLevel', 'Hong Kong Grade',
            LISOs=['cmn', 'yue', 'kor', 'vie', 'ltc'], index_type='IntegerKeys'
        )
        self.iicore = BooleanEnum(
            self, HEADER_GRADES_FREQUENCIES, 'IICore', 'IICore',
            index_type='IntegerKeys'
        )

        #====================================================================#
        #                          Total Strokes                             #
        #====================================================================#

        self.totalstrokes = NoFormatIntegers(
            self, HEADER_TOTAL_STROKES, 'TotalStrokes', 'Chinese Strokes',
            index_type='IntegerKeys'
        )

        #====================================================================#
        #                Kangxi Radical/Additional Strokes                   #
        #====================================================================#

        self.rsjapanese = RadicalStrokes(
            self, HEADER_RADICAL_STROKES, 'RSJapanese', 'Japanese',
            LISOs=['jpn'], index_type='RadicalStrokes'
        )
        self.rskangxi = RadicalStrokes(
            self, HEADER_RADICAL_STROKES, 'RSKangXi', 'KangXi RS',
            index_type='RadicalStrokes'
        )
        self.rskanwa = RadicalStrokes(
            self, HEADER_RADICAL_STROKES, 'RSKanWa', 'KanWa RS',
            LISOs=['jpn'], index_type='RadicalStrokes'
        )
        self.rskorean = RadicalStrokes(
            self, HEADER_RADICAL_STROKES, 'RSKorean', 'Korean RS',
            LISOs=['kor'], index_type='RadicalStrokes'
        )
        self.rsunicode = RadicalStrokes(
            self, HEADER_RADICAL_STROKES, 'RSUnicode', 'Unicode RS',
            index_type='RadicalStrokes'
        )

        #====================================================================#
        #                           Input Data                               #
        #====================================================================#

        self.cangjie = NoFormatStrings(
            self, HEADER_INPUT, 'Cangjie', 'Cangjie Input Code',
            LISOs=['cmn', 'yue', 'kor', 'vie', 'ltc'], index_type='StringKeys'
        )
        self.fourcornercode = NoFormatStrings(
            self, HEADER_INPUT, 'FourCornerCode', 'Four Corner Input Code',
            LISOs=['cmn', 'yue', 'kor', 'vie', 'ltc'], index_type='StringKeys'
        )

        #====================================================================#
        #                            Encoding                                #
        #====================================================================#

        self.bigfive = Hex(
            self, HEADER_ENCODING, 'BigFive', 'Big Five',
            LISOs=['cmn', 'yue']
        )
        self.cccii = Hex(
            self, HEADER_ENCODING, 'CCCII', 'CCCII',
            LISOs=['cmn', 'yue']
        )
        self.cns1986 = Definition(
            self, HEADER_ENCODING, 'CNS1986', 'CNS 11643-1986',
            LISOs=['cmn', 'yue']
        )
        self.cns1992 = Definition(
            self, HEADER_ENCODING, 'CNS1992', 'CNS 11643-1992',
            LISOs=['cmn', 'yue']
        )
        self.eacc = Hex(
            self, HEADER_ENCODING, 'EACC', 'EACC',
            LISOs=['cmn', 'yue']
        )
        self.gb0 = Hex(
            self, HEADER_ENCODING, 'GB0', 'GB 2312-80',
            LISOs=['cmn', 'yue']
        )
        self.gb1 = Hex(
            self, HEADER_ENCODING, 'GB1', 'GB 12345-90',
            LISOs=['cmn', 'yue']
        )
        self.gb3 = Hex(
            self, HEADER_ENCODING, 'GB3', 'GB 7589-87',
            LISOs=['cmn', 'yue']
        )
        self.gb5 = Hex(
            self, HEADER_ENCODING, 'GB5', 'GB 7590-87',
            LISOs=['cmn', 'yue']
        )
        self.gb7 = Hex(
            self, HEADER_ENCODING, 'GB7', 'GB 8565-89 [1]',
            LISOs=['cmn', 'yue']
        )
        self.gb8 = Hex(
            self, HEADER_ENCODING, 'GB8', 'GB 8565-89 [2]',
            LISOs=['cmn', 'yue']
        )
        self.hkscs = Hex(
            self, HEADER_ENCODING, 'HKSCS', 'HKSCS',
            LISOs=['cmn', 'yue']
        )
        self.ibmjapan = Hex(
            self, HEADER_ENCODING, 'IBMJapan', 'IBMJapan',
            LISOs=['jpn']
        )
        self.jis0 = Hex(
            self, HEADER_ENCODING, 'Jis0', 'JIS X 0208-1990',
            LISOs=['jpn']
        )
        self.jis0213 = Definition(
            self, HEADER_ENCODING, 'JIS0213', 'JIS0213',
            LISOs=['jpn']
        )
        self.jis1 = Hex(
            self, HEADER_ENCODING, 'Jis1', 'Jis1',
            LISOs=['jpn']
        )
        self.kps0 = Hex(
            self, HEADER_ENCODING, 'KPS0', 'KPS 9566-97',
            LISOs=['jpn']
        )
        self.kps1 = Hex(
            self, HEADER_ENCODING, 'KPS1', 'KPS 10721-2000',
            LISOs=['kor']
        )
        self.ksc0 = Hex(
            self, HEADER_ENCODING, 'KSC0', 'KS X 1001:1992 (KS C 5601-1989)',
            LISOs=['kor']
        )
        self.ksc1 = Hex(
            self, HEADER_ENCODING, 'KSC1', 'KS X 1002:1991 (KS C 5657-1991)',
            LISOs=['kor']
        )
        self.mainlandtelegraph = Hex(
            self, HEADER_ENCODING, 'MainlandTelegraph', 'MainlandTelegraph',
            LISOs=['cmn', 'yue']
        )
        self.pseudogb1 = Hex(
            self, HEADER_ENCODING, 'PseudoGB1', 'PseudoGB1',
            LISOs=['cmn', 'yue']
        )
        self.taiwantelegraph = Hex(
            self, HEADER_ENCODING, 'TaiwanTelegraph', 'TaiwanTelegraph',
            LISOs=['cmn', 'yue']
        )
        self.xerox = Definition(
            self, HEADER_ENCODING, 'Xerox', 'Xerox',
            LISOs=['cmn', 'yue', 'kor', 'vie', 'ltc']
        )

        #====================================================================#
        #                             Indices                                #
        #====================================================================#

        self.cheungbauerindex = Indices(
            self, HEADER_INDICES, 'CheungBauerIndex', 'Cheung Bauer',
            LISOs=['yue'], index_type='Indices'
        )
        self.cihait = Indices(
            self, HEADER_INDICES, 'CihaiT', 'Cihai',
            LISOs=['yue'], index_type='Indices'
        )
        self.cowles = Indices(
            self, HEADER_INDICES, 'Cowles', 'Cowles',
            LISOs=['yue'], index_type='Indices'
        )
        self.daejaweon = Indices(
            self, HEADER_INDICES, 'DaeJaweon', 'Dae Jaweon',
            LISOs=['kor'], index_type='Indices'
        )
        self.fennindex = Indices(
            self, HEADER_INDICES, 'FennIndex', 'Fenn Dictionary',
            LISOs=['cmn'], index_type='Indices'
        )
        self.gsr = Indices(
            self, HEADER_INDICES, 'GSR', 'Grammata Serica Recensa',
            LISOs=['cmn', 'yue', 'jpn'], index_type='Indices'
        )
        self.hanyu = Indices(
            self, HEADER_INDICES, 'HanYu', 'Hanyu Da Zidian',
            index_type='Indices'
        )
        self.hkglyph = Indices(
            self, HEADER_INDICES, 'HKGlyph', 'HKGlyph',
            LISOs=['yue'], index_type='Indices'
        )
        self.kangxi = Indices(
            self, HEADER_INDICES, 'KangXi', 'KangXi',
            LISOs=['cmn', 'yue', 'kor', 'vie', 'ltc'], index_type='Indices'
        )
        self.karlgren = Indices(
            self, HEADER_INDICES, 'Karlgren', 'Karlgren',
            LISOs=['jpn'], index_type='Indices'
        )
        self.lau = Indices(
            self, HEADER_INDICES, 'Lau', 'Lau',
            LISOs=['yue'], index_type='Indices'
        )
        self.matthews = Indices(
            self, HEADER_INDICES, 'Matthews', 'Matthews',
            LISOs=['yue', 'cmn'], index_type='Indices'
        )
        self.meyerwempe = Indices(
            self, HEADER_INDICES, 'MeyerWempe', 'Meyer Wempe',
            LISOs=['yue'], index_type='Indices'
        )
        self.morohashi = Indices(
            self, HEADER_INDICES, 'Morohashi', 'Morohashi',
            LISOs=['jpn'], index_type='Indices'
        )
        self.nelson = Indices(
            self, HEADER_INDICES, 'Nelson', 'Nelson',
            LISOs=['jpn'], index_type='Indices'
        )
        self.sbgy = Indices(
            self, HEADER_INDICES, 'SBGY', 'Song Ben Guang Yun',
            LISOs=['yue', 'cmn', 'ltc'], index_type='Indices'
        )

        #====================================================================#
        #                        Phonetic Indices                            #
        #====================================================================#

        self.phonetic = NoFormatStrings(
            self, HEADER_PHONETIC_INDICES, 'Phonetic', 'Phonetic',
            LISOs=['yue'], index_type='StringKeys'
        )

        #====================================================================#
        #                             Adobe                                  #
        #====================================================================#

        self.rsadobe_japan1_6 = Definition(
            self, HEADER_ADOBE, 'RSAdobe_Japan1_6', 'RSAdobe_Japan1_6',
            LISOs=['jpn']
        )

