# -*- coding: utf-8 -*-
from sys import maxint

#from char_data.radicals.DataRadicals import DBothChars, DBothRads
from toolkit.encodings.surrogates import w_unichr


class SimilarHanzi:
    def __init__(self, iso, script):
        self.iso = iso
        self.script = script
    
    def raw_data(self, ord_):
        """
        Return similar Hanzi/Kanji etc characters 
        using the MultiRadicals database
        """
        from char_data import char_data
        char = w_unichr(ord_)
        
        if char in DBothChars:
            LRads = self.get_rads(char)
            LNumStrokes = char_data.raw_data('unihan.totalstrokes', ord_) or []
            #print LNumStrokes
            
            L = []
            SAdded = set()
            
            for rad in LRads:
                for i_ord in DBothRads[rad]:
                    if char == w_unichr(i_ord) and True:
                        continue
                    elif i_ord in SAdded:
                        continue
                    
                    SAdded.add(i_ord)
                    L.append(self._get_cmp_value(LRads, LNumStrokes, i_ord))
            L.sort()
            
            return [i[-1] for i in L]
        else:
            return None
    
    def _get_cmp_value(self, LRads, LNumStrokes, ord_):
        i_LRads = self.get_rads(w_unichr(ord_))
        
        # Get the number of multiradicals which are 
        # different between the current character and radical
        num_same = len([i for i in i_LRads if i in LRads])
        
        # Get the difference in number of strokes. If there are 
        # multiple stroke counts for either character, then choose 
        # the smallest difference
        stroke_diff = maxint
        
        #print unichr(ord_), char_data.raw_data('unihan.totalstrokes', ord_)
        for num_strokes in char_data.raw_data('unihan.totalstrokes', ord_) or []:
            for i_num_strokes in LNumStrokes:
                x = abs(i_num_strokes-num_strokes)
                
                if x < stroke_diff:
                    stroke_diff = x
        
        # TODO: Get the frequency depending on language! ==========================================
        LFreqs = []
        for key in ('unihan.frequency', 'kanjidic.freq'):
            freq = char_data.raw_data(key, ord_)
            freq = freq[0] if freq else maxint
            LFreqs.append(freq)
        
        return (
            -num_same,
            stroke_diff,
            LFreqs,
            ord_
        )
    
    def get_rads(self, char):
        return [i for i in DBothChars[char] if i != u'�'] # HACK!
    
    def formatted(self, ord_):
        return ' '.join(w_unichr(i_ord) for i_ord in self.char_data.raw_data(ord_))
