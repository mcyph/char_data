from toolkit.arrays.ArrayUtils import read_arrays

from CharIndexValueInfo import CharIndexValueInfo


class IndicesIndex:
    typ = 'indices'
    
    def __init__(self, f, DJSON):
        # TODO: Allow advanced queries, ranges of pages etc? ========================================
        self.DJSON = DJSON
        _, self.DIndices = read_arrays(f, DJSON)
    
    def values(self):
        L = []
        for value in self.DIndices.keys():
            L.append(value)
        return L

    def get_value_info(self, value):
        return CharIndexValueInfo(value, unicode(value))
    
    def search(self, search):
        if search in self.DIndices:
            return self.DIndices[search]
        raise KeyError(search)