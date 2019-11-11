from char_data.data_processors.internal import CCDict, Kanjidic, UnicodeData, Unihan
from char_data.data_processors.external.hanzi_variants.HanziVariants import HanziVariants
from char_data.data_processors.external.encoding.StandardEncodings import StandardEncodings
from char_data.data_processors.external.reformatters.ReformattedData import ReformattedData
from char_data.data_processors.external.alphabets.Alphabets import Alphabets


class DataReader:
    LData = [
        # Internal sources
        ('unicodedata', 'unidata'),
        ('unihan', 'unihan'),
        ('ccdict', 'ccdict'),
        ('kanjidic', 'kanjidic'),

        # External sources
        ('hanzi_variants', 'hanzi_variants'),
        ('standard_encodings', 'standard_encodings'),
        ('reformatted', 'reformatted'),
        ('cldr_alphabets', 'cldr_alphabets'),
    ]

    #================================================================#
    #                        Read Basic Data                         #
    #================================================================#

    def __init__(self):
        """
        Load the basic data instances
        """
        self.ccdict = CCDict(self)
        self.kanjidic = Kanjidic(self)
        self.unicodedata = UnicodeData(self)
        self.unihan = Unihan(self)

        self.hanzi_variants = HanziVariants(self)
        self.standard_encodings = StandardEncodings(self)
        self.reformatted = ReformattedData(self)
        self.cldr_alphabets = Alphabets(self)

