# -*- coding: utf-8 -*-
from char_data.datatypes.read import StringData
from char_data.radicals.DataRadicals import DRadTypes

#DRads = Radical.get_D_rads()


class RadicalStrokes(StringData):
    def __init__(self, key, f, DJSON):
        StringData.__init__(self, key, f, DJSON)
    
    def get_L_keys(self):
        # radical types
        LRadInfo = DRadTypes[self.key]
        list_type = 'MultiRadSel' # HACK!
        traditional = LRadInfo[0]
        rad_column = None # MultiRadSel HACK!
        LRtn = [list_type, rad_column, traditional]
        return LRtn
    
    def formatted(self, ord_):
        # TODO: Split into (radical, Additional Strokes) and display as 
        # the actual radical using radical.py:
        # %(radical)s (%(Additional Strokes)s Additional Strokes)
        # TODO: Should there be an Adobe/CheungBauer parser?
        data = self.raw_data(ord_)
        
        if not data: 
            return None
        
        L = []
        for x in data.strip().split(' '):
            radical, extra_strokes = x.split('.')
            if not radical:
                # CCDict "㽍" etc HACK!
                continue
            
            # CCDict multiple values HACK!
            extra_strokes = int(extra_strokes.rstrip(';'))
            
            new_radical = ''
            for i_strokes, i_radical, i_eng_name in DRads[radical]:
                new_radical += i_radical
            
            radical = new_radical
            L.append('%s with %s extra strokes' % (radical, extra_strokes))
        data = '/'.join(L)
        return data or None
