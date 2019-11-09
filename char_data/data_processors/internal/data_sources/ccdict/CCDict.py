from char_data.data_processors.internal.property_formatters import (
    Definition, NoFormatStrings, Hex, RadicalStrokes
)
from char_data.data_processors.consts import (
    HEADER_FIXME, HEADER_DEFINITION, HEADER_READINGS,
    HEADER_TOTAL_STROKES, HEADER_RADICAL_STROKES, HEADER_INPUT
)
from char_data.abstract_base_classes.data_sources.InternalSourceBase import InternalSourceBase


class CCDict(InternalSourceBase):
    def __init__(self):
        InternalSourceBase.__init__(self, 'ccdict')

        #====================================================================#
        #                            Definitions                             #
        #====================================================================#

        self.big5 = Hex(
            self, HEADER_FIXME, 'Big5', 'Big5',
            LISOs=['yue', 'cmn', 'hak']
        )
        self.cns11643 = NoFormatStrings(
            self, HEADER_FIXME, 'CNS11643', 'CNS11643',
            LISOs=['yue', 'cmn', 'hak']
        )
        self.gb = NoFormatStrings(
            self, HEADER_FIXME, 'GB', 'GB',
            LISOs=['yue', 'cmn', 'hak']
        )
        self.utf8 = NoFormatStrings(
            self, HEADER_FIXME, 'UTF8', 'Word',
            LISOs=['All']
        )
        self.english = Definition(
            self, HEADER_DEFINITION, 'English', 'Cantonese Definition',
            LISOs=['yue', 'hak'], index_type='Fulltext'
        )

        #====================================================================#
        #                             Readings                               #
        #====================================================================#

        self.cantonese = Definition(
            self, HEADER_READINGS, 'Cantonese', 'Cantonese',
            LISOs=['yue'], index_type='CompressedNames'
        )
        self.hakka = Definition(
            self, HEADER_READINGS, 'Hakka', 'Hakka',
            LISOs=['hak'], index_type='CompressedNames'
        )
        self.mandarin = Definition(
            self, HEADER_READINGS, 'Mandarin', 'Mandarin',
            LISOs=['cmn'], index_type='CompressedNames'
        )

        #====================================================================#
        #                          Total Strokes                             #
        #====================================================================#

        self.totalstrokes = NoFormatStrings(
            self, HEADER_TOTAL_STROKES, 'TotalStrokes', 'TotalStrokes',
            LISOs=['yue', 'hak']
        )

        #====================================================================#
        #                Kangxi Radical/Additional Strokes                   #
        #====================================================================#

        self.r_s = RadicalStrokes(
            self, HEADER_RADICAL_STROKES, 'R/S', 'Cantonese and Hakka',
            LISOs=['yue', 'hak'], index_type='RadicalStrokes'
        )

        #====================================================================#
        #                           Input Data                               #
        #====================================================================#

        self.cangjie = NoFormatStrings(
            self, HEADER_INPUT, 'Cangjie', 'Cangjie',
            LISOs=['yue', 'hak'], index_type='StringKeys'
        )
        self.fourcorner = NoFormatStrings(
            self, HEADER_INPUT, 'FourCorner', 'FourCorner',
            LISOs=['yue', 'hak'], index_type='StringKeys'
        )
