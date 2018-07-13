from toolkit.arrays.ArrayUtils import read_arrays


class IntegerKeyIndex:
    typ = 'integer'
    
    def __init__(self, f, DJSON):
        # OPEN ISSUE: Allow browsing ranges? =========================================================
        
        self.DJSON = DJSON
        _, self.DInts = read_arrays(f, DJSON) # TODO: What ranges are there? =======================
    
    def keys(self):
        return self.DInts.keys()
    
    def search(self, search):
        if search in self.DInts:
            return self.DInts[search]
        raise KeyError(search)
