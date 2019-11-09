from char_data.CharIndexes import char_indexes
from char_data.data_paths import data_path

#=========================================================#
#                       Properties                        #
#=========================================================#


def get_D_props():
    D = {}
    for key in list(char_indexes.keys()):
        D[key.partition('.')[-1]] = key
    return D


def get_D_prop_aliases():
    """
    Get a map of Unicode property aliases,
    e.g. {'ccc': 'Canonical_Combining_Class', ...}
    """
    D = {}
    with open(
        data_path(
            'chardata',
            'unidata/source/PropertyAliases.txt'),
        'r',
        encoding='utf-8'
    ) as f:

        for line in f:
            line = line.split('#')[0].strip()
            L = [i.strip() for i in line.split(';') if i.strip()]
            if not L:
                continue
            
            prop = L[1]
            LAliases = [L[0]]+L[2:]
            
            for alias in LAliases:
                assert not alias in D
                D[alias.lower()] = prop
    
    # HACKS!
    D['canonical_combining_class'] = D['ccc'] = 'canonical_combining_classes'
    return D

#=========================================================#
#                         Values                          #
#=========================================================#


def get_D_values():
    D = {}
    for key in list(char_indexes.keys()):
        D[key] = D[key.partition('.')[-1]] = _get_D_values(key)
    return D


def _get_D_values(key):
    """
    Get a map from the stringified, lowercased property value
    to the property
    
    TODO: support property value aliases!
    """
    L = char_indexes.values(key)
    #print key, type(L)
    if not L:
        return {} # WARNING! =============================================
    
    D = {}
    for i in char_indexes.values(key):
        k = str(i).lower()
        assert not k in D
        D[k] = i
    return D


def get_D_value_aliases():
    pass


def get_D_general_cat_aliases():
    D = {}
    with open(
        data_path(
            'chardata',
            'GeneralCatAliases.txt'
        ),
        'r', encoding='utf-8'
    ) as f:

        for line in f:
            line = line.split('#')[0].strip()
            if not line:
                continue
            
            prop, alias = line.split('\t')
            alias = alias.lower()
            if alias in D:
                assert D[alias] == prop
            
            D[alias.lower()] = prop
    return D

#=========================================================#
#                         Other                           #
#=========================================================#


def get_D_default_props():
    """
    Get the default [:xxx:] and \p{xxx} mappings
    
    TODO: Add posix values, e.g. [:alnum:] etc!
    """
    
    L = [
        'general category',
        'script',
        'property list'
    ]
    
    D = {}
    D['l&'] = [('general category', i) for i in (
        'Ll',
        'Lu',
        'Lt'
    )]
    
    for key in char_indexes.values('general category'):
        # make it so that e.g. "L"/"l" finds all letters
        D.setdefault(key[0].lower(), []).append(('general category', key))
    
    for idx_key in L:
        i_D = _get_D_values(idx_key)
        for key, value in list(i_D.items()):
            D.setdefault(key, []).append((idx_key, value))

    for key, value in list(get_D_general_cat_aliases().items()):
        #print value
        if value == 'Cn':
            continue # UNASSIGNED HACK! ========================================
        
        for i_key, i_value in D[value.lower()]:
            assert i_key == 'general category'
            D.setdefault(key, []).append(('general category', i_value))
    
    #print 'DDefaultProps:', D
    #from pprint import pprint
    #pprint(D)
    return D
