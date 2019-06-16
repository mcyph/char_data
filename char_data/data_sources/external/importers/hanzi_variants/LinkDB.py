# -*- coding: utf-8 -*-
from toolkit import json_tools
from toolkit.list_operations.rem_dupes import fast_rem_dupes
from dicts.misc.ExpandTree import open
from dicts.japanese.JSimplified import trad_to_simp


class LinkDB:
    def __init__(self, path, LKeys=None, LRevKeys=None):
        self.path = path
        #self.TransInst = TransInst  # For Hanzi->Pinyin
                                    # Hanzi->Jyutping
                                    # Hanzi->Hakka
        
        # Load the data
        with open(path, 'rb') as f:
            DKeys = json_tools.loads(
                f.read().decode('utf-8')
            ) # WARNING!
        
        # Assign LKeys/LRevKeys (Defaulting if not supplied)
        if not LKeys: 
            LKeys = DKeys['DFwd'].keys()
        
        if not LRevKeys: 
            LRevKeys = DKeys['DRev'].keys()
        
        self.LKeys = LKeys
        self.LRevKeys = LRevKeys
        
        # Assign DFwd/DRevSimp/DRevTrad
        self.DFwd = DKeys['DFwd']
        self.DRev = DKeys['DRev']


    #========================================================================#
    #                            Get Exact Links                             #
    #========================================================================#


    def get_links(self, LWords):
        for key in self.LKeys:
            if key in LIgnoreInTypes:
                continue # HACK!
            D = self.DFwd[key]
            
            _, trad = LWords
            if trad in D:
                for i in D[trad]:
                    yield DDispAs[key][1], tuple(i)
        
        for key in self.LRevKeys:
            if key in LIgnoreInTypes:
                continue # HACK!
            D = self.DRev[key]
            
            _, trad = LWords
            if trad in D:
                for i in D[trad]:
                    yield DDispAs[key][2], tuple(i)


    #========================================================================#
    #                              Get Variants                              #
    #========================================================================#


    # NOTE: Variants are words which have the 
    # same length and readings but different Hanzi
    
    def iter_variants(self, LWords):
        # Yields (FwdExplanation, RevExplanation, variant)
        # Where the forward explanation might be "Chinese variant"
        # and the reverse explanation might be "Japanese variant"
        def print_(search):
            return ' '.join([unicode(i) for i in search]).encode('utf-8')
        
        LWords = tuple(LWords)
        for key in self.LKeys:
            if not DDispAs[key][0]: 
                continue
            
            # HACK: Convert Japanese 氣 -> 気 etc
            for search in self._iter_variants(self.DFwd[key], LWords):
                if key == 'DJVariants':
                    if not search[1]: 
                        continue # HACK!
                    
                    search = (search[0], search[1]) # HACK!
                    
                    if search[1] == LWords[1]: 
                        continue
                
                #print '1 YIELD:', print_(search)
                yield DDispAs[key][1], DDispAs[key][2], search
            
            if key == 'DJVariants': # FIXME!
                LYield = (None, LWords[1])
                if LYield[1] != LWords[1]:
                    #print '2 YIELD:', print_(LYield)
                    yield DDispAs[key][1], DDispAs[key][2], LYield
        
        for key in self.LRevKeys:
            if not DDispAs[key][0]: 
                continue
            
            # HACK: Convert Japanese 気 -> 氣 etc
            for search in self._iter_variants(self.DRev[key], LWords):
                if key == 'DJVariants':
                    if not search[1]: 
                        continue # HACK!
                    
                    search = (None, trad_to_simp(search[1])) # HACK!
                    
                    if search[1] == LWords[1]: 
                        continue
                
                #print '3 YIELD:', print_(search)
                yield DDispAs[key][2], DDispAs[key][1], search
            
            if key == 'DJVariants': # FIXME!
                LYield = (None, trad_to_simp(LWords[1]))
                if LYield[1] != LWords[1]:
                    #print '4 YIELD:', print_(LYield)
                    yield DDispAs[key][2], DDispAs[key][1], LYield


    def _iter_variants(self, D, LWords):
        #print ' '.join(LWords)
        
        def recurse(word, o_word, x, typ, LRtn, 
                    append='', no_append=False):
            # Get all combinations in key
            len_ = len(word)
            if x == len(word):
                return LRtn
            
            while 1:
                if len_ == x: 
                    break
                
                slice = word[x:len_]
                if not slice: 
                    break
                
                if slice in D:
                    for i_L in D[slice]:
                        # TODO: What about REVERSE SIMPLIFIED variants?
                        if no_append: 
                            LRtn.append(None)
                        else: 
                            LRtn.append(append+i_L[typ]+word[len(append)+len(i_L[typ]):])
                        
                        recurse(
                            word, o_word, len_, typ, LRtn,
                            append=append+i_L[typ],
                            no_append=no_append
                        )
                
                elif o_word[x:len_] in D:
                    # append "None"s if found in the opposite variant
                    for i_L in D[o_word[x:len_]]:
                        LRtn.append(None)
                        recurse(
                            word, o_word, len_, typ, LRtn,
                            append=append+i_L[typ],
                            no_append=True
                        )
                    
                elif len(slice) == 1:
                    recurse(
                        word, o_word, len_, typ, LRtn,
                        append=append+slice,
                        no_append=no_append
                    )
                len_ -= 1
            return LRtn
        
        LRtn1 = recurse(LWords[0], LWords[1], 0, 0, []) # Simplified
        LRtn2 = recurse(LWords[1], LWords[0], 0, 1, []) # Traditional
        LRtn = []
        for i in xrange(len(LRtn1)):
            try: 
                LRtn.append((LRtn1[i], LRtn2[i]))
            except: 
                print('LINKDB WARNING: %s' % ' '.join(LWords))
                return [] # WARNING!
        
        LRtn = [i for i in LRtn if i[0] != LWords[0] and i[1] != LWords[1]] # WARNING!
        return fast_rem_dupes(LRtn)


if __name__ == '__main__':
    def test(simp, trad=None):
        if not trad: 
            trad = simp
        
        print('Testing:', simp.encode('utf-8'), trad.encode('utf-8'))
        
        for typ, opposite, variant in LinkDB.iter_variants((simp, trad)): # HACK!
            print('\tVar - %s;'%typ, '%s;'%opposite, ' '.join([unicode(i) for i in variant]).encode('utf-8'))
        
        for typ, LVariant in LinkDB.get_links((simp, trad)): # HACK!
            simp, trad = LVariant
            print('\tLnk - %s:'%typ, simp.encode('utf-8'), trad.encode('utf-8'))
    
    test(u'真是的') # Recommended variant
    test(u'眞是的') # Other variant
    test(u'戦争') # Japanese variant
    test(u'平仮名') # Japanese variant
    test(u'壌') # Japanese variant
    test(u'座') # Classifiers
    test(u'法論功') # Erronous Form
    test(u'法轮功') # Correct Form
    test(u'簹') # See Also
    test(u'盧') # Korean variant
    test(u'汉字査字法', u'漢字査字法') # Multiple Variants (but Should be One)
    test(u'化學比色法', u'化學比色法') # WRONG!
    test(u'美國獨立戰爭') # Has lots of very rarely used variants - PLEASE FIX ME!
    
    test(u'剣')
    test(u'剣', u'劍')
    test(u'剣', u'劍')
    test(u'劍', u'剣')
    test(u'剑', u'劍')
