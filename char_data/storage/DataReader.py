from toolkit.json_tools import load
from toolkit.py_ini import read_D_pyini

from char_data.data_paths import data_path
from char_data.storage.indexes import DIndexReaders


class DataReader:
    LData = [
        ('unicodedata', 'unidata'),
        ('unihan', 'unihan'),
        ('ccdict', 'ccdict'),
        ('kanjidic', 'kanjidic'),
        ('nameslist', 'nameslist')
    ]
    
    #================================================================#
    #                         Read Indexes                           #
    #================================================================#

    def get_D_indexes(self):
        """
        Load the indexes for reverse searching
        """
        D = {}
        for key, path in self.LData:
            D[key.lower()] = self.open_index('%s/output/%s' % (path, path))
        return D

    def open_index(self, path):
        DRtn = {}
        
        DKeys = load(data_path('chardata', path+'-idx.json'))
        DINI = read_D_pyini(data_path('chardata', path.replace('/output/', '/')+'.pyini'))
        #print DINI
        
        with open(data_path('chardata', path+'-idx.bin'), 'r+b') as f:
            for key, DJSON in DKeys.items():
                i_DINI = DINI[key]
                if not 'index' in i_DINI or i_DINI['index'] in (None, 'FIXME'): # HACK!
                    continue
                elif DJSON is None:
                    continue # ???
                
                cls = DIndexReaders[i_DINI['index']]
                assert not key.lower() in DRtn
                #print 'Getting key:', key, DJSON
                DRtn[key.lower()] = cls(f, DJSON)
        
        return DRtn

    #================================================================#
    #                        Read Basic Data                         #
    #================================================================#

    def get_D_data(self):
        """
        Load the basic data instances
        """
        D = self.D = {}
        for key, path in self.LData:
            D[key.lower()] = self.open_data(
                data_path('chardata', '%s/output/%s' % (path, path))
            )
        
        #self.create_combine_insts()
        #self.create_alphabet_insts()
        #self.create_multi_radicals_inst()
        #self.create_normalization_insts()
        #self.create_encoding_insts()
        self.create_hanzi_variants_insts()
        return D

    def open_data(self, path):
        DRtn = {}
        
        DKeys = load(path+'.json')
        DINI = read_D_pyini(path.replace('/output/', '/')+'.pyini')
        #print DINI
        
        with open('%s.bin' % path, 'r+b') as f:
            for key, DJSON in DKeys.items():
                i_DINI = DINI[key]
                cls = getattr(property_formatters, i_DINI['formatter'])
                
                assert not key.lower() in DRtn
                DRtn[key.lower()] = cls(key, f, DJSON)
        
        return DRtn

    def create_hanzi_variants_insts(self):
        D = self.D['hanzi variants'] = {}

        D['japanesesimplified'] = (
            property_formatters.JaSimplified('japanesesimplified')
        )
        D['chinesetraditional'] = (
            property_formatters.JaSimplified('chinesetraditional')
        )

        for key in property_formatters.LHanziVariantKeys:
            D[key.lower()] = property_formatters.CEDictVariants(key)

    #================================================================#
    #                   Create Dynamic Instances                     #
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
DData = data_reader.get_D_data()
DIndexes = data_reader.get_D_indexes()
#print DIndexes
