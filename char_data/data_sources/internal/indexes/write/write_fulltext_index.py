from unicodedata import normalize

from toolkit.arrays import get_int_array, get_array_by_type
from toolkit.arrays import write_array, write_json
from char_data.misc.process_word import remove_tones
from toolkit.list_operations.rem_dupes import rem_dupes
from toolkit.hashes.fast_hash import fast_hash


def key_to_iso(key):
    key = key.lower()

    if 'ja' in key.split('_'):
        return 'ja'
    elif 'ko' in key.split('_'):
        return 'ko'
    elif 'es' in key.split('_'):
        return 'es'
    elif 'pt' in key.split('_'):
        return 'pt'
    elif 'fr' in key.split('_'):
        return 'fr'
    elif 'canto' in key:
        return None
    elif 'mand' in key:
        return None
    elif 'nanori' in key:
        return 'ja'
    elif 'pinyin' in key:
        return None
    elif 'hangul' in key:
        return 'ko'
    elif 'viet' in key:
        return 'vi'
    elif 'tang' in key:
        return 'ltc'
    else:
        return 'en' # CHECK ME!


def write_fulltext_index(f, key, DData):
    #print 'DJSON:', DJSON
    #print 'DData:', DData
    LISO = ['eng:Latin'] #  FIXME!!!!        DJSON.get('script', 'eng:Latin').split(':')
    inst = FulltextWriter(key, DData, LISO)
    return inst.write(f)


def write_compressed_names_index(f, key, DData, DJSON=None):
    inst = FulltextWriter(key, DData, LISO=None)
    return inst.write(f)


def get_tokens(word):
    """
    Replace various symbols with spaces so that 
    `word` can be more easily indexed
    """
    word = word.strip()
    for char in ',;*.<>()"\'=-:#':
        word = word.replace(char, ' ')
    return word


class FulltextWriter:
    def __init__(self, key, DData, LISO=None):
        """
        For readings in other languages etc where the data isn't in English
        Write the index to disk, using stem
        FIXME: ADD RANGE SUPPORT!
        TODO: REMOVE DUPE WORDS?
        """
        self.key = key
        self.DData = DData
        #self.LISO = LISO
        self.iso = key_to_iso(key)
        print('FulltextWriter ISO:', key, self.iso)
        self.SSpell = set()
        
        L = []
        for ord_ in list(self.DData.keys()):
            value = self.DData.get(ord_, [])
            LValues = value if isinstance(value, (list, tuple)) else [value]
            
            for value in LValues:
                if self.iso and self.iso == 'ltc': # Tang dynasty Chinese
                    L.extend(self.get_L_tang(ord_, value))
                
                elif self.iso:
                    L.extend(self.get_L_inflected(ord_, value))
                    
                else:
                    L.extend(self.get_L_general(ord_, value))
        L.sort()
        
        # Convert to c array types
        LHash = self.LHash = get_int_array(signed=False)
        LOrds = self.LOrds = get_int_array()
        
        for hash_, ord_ in L:
            LHash.append(hash_)
            LOrds.append(ord_)
        
    def write(self, f):
        # And write to disk
        DRtn = {}
        DRtn['LSpell'] = write_json(f, list(self.SSpell))
        DRtn['LHash'] = write_array(f, self.LHash)
        DRtn['LOrds'] = write_array(f, self.LOrds)
        DRtn['deinflect_iso'] = self.iso
        return DRtn
    
    def get_L_inflected(self, ord_, value):        
        LWords = []
        for token in get_tokens(value).split():
            # Add to the spellcheck BEFORE deinflecting!
            token = token.strip().upper()
            if token: 
                self.SSpell.add(token)

            from title_idx.language_support.Stem import get_L_stemmed
            LStemmed = get_L_stemmed(token.strip(), self.iso)
            LWords.extend(LStemmed)
        
        return self.get_L_tokens(ord_, LWords, 
                                 add_to_spellcheck=False)
    
    def get_L_tokens(self, ord_, LWords, add_to_spellcheck=True):
        LRtn = []
        for word in LWords:
            # Convert words to uppercased, decomposed (combining) form
            word = normalize('NFD', str(word))
            word = word.strip().upper()
            
            if not word:
                continue
            
            # Remove codepoint values
            if 'U+' in word:
                #is_codepoint = (
                #    float(int(word.replace('U+', '') or , 16)) ==
                #    float(word.replace('U+', ''))
                #)

                is_codepoint = True
                if is_codepoint:
                    continue
            
            # Add to the spellcheck list
            if add_to_spellcheck:
                no_tones = remove_tones(word)
                if no_tones: 
                    self.SSpell.add(no_tones)
            
            # Add the word itself
            LRtn.append((fast_hash(word), ord_))
        return rem_dupes(LRtn)
    
    def get_L_general(self, ord_, value):
        """
        Index with and without accents/tones/symbols
        etc to make it more likely that searches will 
        find the result the user wanted
        """
        LRtn = []
        for word in value.split():
            """
            Add With and without a 'period' 
            for Japanese (or remove the period?)
            """
            tokens = get_tokens(word.replace('.', ''))
            if not tokens: 
                continue
            
            tokens = normalize('NFD', str(tokens))            
            tokens = remove_tones(tokens)
            LRtn.extend(self.get_L_tokens(ord_, [tokens]))
        return LRtn
    
    def get_L_tang(self, ord_, value):
        LRtn = []
        for word in value.split():
            """
            HACK: Tang dynasty Chinese has * characters 
            etc which are difficult to search by, 
            """
            tokens = get_tokens(word)
            if not tokens: 
                continue
            
            LTokens = [word, 
                       tokens,
                       remove_tones(word),
                       remove_tones(tokens)]
            LRtn.extend(self.get_L_tokens(ord_, LTokens))
        return LRtn
