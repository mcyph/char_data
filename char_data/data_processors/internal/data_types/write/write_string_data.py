from char_data.toolkit.arrays import get_uni_array, get_int_array
from char_data.misc import get_char_gaps, iter_ranges
from char_data.toolkit.arrays import write_json, write_array
from char_data.data_processors.internal.data_types.write.range_gen_tools import compress_ord_ranges


def write_string_data(f, key, DOrds):
    """
    StringData (storing string lists by number to save space)
    """
    # Variables: 
    # + LRanges
    LRanges, DOrds = compress_ord_ranges(DOrds)
    
    # + LSeek[+1][Ranges Subtracted] -> LWords[\v terminated]
    LSeek = get_int_array() # [+1]
    LAmount = get_int_array()
    LWords = get_uni_array()
    
    DWordSeek = {}
    def get_L_seek(L):
        if not isinstance(L, (tuple, list)):
            L = [L]
        
        LRtn = []
        for data in L:
            # Append the seek position for string `data`
            if not data in DWordSeek:
                seek = len(LWords)
                amount = LWords.extend(str(data))
                DWordSeek[data] = (seek, amount)

            LRtn.append(
                DWordSeek[data]
            )
        return LRtn
    
    LIgnoreRanges = []
    if DOrds:
        # Only process if not Blocks etc
        LIgnoreRanges = get_char_gaps(DOrds)
        #print 'CHARGAPS:', LIgnoreRanges
        
        for ord_ in iter_ranges(LIgnoreRanges, max(DOrds)):
            #print Key, ord_
            if ord_ in DOrds:
                # And add the DWordSeek link to LSeek [+1]
                data = DOrds[ord_]
                
                for seek, amount in get_L_seek(data):
                    LSeek.append(seek+1)
                    LAmount.append(amount)
            else:
                LSeek.append(0)
                LAmount.append(0) # NOTE ME: It may pay to make this -1 and add assertions (!)
    
    # Make the values in the LRanges to point 
    # to seek positions as well to save space
    n_LRanges = []
    for from_, to, value in LRanges:
        a = get_L_seek(value)
        a = a[0] if len(a)==1 else a
        n_LRanges.append((from_, to, a))
    
    # Write to disk
    DRtn = {}
    DRtn['LRanges'] = write_json(f, n_LRanges)
    DRtn['LSeek'] = write_array(f, LSeek)
    DRtn['LAmount'] = write_array(f, LAmount)
    DRtn['LWords'] = write_array(f, LWords)
    DRtn['LIgnoreRanges'] = write_json(f, LIgnoreRanges)
    return DRtn
