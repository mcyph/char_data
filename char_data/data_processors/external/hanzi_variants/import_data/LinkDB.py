# -*- coding: utf-8 -*-
from toolkit import json_tools
from char_data.toolkit.list_operations.rem_dupes import fast_rem_dupes
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
            LKeys = list(DKeys['DFwd'].keys())
        
        if not LRevKeys: 
            LRevKeys = list(DKeys['DRev'].keys())
        
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
            return ' '.join([str(i) for i in search]).encode('utf-8')
        
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
        
        def recurse(word, o_word, x, typ, return_list, 
                    append='', no_append=False):
            # Get all combinations in key
            len_ = len(word)
            if x == len(word):
                return return_list
            
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
                            return_list.append(None)
                        else: 
                            return_list.append(append+i_L[typ]+word[len(append)+len(i_L[typ]):])
                        
                        recurse(
                            word, o_word, len_, typ, return_list,
                            append=append+i_L[typ],
                            no_append=no_append
                        )
                
                elif o_word[x:len_] in D:
                    # append "None"s if found in the opposite variant
                    for i_L in D[o_word[x:len_]]:
                        return_list.append(None)
                        recurse(
                            word, o_word, len_, typ, return_list,
                            append=append+i_L[typ],
                            no_append=True
                        )
                    
                elif len(slice) == 1:
                    recurse(
                        word, o_word, len_, typ, return_list,
                        append=append+slice,
                        no_append=no_append
                    )
                len_ -= 1
            return return_list
        
        LRtn1 = recurse(LWords[0], LWords[1], 0, 0, []) # Simplified
        LRtn2 = recurse(LWords[1], LWords[0], 0, 1, []) # Traditional
        return_list = []
        for i in range(len(LRtn1)):
            try: 
                return_list.append((LRtn1[i], LRtn2[i]))
            except: 
                print(('LINKDB WARNING: %s' % ' '.join(LWords)))
                return [] # WARNING!
        
        return_list = [i for i in return_list if i[0] != LWords[0] and i[1] != LWords[1]] # WARNING!
        return fast_rem_dupes(return_list)


if __name__ == '__main__':
    def test(simp, trad=None):
        if not trad: 
            trad = simp
        
        print(('Testing:', simp.encode('utf-8'), trad.encode('utf-8')))
        
        for typ, opposite, variant in LinkDB.iter_variants((simp, trad)): # HACK!
            print(('\tVar - %s;'%typ, '%s;'%opposite, ' '.join([str(i) for i in variant]).encode('utf-8')))
        
        for typ, LVariant in LinkDB.get_links((simp, trad)): # HACK!
            simp, trad = LVariant
            print(('\tLnk - %s:'%typ, simp.encode('utf-8'), trad.encode('utf-8')))
    
    test('真是的') # Recommended variant
    test('眞是的') # Other variant
    test('戦争') # Japanese variant
    test('平仮名') # Japanese variant
    test('壌') # Japanese variant
    test('座') # Classifiers
    test('法論功') # Erronous Form
    test('法轮功') # Correct Form
    test('簹') # See Also
    test('盧') # Korean variant
    test('汉字査字法', '漢字査字法') # Multiple Variants (but Should be One)
    test('化學比色法', '化學比色法') # WRONG!
    test('美國獨立戰爭') # Has lots of very rarely used variants - PLEASE FIX ME!
    
    test('剣')
    test('剣', '劍')
    test('剣', '劍')
    test('劍', '剣')
    test('剑', '劍')
