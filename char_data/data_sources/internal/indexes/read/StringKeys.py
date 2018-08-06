from toolkit.list_operations.rem_dupes import fast_rem_dupes
from toolkit.arrays.ArrayUtils import read_arrays, read_json

from char_data.data_sources.internal.property_formatters.enum.DEnum import DEnum

from CharIndexValueInfo import CharIndexValueInfo


class StringKeyIndex:
    typ = 'string_keys'
    
    def __init__(self, f, DJSON):
        _, self.DStringKeys = read_arrays(f, DJSON['DStringKeys'])
        
        D = self.DRanges = {}
        for from_, to, value in read_json(f, DJSON['LRanges']):
            D.setdefault(value, []).append((from_, to))
    
    def values(self):
        LKeys = list(self.DStringKeys.keys()) + list(self.DRanges.keys())
        LKeys = fast_rem_dupes(LKeys)

        L = []
        for value in LKeys:
            L.append(value)
        return L

    def get_value_info(self, value):
        if self.key in DEnum:
            display_value = DEnum[self.key].get(unicode(value), value)
        else:
            display_value = value

        return CharIndexValueInfo(value, display_value)
    
    def search(self, search):
        # TODO: How will codepoint subdividers be added?
        LRtn = []
        
        if search in self.DStringKeys:
            #print self.DStringKeys
            LRtn.extend([(i, i) for i in self.DStringKeys[search]])
        
        if search in self.DRanges:
            LRtn.extend([(i[0], i) for i in self.DRanges[search]])
        
        if not LRtn: 
            raise KeyError(search)
        
        LRtn.sort()
        LRtn = [i[1] for i in LRtn]
        return LRtn
