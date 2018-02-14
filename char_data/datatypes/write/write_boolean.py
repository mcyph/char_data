from toolkit.arrays import get_uni_array
from char_data.importer.misc.char_utilities import get_char_gaps, iter_ranges
from toolkit.arrays.ArrayUtils import write_array, write_json
from char_data.datatypes.write.range_gen_tools import compress_ord_ranges

def ranges_to_single_ords(DOrds):
    # Convert ranges to single codepoints
    for ord_ in list(DOrds.keys()):
        if isinstance(ord_, tuple):
            value = DOrds[ord_]
            del DOrds[ord_]
            for x in xrange(ord_[0], ord_[1]+1): # CHECK ME! ============================================
                assert not x in DOrds
                DOrds[x] = value
    return DOrds

def write_boolean(f, key, DOrds):
    '''
    Boolean [Mirrored etc (Technically three-value 
      e.g. 0 for False 1 for True U for undefined)]
    TODO: Should this be a range?
    uses char as type
    Variables: LValues[Default U]
    '''
    LValues = get_uni_array() # [+1]
    
    LRanges, DOrds = compress_ord_ranges(DOrds)
    
    LIgnoreRanges = get_char_gaps(DOrds)
    DOrds = ranges_to_single_ords(DOrds)
    
    # Fill the data gaps
    if DOrds:
        for ord_ in iter_ranges(LIgnoreRanges, max(DOrds)):
            if ord_ in DOrds:
                if DOrds[ord_]:
                    LValues.append('1')
                else: 
                    LValues.append('0')
            else: 
                LValues.append('U')
    else:
        assert LRanges
    
    # Write to disk
    DRtn = {}
    DRtn['LValues'] = write_array(f, LValues)
    DRtn['LIgnoreRanges'] = write_json(f, LIgnoreRanges)
    DRtn['LRanges'] = write_json(f, LRanges)
    return DRtn
