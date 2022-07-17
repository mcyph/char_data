from char_data.data_processors.internal.data_types.read import Indices as _Indices


class Indices(_Indices):
    def _format_data(self, ord_, data):
        # Indices have a dict e.g. {'Page': 145, 'Offset': "'"} etc
        # TODO: ADD INDICE FORMATTING for KangXi etc columns!
        if data is None:
            return None
        LOrder, LData = data
        
        return_list = []
        for DData in LData:
            L = []
            for key in LOrder:
                value = DData[key]
                if value != None:
                    # TODO: What if there are multiple values?
                    L.append('%s: %s' % (key, value))
            
            if L:
                return_list.append(' '.join(L))
        
        if return_list: 
            return '; '.join(return_list)
        else: 
            return None
