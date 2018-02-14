from toolkit.escape import E, esc_q
USE_CACHE = True

# This file contains info on HOW to display the data for the user interface,
# e.g. whether to use a tree or list control or radical control etc.

DLists = {}
def get_select(S):
    LList = []
    opt_group = False
    
    for line in S.split('\n'):
        line = line.strip().replace('    ', '\t')
        
        if not line or line[0] == '#': 
            continue
        
        key, mapping = line.split('\t')
        key = key.strip()
        mapping = mapping.strip()
        
        if mapping == '--':
            # A 'placeholder' value
            if opt_group:
                LList.append('</optgroup>')
            LList.append('<optgroup label="%s">' % E(key))
            opt_group = True
        else:
            # A mapping
            DLists[key] = mapping
            LList.append('<option value="%s">%s</option>' % (esc_q(key), E(key)))
    
    if opt_group:
        LList.append('</optgroup>')
    return ''.join(LList)

DSelect = {'Base': get_select('Base.txt'),
           'Other': get_select('Other.txt'),
           'Radicals': get_select('Radicals.txt')}
