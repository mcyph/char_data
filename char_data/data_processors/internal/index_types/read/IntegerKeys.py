from toolkit.arrays import read_arrays

from char_data.CharIndexValueInfo import CharIndexValueInfo


class IntegerKeyIndex:
    typ = 'integer'
    
    def __init__(self, f, DJSON):
        # OPEN ISSUE: Allow browsing ranges? =========================================================
        
        self.DJSON = DJSON
        _, self.DInts = read_arrays(f, DJSON) # TODO: What ranges are there? =======================
    
    def values(self):
        L = []
        for value in list(self.DInts.keys()):
            L.append(value)
        return L

    def get_value_info(self, value):
        return CharIndexValueInfo(value, str(value))

    def search(self, search):
        if search in self.DInts:
            return self.DInts[search]
        raise KeyError(search)
