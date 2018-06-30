DCombine = {
    'cmn': [],
    'jpn': [],
    'kor': [],
    '': []
}


class DefinitionCombine:
    def __init__(self, LKeys):
        pass
    
    def raw_data(self, ord_):
        # TODO: Combine data from multiple sources
        pass
    
    def formatted(self, ord_):
        LRtn = []
        if typ == 'cmn:eng':
            extend_data(LRtn, )
        
        elif typ == 'yue:eng':
            # Add Cantonese Definition
            added = extend_data(LRtn, 'Cantonese Definition', ord_)
            
            if not added:
                extend_data(LRtn, 'Chinese Definition', ord_,
                            format=' [Mandarin Definition]')
        
        elif type.startswith('jpn:'):
            # Add Japanese Definition
            DTypes = {'eng': 'Japanese Definition',
                      'por': 'Japanese Definition in Portuguese',
                      'spa': 'Japanese Definition in Spanish'}
            
            LRtn = []
            to_iso = typ.split(':')[-1]
            added = extend_data(LRtn, DTypes[to_iso], ord_)
            
            if not added and to_iso=='eng':
                # Fallback to a Chinese definition 
                # if not one found for Japanese
                extend_data(LRtn, 'Chinese Definition', ord_, 
                            format='%s [Mandarin definition]')
        
        else: 
            raise Exception("Unknown CharMap type: %s" % typ)
        
        return LRtn
    