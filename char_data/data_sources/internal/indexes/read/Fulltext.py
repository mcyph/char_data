import heapq
import bisect
#from editdist import distance
from unicodedata import normalize

from toolkit.arrays import read_json, read_array
from toolkit.hashes.fast_hash import fast_hash

from .CharIndexValueInfo import CharIndexValueInfo


class FulltextIndex:
    typ = 'fulltext'
    
    def __init__(self, f, DJSON):
        """
        Provides a basic fulltext index for searching through
        characters.
        
        OPEN ISSUE: Replace me with a Lucene class? ==================================================
        """
        
        # None for no deinflection
        # [ISO, variant] to use with the stemmer
        self.LDeinflect = None #DJSON['LDeinflect'] # FIXME! ====================================
        
        self.LSpell = read_json(f, DJSON['LSpell'])
        self.LHash = read_array(f, DJSON['LHash'])
        self.LOrds = read_array(f, DJSON['LOrds'])
        
    #======================================================#
    #                    Exact Searching                   #
    #======================================================#
    
    def values(self):
        """
        CompressedNames reference by unsigned int hash
        and there can sometimes be too many items, so 
        I've disabled it for now
        """
        return self.LSpell

    def get_value_info(self, value):
        return CharIndexValueInfo(value, value) # CHECK ME!!!
    
    def search(self, search):
        """
        Search for a specific value
        """
        return self.fulltext(search)  #hack

        LSearch = [i.strip().upper() 
                   for i in search.split() 
                   if i.strip()]
        
        SPrev = None
        for search in LSearch:
            SPossible = set()
            self._find(search, SPrev, SPossible)
            
            if not SPossible: 
                raise KeyError(search)
            SPrev = SPossible
        
        for ord_ in SPrev:
            from char_data import char_data
            value = char_data.raw_data(FIXME, search) # FIXME! ==============================
            if value.upper() == search.upper():
                return (ord_,)
        raise KeyError(search)
    
    #======================================================#
    #                  Fulltext Searching                  #
    #======================================================#
    
    def fulltext_keys(self):
        return self.LSpell
    
    def fulltext(self, search):
        """
        Try in each of the words, removing possibilities 
        if there aren't any of that name
        """
        LSearch = [i.strip().upper() 
                   for i in search.split() 
                   if i.strip()]
        
        SPrev = None
        for search in LSearch:
            SPossible = set()
            self._find(SPrev, SPossible, search)
            
            if not SPossible: 
                raise KeyError(search)
            SPrev = SPossible
        
        if not SPossible:
            raise KeyError(search)
        
        LOrds = sorted(SPossible)
        return LOrds
    
    def _find(self, SPrev, SPossible, search):
        LDeinflect = self.LDeinflect
        if LDeinflect:
            from title_idx.language_support.Stem import get_L_stemmed
            search = get_L_stemmed(search.lower(), *LDeinflect)[0].upper()
            #print 'STEMMED SEARCH:', LDeinflect, search.encode('utf-8')
        
        Hash = fast_hash(search)
        pos = bisect.bisect_left(self.LHash, Hash)
        while 1:
            if pos > len(self.LOrds)-1:
                break
            
            elif self.LHash[pos] != Hash:
                break
            
            else:
                # For example, "Latin Small Letter e" will disqualify 
                # names which don't contain "Latin" when looking for "Small"
                ord_ = self.LOrds[pos]
                if SPrev is None or ord_ in SPrev:
                    SPossible.add(ord_)
            pos += 1
    
    #======================================================#
    #                      Spellcheck                      #
    #======================================================#
    
    def spellcheck(self, search):
        """
        Get spellchecked values close to `search`
        
        NOTE: Only works for a single word! ==================================
        """
        search = str(search)
        
        LRtn = []
        for word in self.LSpell:
            if not word[0] == search[0]: 
                continue
            
            LRtn.append((distance(search, word), word))
            
        if not LRtn:
            for word in self.LSpell:
                if not word[-1] == search[-1]: 
                    continue
                
                LRtn.append((distance(search, word), word))
        
        LRtn = [i for i in heapq.nsmallest(10, LRtn)]
        LRtn.sort()
        LRtn = [normalize('NFC', str(i[1].lower())) for i in LRtn]
        #print 'SPELLCHECK:', LRtn
        return LRtn
