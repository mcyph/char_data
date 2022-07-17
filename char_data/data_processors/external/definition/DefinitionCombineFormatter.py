from char_data.data_processors.external.property_formatters import ExternalFormatterBase


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


class DefinitionCombineFormatter(ExternalFormatterBase):
    def __init__(self, LKeys):
        FIXME
    
    def raw_data(self, ord_):
        # TODO: Combine data from multiple sources
        pass
    
    def formatted(self, ord_, data):
        return_list = []
        if typ == 'cmn:eng':
            extend_data(return_list, )
        
        elif typ == 'yue:eng':
            # Add Cantonese Definition
            added = extend_data(return_list, 'Cantonese Definition', ord_)
            
            if not added:
                extend_data(return_list, 'Chinese Definition', ord_,
                            format=' [Mandarin Definition]')
        
        elif type.startswith('jpn:'):
            # Add Japanese Definition
            DTypes = {'eng': 'Japanese Definition',
                      'por': 'Japanese Definition in Portuguese',
                      'spa': 'Japanese Definition in Spanish'}
            
            return_list = []
            to_iso = typ.split(':')[-1]
            added = extend_data(return_list, DTypes[to_iso], ord_)
            
            if not added and to_iso=='eng':
                # Fallback to a Chinese definition 
                # if not one found for Japanese
                extend_data(return_list, 'Chinese Definition', ord_,
                            format='%s [Mandarin definition]')
        
        else: 
            raise Exception("Unknown CharMap type: %s" % typ)
        
        return return_list
    