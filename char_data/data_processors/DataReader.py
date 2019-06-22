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

        #('nameslist', 'nameslist')
    ]

    #================================================================#
    #                        Read Basic Data                         #
    #================================================================#

    def __init__(self):
        """
        Load the basic data instances
        """
        self.ccdict = CCDict()
        self.kanjidic = Kanjidic()
        self.unicodedata = UnicodeData()
        self.unihan = Unihan()

        self.hanzi_variants = HanziVariants()
        self.standard_encodings = StandardEncodings()
        self.reformatted = ReformattedData()
        self.cldr_alphabets = Alphabets()

        #self.create_combine_insts()
        #self.create_alphabet_insts()
        #self.create_multi_radicals_inst()
        #self.create_normalization_insts()
        #self.create_encoding_insts()

    #================================================================#
    #                 Create Dynamic Data Instances                  #
    #================================================================#

    def create_combine_insts(self):
        """
        Create the "combine" instances, which take the character data 
        and combine from multiple sources into a single item.
        """
        
        # TODO: Create the DefinitionCombine instances
        DDefs = self.D['definitions'] = {}
        for iso in FIXME:
            DDefs[iso] = property_formatters.DefinitionCombine(LKeys)
        
        # TODO: Create the ReadingsCombine instances
        DReadings = self.D['readings'] = {}
        for iso in FIXME:
            DReadings[iso] = property_formatters.ReadingsCombine(FIXME)
        
        # TODO: Create the RSCombine instances
        DRS = D['rs'] = {}
        for FIXME in FIXME:
            DRS[FIXME] = FIXME

    def create_alphabet_insts(self):
        # TODO: Create the Alphabets instance
        DOther = self.D.setdefault('other', {})
        DOther['alphabets'] = property_formatters.Alphabets(FIXME)
        
        # TODO: Create the Casing instances
        DOther['lowercased form'] = property_formatters.Casing(FIXME)
        DOther['uppercased form'] = property_formatters.Casing(FIXME)
        
        # TODO: Create the Translit instances
        DOther['transliteration mappings'] = property_formatters.Translit(FIXME)

    def create_encoding_insts(self):
        # TODO: Create the Encodings instances
        DEncs = self.D['encodings'] = {}
        for encoding in FIXME:
            DEncs[encoding] = property_formatters.Encodings(encoding)

    def create_multi_radicals_inst(self):
        # TODO: Create the MultiRadicals instance [???]
        DOther = self.D.setdefault('other', {})
        DOther['multi radicals'] = property_formatters.MultiRadicals(FIXME)

    def create_normalization_insts(self):
        # TODO: Create the Normalization instances
        DOther = self.D.setdefault('other', {})
        DOther['nfd normalization'] = property_formatters.Normalization('NFD')
        DOther['nfkd normalization'] = property_formatters.Normalization('NFKD')


from char_data.data_processors.internal import property_formatters

