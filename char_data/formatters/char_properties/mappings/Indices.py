from char_data.datatypes.read import Indices as _Indices


class Indices(_Indices):
    def __init__(self, key, f, DJSON):
        _Indices.__init__(self, key, f, DJSON)
    
    def formatted(self, ord_):
        # Indices have a dict e.g. {'Page': 145, 'Offset': "'"} etc
        # TODO: ADD INDICE FORMATTING for KangXi etc columns!
        data = self.raw_data(ord_)
        
        if data is None:
            return None
        LOrder, LData = data
        
        LRtn = []
        for DData in LData:
            L = []
            for key in LOrder:
                value = DData[key]
                if value != None:
                    # TODO: What if there are multiple values?
                    L.append('%s: %s' % (key, value))
            
            if L:
                LRtn.append(' '.join(L))
        
        if LRtn: 
            return '; '.join(LRtn)
        else: 
            return None
