# -*- coding: utf-8 -*-
#from Chars.Radicals.MultiRad import DBothChars
from toolkit.encodings.surrogates import w_unichr


class MultiRadicals:
    def raw_data(self, ord_):
        char = w_unichr(ord_)
        
        if char in DBothChars:
            return ' '.join(tuple([i for i in DBothChars[char] if i != u'�']))
        else:
            return None
    
    def formatted(self, ord_):
        # Add multi-radical mappings
        return self.raw_data(ord_) # TODO: Make me more pretty! ==============================
