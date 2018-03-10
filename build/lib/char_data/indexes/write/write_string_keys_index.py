from toolkit.arrays import get_uni_array, get_int_array
from toolkit.arrays.ArrayUtils import write_arrays, write_json

def iter_values(values):
    '''
    Iterate through each single value if there are multiple 
    in `values`. Otherwise just yield a single value
    '''
    if isinstance(values, (list, tuple)):
        LValues = values
    else:
        LValues = [values]
    
    for i_value in LValues:
        if isinstance(i_value, (list, tuple)):
            # (ordinal, flag), so just use the ordinal
            i_value = i_value[0]
        
        yield i_value

def write_string_keys_index(f, key, DData, DJSON):
    '''
    Will be stored by dicts, e.g.
    {'Arabic': [array.array('I')], ...}
    '''
    DStringKeys = {}
    LRanges = []
    
    # First go through the e.g. Unicode-specified ranges
    for ord_ in DData:
        for value in iter_values(DData[ord_]):
            if not value in DStringKeys:
                # Create a get_int_array for each value->ordinals mapping
                DStringKeys[value] = get_int_array()
        
            if type(ord_) in (list, tuple):
                # A range, so reprocess below
                LRanges.append((ord_, ord_))
            else:
                # A single value, so add just the codepoint
                DStringKeys[value].append(ord_)
    
    if len(DStringKeys) > 1000:
        print 'StringKeys Ignored Because of Size:', key, len(DStringKeys)
        return
    
    LRangesOut = []
    for key, (from_, to) in LRanges:
        # Normal Data
        LRangesOut.append([from_, to, DData[from_, to]])
    
    # Write to disk
    # TODO: Divide larger keys into smaller categories?
    DRtn = {}
    DRtn['DStringKeys'] = write_arrays(f, DStringKeys)
    DRtn['LRanges'] = write_json(f, LRangesOut)
    return DRtn
