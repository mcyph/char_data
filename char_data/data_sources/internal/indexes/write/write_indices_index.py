from write_integer_keys_index import write_integer_keys_index
from char_data.data_sources.internal.data.write import indice_tools


def write_indices_index(f, key, DData):
    '''
    Technically the same as a IntegerKeys, but as 
    the values are dicts filter down to the page number
    
    TODO: Allow more advanced queries? ============================================================
    '''
    print DData
    _, DData = indice_tools.parse_indices(key, DData)
    print DData
    
    DOut = {}
    for ord_ in DData:
        for DVal in DData[ord_]:
            if not DVal or not 'page' in DVal or DVal['page'] in (None, ''): 
                continue
            
            DOut[ord_] = DVal['page']  # MULTIPLE VALUE WARNING! ============
    
    # TODO: Fix the key orders! ==================================================================
    return write_integer_keys_index(f, key, DOut,
                                    prefix='pages')
