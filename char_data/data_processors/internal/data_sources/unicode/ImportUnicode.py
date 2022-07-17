import warnings

from char_data.data_paths import data_path
from char_data.data_processors.internal.data_sources.misc import get_code_point
from char_data.data_processors.internal.data_sources.misc import open_scsv, uni_open
from char_data.data_processors.internal.data_types.write.write_encoding import get_L_encoding
from char_data.data_processors.internal.data_sources.unicode.nameslist import NamesList
from char_data.data_processors.internal.data_sources.WriteBase import WriteBase, add


class ImportUnicode(WriteBase):
    def __init__(self):
        from char_data.data_processors.internal.data_sources.unicode.UnicodeData import UnicodeData
        WriteBase.__init__(self, UnicodeData())


        # Basic data
        self.unicode_data('UnicodeData.txt')
        self.names_list(data_path('chardata', 'unidata/source/NamesList.txt'))
        
        # Arabic shaping
        self.arabic_shaping('ArabicShaping.txt')
        
        # Normalization/composition
        self.composition_exclusions('CompositionExclusions.txt')
        self.normalization_props('DerivedNormalizationProps.txt')
        self.normalization_corrections('NormalizationCorrections.txt')
        
        # Casing
        self.case_folding('CaseFolding.txt') # Also adds in "Unicode General"
        self.special_casing('SpecialCasing.txt')
        
        for key, path in [
            # Rendering/case folding/display etc
            ('east asian width', 'EastAsianWidth.txt'),
            ('property list', 'PropList.txt'),
                          
            # Derived properties
            ('core properties', 'DerivedCoreProperties.txt'),
            ('age', 'DerivedAge.txt'),
                          
            # Definitions
            ('conscript name', 'UnicodeDataConscript.txt'),
            #('named aliases', 'NameAliases.txt'), # FIXME! ==================================
                          
            # Layout
            ('line break', 'LineBreak.txt'),
            ('joining type', 'extracted/DerivedJoiningType.txt'),
            ('grapheme break', 'auxiliary/GraphemeBreakProperty.txt'),
            ('sentence break', 'auxiliary/SentenceBreakProperty.txt'),
            ('word break', 'auxiliary/WordBreakProperty.txt'),
            ('bidi mirroring', 'BidiMirroring.txt'),

            # Blocks/scripts
            ('block', 'Blocks.txt'),
            ('script', 'Scripts.txt'),
            ('conscript blocks', 'ConscriptBlocks.txt')
        ]:
            self.simple(key, path)
    
    @add
    def simple(self, key, path):
        """
        open a simple semicolon-separated file with two columns
        """
        for ord_, value in open_scsv(path):
            yield key, ord_, value
    
    #=======================================================#
    #                  General Unicode Data                 #
    #=======================================================#
    
    @add
    def unicode_data(self, path):
        for i in self._unicode_data(path):
            yield i
    
    def _unicode_data(self, path):
        """
        Open Unicode Data
        """
        
        # Name (SentenceData)
        f = uni_open(path) # 'UnicodeData.txt'
        
        for line in f:
            # CONSCRIPT HACKS!
            if not line.strip(): 
                continue
            elif '(This position shall not be used)' in line:
                continue
            
            cols_dict = [
                'code value', 
                'name', 
                     
                'general category',
                'canonical combining classes',
                'bidirectional category',
                'character decomposition mapping',
                     
                'decimal digit value',
                'digit value',
                'numeric value',
                     
                'mirrored', 
                'Unicode 1.0 name',
                '10646 comment field', 
                'uppercase', 
                'lowercase', 
                'titlecase'
            ]
            
            for key, value in zip(cols_dict, line.split(';')):
                if key == 'code value':
                    ord_ = int(value, 16)
                    continue
                elif key == 'character decomposition mapping':
                    # HACK: As the NFC/NFD algorithms are too complicated for me 
                    # to program, I've decided to leave this info out
                    continue
                elif not value.strip(): 
                    # ignore blank values
                    continue
                
                yield key, ord_, value
        f.close()
    
    #=======================================================#
    #              Various Other f Handlers              #
    #=======================================================#
    
    @add
    def arabic_shaping(self, path):
        """
        Open Arabic Shaping (StringData)
        """
        for ord_, char_name, typ, group in open_scsv(path):
            # character name is ignored here as it's the same as unicodedata.txt
            yield 'arabic shaping type', ord_, typ
            yield 'arabic shaping group', ord_, group
    
    @add
    def composition_exclusions(self, path):
        """
        Open Composition Exclusions (Boolean)
        """
        for ord_, in open_scsv(path):
            yield 'composition exclusions', ord_, True
    
    @add
    def names_list(self, path):
        """
        Open Names List (the most complicated file)
        I'm mainly interested in alternative character names but 
        I may add alternative block names later if I have time
        """
        
        DInfo = None
        DBlock = None
        DSubBlock = None
        sub_block_yielded = True
        
        for mode, D in NamesList(path):
            if mode == 'information':
                DInfo = D
                #print 'DInfo:', DInfo
            
            elif mode == 'block':
                if not sub_block_yielded:
                    # Subheading etc not used in any codepoints, so
                    # assume it belonged to the entire previous block
                    # while raising a warning (no codepoints were there
                    # to imply a subblock), this only occured once as of
                    # Unicode 6.0.0:
                    #
                    # "This range of 6400 code points is dedicated to private use."
                    warnings.warn('sub block not yielded: %s' % DSubBlock)
                    
                    for i in self._iter_D_sub_block(DSubBlock, (DBlock['from'], DBlock['to'])):
                        yield i
                
                DBlock = D
                DSubBlock = None
                #print 'DBlock:', DBlock
                
                for key, value in list(D.items()):
                    if key in ['block description',
                               'block name']:
                        
                        yield key, (D['from'], D['to']), value
                    elif key in ['codepoint', 'from', 'to', 'has separator']:
                        pass
                    else:
                        raise Exception("unknown block key: %s" % key)
                
            elif mode == 'subblock':
                DSubBlock = D
                sub_block_yielded = False
                #print 'DSubBlock:', DSubBlock
                
            elif mode == 'character':
                #print 'DChar:', D
                
                sub_block_yielded = True
                for i in self._iter_D_sub_block(DSubBlock, D['codepoint']):
                    yield i
                
                for key, value in list(D.items()):
                    if key in ['name',
                               'also called',
                               'formally also called',
                               'see also',
                               'decomposed form',
                               'compatibility mapping',
                               'technical notice',
                               'comments']:
                        
                        yield key, D['codepoint'], value
                    elif key in ['codepoint']:
                        pass
                    else:
                        raise Exception("unknown character key: %s" % key)
    
    def _iter_D_sub_block(self, DSubBlock, ord_):
        """
        Add any messages etc about the current subblock inside the 
        current block to this character if there are any, e.g.
        a sub heading of "Weather and astrological symbols" 
        inside the "U+2600-U+26FF Miscellaneous Symbols" range
        """
        if DSubBlock:
            for key, value in list(DSubBlock.items()):
                if key in ['subblock heading',
                           'subblock technical notice',
                           'subblock see also']:
                    yield key, ord_, value
    
    @add
    def case_folding(self, path):
        """
        Open Case Folding
        """
        for ord_, status, mapping, __ignore__ in open_scsv(path):
            # TODO: Should the properties be added with ord_/mapping reversed?
            yield 'case folding status', ord_, status
            yield 'case folding', ord_, mapping
    
    @add
    def normalization_props(self, path):
        """
        Open Derived Normalization Properties
        """
        
        DProps = {'Full_Composition_Exclusion': ('full composition exclusion', True),
                  'Changes_When_NFKC_Casefolded': ('changes when NFKC casefolded', True),
                  
                  'FC_NFKC': ('FC NFKC closure', None),
                  'NFKC_CF': ('NFKC casefold', None),
                  
                  'NFD_QC': ('NFD quick check', 'N'),
                  'NFC_QC': ('NFC quick check', 'N'),
                  'NFKD_QC': ('NFKD quick check', 'N'),
                  'NFKC_QC': ('NFKC quick check', 'N'),
                  
                  'Expands_On_NFD': ('expands on NFD', True),
                  'Expands_On_NFC': ('expands on NFC', True),
                  'Expands_On_NFKD': ('expands on NFKD', True),
                  'Expands_On_NFKC': ('expands on NFKC', True)}
        
        for L in open_scsv(path):
            property = L[1]
            assert property in DProps, "unknown normalization property %s" % property
            
            if len(L) == 3:
                ord_, property, mapping = L
                yield DProps[property][0], ord_, mapping
            else: 
                ord_, property = L
                conv_property, mapping = DProps[property]
                yield conv_property, ord_, mapping
    
    @add
    def normalization_corrections(self, path):
        """
        Open Normalization Corrections
        """
        for ord_, err_code_point, correct_code_point, unicode_ver in open_scsv(path):
            # TODO: Should the codepoints be corrected?
            err_code_point = get_code_point(err_code_point)
            correct_code_point = get_code_point(correct_code_point)
            
            yield 'normalization corrections errors', ord_, err_code_point
            yield 'normalization corrections corrected', ord_, correct_code_point
            #yield 'normalization corrections Unicode version', ord_, unicode_ver
            
    @add
    def special_casing(self, path):
        """
        Open Special Casing
        """
        for L in open_scsv(path):
            ord_ = L[0]
            
            def get_hex_encoding(i):
                return [i[0] for i in get_L_encoding({}, i)] # HACK!
            
            yield 'special casing lower', ord_, get_hex_encoding(L[1])
            yield 'special casing title', ord_, get_hex_encoding(L[2])
            yield 'special casing upper', ord_, get_hex_encoding(L[3])
            
            if len(L) == 6:
                # TODO: Add info to what this value means, e.g.
                # "az Not_Before_Dot"
                yield 'special casing condition list', ord_, L[4]
    
    #=======================================================#
    #        Enum etc which don't use CodePoints         #
    #=======================================================#
    
    @add
    def property_value_aliases(self, path):
        """
        Open property Value Enum
        """
        DPropValAliases = {}
        for L in open_scsv('PropertyValueAliases.txt'):
            # FIXME: Provide support for L[3] where it exists?
            alias, property, Value = L[0], L[1], L[2]
            if not alias in DPropValAliases:
                DPropValAliases[alias] = {}
            DPropValAliases[alias][property] = Value
    
    @add
    def property_aliases(self, path):
        """
        Open property Enum
        Doesn't use a ord_, so can't be indexed 
        """
        DPropertyAliases = {}
        for ord_, property in open_scsv('PropertyAliases.txt'):
            DPropertyAliases[ord_] = property
    
    #=======================================================#
    #   Files which might be useful but not loaded for now  #
    #=======================================================#
    
    """
    def standardized_variants(self, path):
        # Open Standardized Variants?
        # This uses multiple characters, so I've left this out for now
        pass
    
    def normalization_test(self, path):
        # Normalization Test isn't that useful, so I've left it out
        pass
    
    def named_sequences(self, path):
        # Open Named Sequences
        # This technically is multiple characters, so I've disabled this for now
        f = codecs.open('NamedSequences.txt', 'rb', 'utf-8')
        for line in f:
            line = line.split('#')[0].strip()
            if not line: 
                continue
            
            ord_, property = line.split(';')
            ord_ = get_code_point(ord_.strip())
            DKeys['Named Aliases'][ord_] = property.strip()
        f.close()
    
    # I've decided to fallback to unicodedata for the Hangul 
    # algorithm for now as it's a bit beyond me :-)
    
    def hangul_syllable_type(self, path):
        # Open Hangul Syllable Type?
        pass
    
    def jamo(self, path):
        # Open Jamo?
        pass
    
    def named_sequences_provider(self):
        # Open Named Sequences Provider
        # Technically multiple codepoints, so the below code is broken
        
        for ord_, property in open_scsv('NamedSequencesProv.txt'):
            DKeys['Named Sequences Provider'][ord_] = property
    """

def run():
    ImportUnicode().write(data_path('chardata', 'unidata/output/unidata'))

if __name__ == '__main__':
    run()
