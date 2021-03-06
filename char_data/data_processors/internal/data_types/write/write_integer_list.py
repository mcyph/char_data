from char_data.toolkit.arrays import get_int_array
from char_data.misc import get_char_gaps, iter_ranges
from char_data.toolkit.arrays import write_array, write_json

from char_data.data_processors.internal.data_types.write.range_gen_tools import compress_ord_ranges


def coerce_to_int(DOrds):
    for ord_, L in list(DOrds.items()):
        if isinstance(L, str):
            L = L.split()
        
        nL = []
        for i in L:
            chk1 = str(int(i))
            chk2 = str(i)
            assert chk1 == chk2, "%s should be %s" % (chk1, chk2)
            
            nL.append(int(i))
        DOrds[ord_] = nL
    return DOrds


def write_integer_list(f, key, DOrds):
    """
    IntegerList [Grades/Frequencies (storing only numbers)]
    """
    DOrds = coerce_to_int(DOrds)
    LRanges, DOrds = compress_ord_ranges(DOrds)
    LIgnoreRanges = get_char_gaps(DOrds)
    
    LShort = get_int_array() # [+1]
    
    # Fill the data gaps - TODO: ADD SUPPORT FOR MULTIPLE VALUES!
    DMultiVals = {}
    for ord_ in iter_ranges(LIgnoreRanges, max(DOrds)):
        #print 'ord_:', ord_
        if ord_ in DOrds:
            L = DOrds[ord_]
            LShort.append(int(L[0])+1)
            
            if len(L) > 1:
                # Append to `DMultiVals` if there is a 
                # character with multiple integers mappings!
                assert not str(ord_) in DMultiVals
                DMultiVals[str(ord_)] = L[1:]
        else: 
            LShort.append(0)
    
    # Write to disk
    print('WRITE LShort!')
    DRtn = {}
    DRtn['LShort'] = write_array(f, LShort)
    print('WRITE LIgnoreRanges!')
    DRtn['LIgnoreRanges'] = write_json(f, LIgnoreRanges)
    print('WRITE LRanges!')
    DRtn['LRanges'] = write_json(f, LRanges)
    print('WRITE DMultiVals!')
    DRtn['DMultiVals'] = write_json(f, DMultiVals)
    print(('OK:', DRtn))
    return DRtn
