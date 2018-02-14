from char_data.datatypes.read import IntegerList, StringData
from char_data.radicals.Cangjie import DCangjie

class NoFormatStrings(StringData): # WARNING! ============================================================
    def __init__(self, key, f, DJSON):
        StringData.__init__(self, key, f, DJSON)
    
    def formatted(self, ord_):
        # As the name suggests, don't do any processing, just return
        data = self.raw_data(ord_)
        
        if self.key=='Cangjie Input Code' and data:
            # CANGJIE HACK! 
            # TODO: Move to a separate type :-P
            LRtn = []
            for c in data:
                if c in DCangjie:
                    LRtn.append(DCangjie[c][0])
                else: 
                    LRtn.append('?')
            return '%s (%s)' % (data, ''.join(LRtn))
        return data

class NoFormatIntegers(IntegerList):
    def __init__(self, key, f, DJSON):
        IntegerList.__init__(self, key, f, DJSON)
        
    def formatted(self, ord_):
        return self.raw_data(ord_)
