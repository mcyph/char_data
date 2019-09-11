from toolkit.list_operations.rem_dupes import fast_rem_dupes
from toolkit.arrays import read_arrays, read_json

from char_data.data_processors.internal.property_formatters.enum.DEnum import DEnum

from .CharIndexValueInfo import CharIndexValueInfo


def init_me(fn):
    def return_me(self, *args, **kw):
        if not self._initd:
            # This uses a fair amount of resources, so only load on-demand
            # TODO: Rewrite this entirely, to make me more memory-efficient!! ============================================
            self._initd = True

            _, self.DStringKeys = read_arrays(self.f, self.DJSON['DStringKeys'])

            D = self.DRanges = {}
            for from_, to, value in read_json(self.f, self.DJSON['LRanges']):
                if isinstance(value, list):
                    for i_value in value:
                        if isinstance(i_value, str):
                            D.setdefault(i_value, []).append((from_, to))
                else:
                    D.setdefault(value, []).append((from_, to))

        return fn(self, *args, **kw)
    return return_me


class StringKeyIndex:
    typ = 'string_keys'
    
    def __init__(self, f, DJSON):
        self._initd = False
        self.f = f
        self.DJSON = DJSON

    @init_me
    def values(self):
        LKeys = list(self.DStringKeys.keys()) + list(self.DRanges.keys())
        LKeys = fast_rem_dupes(LKeys)

        L = []
        for value in LKeys:
            L.append(value)
        return L

    #@init_me
    def get_value_info(self, value):
        if self.key in DEnum:
            display_value = DEnum[self.key].get(str(value), value)
        else:
            display_value = value

        return CharIndexValueInfo(value, display_value)

    @init_me
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
