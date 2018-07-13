from char_data.data_sources.internal.data.read import Indices as _Indices


class Indices(_Indices):
    def _format_data(self, ord_, data):
        # Indices have a dict e.g. {'Page': 145, 'Offset': "'"} etc
        # TODO: ADD INDICE FORMATTING for KangXi etc columns!
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
