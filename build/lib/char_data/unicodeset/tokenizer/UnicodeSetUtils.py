import codecs
from char_data import idx_keys, idx_values
from char_data.data_paths import data_path

#=========================================================#
#                       Properties                        #
#=========================================================#

def get_D_props():
    D = {}
    for ns, key, _ in idx_keys():
        conv_key = key.lower().replace(' ', '_')
        D['%s.%s' % (ns, conv_key)] = '%s.%s' % (ns, key)
        D[conv_key] = key
    return D

def get_D_prop_aliases():
    """
    Get a map of Unicode property aliases,
    e.g. {'ccc': 'Canonical_Combining_Class', ...}
    """
    D = {}
    with codecs.open(
        data_path(
            'chardata',
            'unidata/src/PropertyAliases.txt'),
        'rb',
        'utf-8'
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
    for ns, key, _ in idx_keys():
        D['%s.%s' % (ns, key)] = D[key] = _get_D_values((ns, key))
    return D

def _get_D_values(key):
    """
    Get a map from the stringified, lowercased property value
    to the property
    
    TODO: support property value aliases!
    """
    L = idx_values(key)
    #print key, type(L)
    if not L:
        return {} # WARNING! =============================================
    
    D = {}
    for i in idx_values(key):
        k = unicode(i).lower()
        assert not k in D
        D[k] = i
    return D

def get_D_value_aliases():
    pass

def get_D_general_cat_aliases():
    D = {}
    with codecs.open(
        data_path(
            'unicode_set',
            'GeneralCatAliases.txt'
        ),
        'rb',
        'utf-8'
    ) as f:

        for line in f:
            line = line.strip()
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
    
    L = ['general category', 
         'script',
         'property list']
    
    D = {}
    D['l&'] = [('general category', i) for i in ('Ll', 
                                                 'Lu', 
                                                 'Lt')]
    
    for key in idx_values('general category'):
        # make it so that e.g. "L"/"l" finds all letters
        D.setdefault(key[0].lower(), []).append(('general category', key))
    
    for idx_key in L:
        i_D = _get_D_values(idx_key)
        for key, value in i_D.items():
            D.setdefault(key, []).append((idx_key, value))
    
    
    for key, value in get_D_general_cat_aliases().items():
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
