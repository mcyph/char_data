from toolkit.arrays import get_int_array
from char_data.misc import get_char_gaps, iter_ranges
from toolkit.arrays import write_array, write_json
from write_boolean import ranges_to_single_ords
from range_gen_tools import compress_ord_ranges


def coorce_to_encodings(DOrds):
    DFlags = {} # {flag: string, ...}
    for ord_, value in DOrds.items():
        LEnc = get_L_encoding(DFlags, value)
        DOrds[ord_] = LEnc
    return DFlags, DOrds


def write_encoding(f, key, DOrds):
    DFlags, DOrds = coorce_to_encodings(DOrds)
    LRanges, DOrds = compress_ord_ranges(DOrds)
    DOrds = ranges_to_single_ords(DOrds)
    LIgnoreRanges = get_char_gaps(DOrds)
    
    '''
    Encoding [BigFive etc]
    Variables: LSeek[+1] -> LValues[+1]
    '''
    LSeek = get_int_array() # [+1]
    
    '''
    LValues should be [+1], but can't be used as "FFFF" 
    will be chopped off. Instead I've used the *first*
    value to specify the number of values at that seekpoint, 
    similar to pascal strings which don't use \0's
    '''
    LValues = get_int_array() # [should be +1, but can't]
    
    '''
    Store flags assigned to variants if there's a source 
    associated to it, e.g. in Unihan's kSemanticVariant 
    "U+7A69<kFenn,kMatthews" might store kFenn as `1` 
    and kMatthews as `2`, making the flag for U+7A69 `3`
    '''
    LFlags = get_int_array()
    
    if DOrds:
        for ord_ in iter_ranges(LIgnoreRanges, max(DOrds)):
            if ord_ in DOrds:
                LEnc = DOrds[ord_]
                
                LSeek.append(len(LValues)+1)
                
                LValues.append(len(LEnc))
                LFlags.append(0) # NOTE ME!
                
                for enc, flags in LEnc: 
                    LValues.append(enc)
                    LFlags.append(flags)
            else: 
                LSeek.append(0)
    else:
        assert LRanges
    
    # Write to disk
    DRtn = {}
    DRtn['LSeek'] = write_array(f, LSeek)
    DRtn['LValues'] = write_array(f, LValues)
    DRtn['LIgnoreRanges'] = write_json(f, LIgnoreRanges)
    DRtn['LRanges'] = write_json(f, LRanges)
    
    if DFlags:
        # Write flags to disk if there are any for this key
        DFlagsReversed = dict((str(value), i_key) for i_key, value in DFlags.items())
        DRtn['DFlags'] = write_json(f, DFlagsReversed)
        DRtn['LFlags'] = write_array(f, LFlags)
    
    return DRtn


def get_L_encoding(DFlags, hex_):
    if type(hex_) in (str, unicode):
        # Return a list of ints from the hex values separated by spaces
        LRtn = []
        for enc in hex_.split():
            if not enc.strip(): 
                continue
            
            # Remove U+ (unicode codepoint markers)
            enc = enc.replace('U+', '')
            
            # Process any source flags
            if '<' in enc:
                enc, _, sources = enc.partition('<')
                
                flag = 0
                for source in sources.split(','):
                    source = source.strip()
                    
                    if not source in DFlags:
                        DFlags[source] = 2**len(DFlags)
                    
                    flag = flag|DFlags[source]
            else:
                flag = 0
            
            LRtn.append((int(enc, 16), flag))
        return LRtn
    
    elif type(hex_) in (list, tuple):
        return [(i, 0) for i in hex_]
    
    else: 
        # Assume the values are already decimal numbers and return
        return [(hex_, 0)]
