from char_data.data_sources.external.property_formatters import ExternalBaseClass


# TODO: REMOVE ME! ----------------------------------------------------------------------------------------
DISO2LFullText = {
    'yue': [['Cantonese', 'Cantonese Readings'], ['Cantonese Definition']], # MULTIPLE?
    'jpn': [['Japanese Kun', 'Japanese On', 'Japanese Nanori'], ['Japanese Definition']],
    'hak': [['Hakka'], ['Cantonese Definition']],
    'kor': [['Korean', 'Hangul Readings', 'Korean Hangul'], ['Chinese Meanings']], # MULTIPLE?
    'cmn': [['Mandarin'], ['Chinese Definition']],
    'ltc': [['Tang'], ['Chinese Definition']],
    'vie': [['Vietnamese'], ['Chinese Definition']]
}  # PHONETIC WARNING!


DMap = {
    'All': ('cmn:eng', 'jpn:eng', 'yue:eng', 'General', 'NamesList'),
    'cmn:eng': ('cmn:eng', 'General', 'NamesList'),
    'yue:eng': ('yue:eng', 'General', 'NamesList'),
    'jpn:eng': ('jpn:eng', 'General', 'NamesList'),
    'jpn:spa': ('jpn:spa', 'General', 'NamesList'),
    'jpn:por': ('jpn:por', 'General', 'NamesList'),
    'kor:eng': ('cmn:eng', 'General', 'NamesList'),
    'hak:eng': ('yue:eng', 'General', 'NamesList'),
    'ltc:eng': ('cmn:eng', 'General', 'NamesList'),
    'vie:eng': ('cmn:eng', 'General', 'NamesList')
}




DCombine = {
    'cmn': [],
    'jpn': [],
    'kor': [],
    '': []
}


class DefinitionCombine(ExternalBaseClass):
    def __init__(self, LKeys):
        FIXME
    
    def raw_data(self, ord_):
        # TODO: Combine data from multiple sources
        pass
    
    def formatted(self, ord_, data):
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
    