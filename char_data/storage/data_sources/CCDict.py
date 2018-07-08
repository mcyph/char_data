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


class CCDict:
    def __init__(self, load_db=True):
        #====================================================================#
        #                            Definitions                             #
        #====================================================================#

        self.big5 = Hex(
            self, HEADER_FIXME, 'Big5', 'Big5',
            LISOs=['yue', 'cmn', 'hak'], index=None
        )
        self.cns11643 = NoFormatStrings(
            self, HEADER_FIXME, 'CNS11643', 'CNS11643',
            LISOs=['yue', 'cmn', 'hak'], index=None
        )
        self.gb = NoFormatStrings(
            self, HEADER_FIXME, 'GB', 'GB',
            LISOs=['yue', 'cmn', 'hak'], index=None
        )
        self.utf8 = NoFormatStrings(
            self, HEADER_FIXME, 'UTF8', 'Word',
            LISOs=['All'], index=None
        )
        self.english = Definition(
            self, HEADER_DEFINITION, 'English', 'Cantonese Definition',
            LISOs=['yue', 'hak'], index=Fulltext
        )

        #====================================================================#
        #                             Readings                               #
        #====================================================================#

        self.cantonese = Definition(
            self, HEADER_READINGS, 'Cantonese', 'Cantonese',
            LISOs=['yue'], index=CompressedNames
        )
        self.hakka = Definition(
            self, HEADER_READINGS, 'Hakka', 'Hakka',
            LISOs=['hak'], index=CompressedNames
        )
        self.mandarin = Definition(
            self, HEADER_READINGS, 'Mandarin', 'Mandarin',
            LISOs=['cmn'], index=CompressedNames
        )

        #====================================================================#
        #                          Total Strokes                             #
        #====================================================================#

        self.totalstrokes = NoFormatStrings(
            self, HEADER_TOTAL_STROKES, 'TotalStrokes', 'TotalStrokes',
            LISOs=['yue', 'hak'], index=None
        )

        #====================================================================#
        #                Kangxi Radical/Additional Strokes                   #
        #====================================================================#

        self.r_s = RadicalStrokes(
            self, HEADER_RADICAL_STROKES, 'R/S', 'Cantonese and Hakka',
            LISOs=['yue', 'hak'], index=RadicalStrokes
        )

        #====================================================================#
        #                           Input Data                               #
        #====================================================================#

        self.cangjie = NoFormatStrings(
            self, HEADER_INPUT, 'Cangjie', 'Cangjie',
            LISOs=['yue', 'hak'], index=StringKeys
        )
        self.fourcorner = NoFormatStrings(
            self, HEADER_INPUT, 'FourCorner', 'FourCorner',
            LISOs=['yue', 'hak'], index=StringKeys
        )
