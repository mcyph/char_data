from toolkit.json_tools import load
from toolkit.py_ini import read_D_pyini

from char_data.data_paths import data_path
from char_data.storage.indexes import DIndexReaders

from internal_data_sources import CCDict, Kanjidic, UnicodeData, Unihan
from get_key_name import get_key_name


class DataReader:
    LData = [
        ('unicodedata', 'unidata'),
        ('unihan', 'unihan'),
        ('ccdict', 'ccdict'),
        ('kanjidic', 'kanjidic'),
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


        #self.create_combine_insts()
        #self.create_alphabet_insts()
        #self.create_multi_radicals_inst()
        #self.create_normalization_insts()
        #self.create_encoding_insts()
        #self.create_hanzi_variants_insts()

    def create_hanzi_variants_insts(self):
        D = self.D['hanzi_variants'] = {}

        D['japanesesimplified'] = (
            property_formatters.JaSimplified('japanesesimplified')
        )
        D['chinesetraditional'] = (
            property_formatters.JaSimplified('chinesetraditional')
        )

        for key in property_formatters.LHanziVariantKeys:
            D[key.lower().replace(' ', '_')] = property_formatters.CEDictVariants(key)

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


from char_data.formatters import property_formatters

data_reader = DataReader()
