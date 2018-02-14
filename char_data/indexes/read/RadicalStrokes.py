from toolkit.arrays.ArrayUtils import read_arrays

class RadicalStrokesIndex:
    typ = 'radical_strokes'
    
    def __init__(self, f, DJSON):
        self.DJSON = DJSON
        
        '''
        DRS -> {'[Kangxi radical].[number of additional strokes]: [...],
                '[Kangxi radical]': [...],
                ...}
        
        Kangxi radical is the number, a "'" character 
        after the number indicates a simplified variant
        '''
        _, self.DRS = read_arrays(f, DJSON)
    
    def keys(self):
        '''
        RadicalStrokes really need to use the data 
        in Radical to get English radnames etc
        and this would return the stroke counts which 
        I think adds too many items so I've disabled it
        '''
        return None
    
    def search(self, search):
        if search in self.DRS:
            return self.DRS[search]
        raise KeyError(search)
