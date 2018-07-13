from toolkit.arrays.ArrayUtils import read_arrays


class IndicesIndex:
    typ = 'indices'
    
    def __init__(self, f, DJSON):
        # TODO: Allow advanced queries, ranges of pages etc? ========================================
        self.DJSON = DJSON
        _, self.DIndices = read_arrays(f, DJSON)
    
    def keys(self):
        return self.DIndices.keys()
    
    def search(self, search):
        if search in self.DIndices:
            return self.DIndices[search]
        raise KeyError(search)
