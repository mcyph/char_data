from toolkit.arrays import get_uni_array, get_int_array
from toolkit.arrays import write_arrays, write_json


def iter_values(values):
    """
    Iterate through each single value if there are multiple 
    in `values`. Otherwise just yield a single value
    """
    if isinstance(values, (list, tuple)):
        LValues = values
    else:
        LValues = [values]
    
    for i_value in LValues:
        if isinstance(i_value, (list, tuple)):
            # (ordinal, flag), so just use the ordinal
            i_value = i_value[0]
        
        yield i_value


def write_string_keys_index(f, key, DData):
    """
    Will be stored by dicts, e.g.
    {'Arabic': [array.array('I')], ...}
    """
    DStringKeys = {}
    LRanges = []
    
    # First go through the e.g. Unicode-specified ranges
    for ord_ in DData:
        #if key =='subblock_heading':
        #    print('DData[ord]:', DData[ord_])

        for value in iter_values(DData[ord_]):
            #if key == 'subblock_heading':
            #    print(value, ord_)

            if not value in DStringKeys:
                # Create a get_int_array for each value->ordinals mapping
                DStringKeys[value] = get_int_array()
        
            if type(ord_) in (list, tuple):
                # A range, so reprocess below
                LRanges.append((value, ord_))
            else:
                # A single value, so add just the codepoint
                DStringKeys[value].append(ord_)
    
    #if len(DStringKeys) > 10000:
    #    print(('StringKeys Ignored Because of Size:', key, len(DStringKeys)))
    #    return
    
    LRangesOut = []

    for value, (from_, to) in LRanges:
        # Normal Data
        LRangesOut.append([from_, to, value])
    
    # Write to disk
    # TODO: Divide larger keys into smaller categories?
    DRtn = {}
    DRtn['DStringKeys'] = write_arrays(f, DStringKeys)
    DRtn['LRanges'] = write_json(f, LRangesOut)

    return DRtn
