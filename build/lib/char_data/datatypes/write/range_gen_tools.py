MINIMUM_THRESHOLD = 15

def uncompress_ranges(DOrds):
    DRtn = {}
    for ord_ in DOrds:
        if type(ord_) == tuple:
            # Make the values point to LSeek
            
            # A range, so add it to LRanges
            # Note that the second value is [+0]
            data = DOrds[ord_]
            from_, to = ord_
            for i_ord in xrange(from_, to+1):
                #assert not i_ord in DOrds, (i_ord, data, DOrds[i_ord]) # WARNING! ==============================================
                DRtn[i_ord] = data
            #LRanges.append(tuple(ord_)+(data,))
            
        else: 
            # A single codepoint
            DRtn[ord_] = DOrds[ord_]
    return DRtn

def append(DOrds, LRanges, LRange, last_value, LDelOrds):
    # Add a minimum range threshold, to save type overhead
    num_chars = (LRange[1]-LRange[0])
    no_last_value = last_value == 'NO_LAST_VALUE'
    
    if num_chars>MINIMUM_THRESHOLD and not no_last_value: 
        # Add to ranges and delete from individual codepoints                        
        for del_ord in LDelOrds:
            del DOrds[del_ord]
        
        # Add to ranges as above, remembering tha val is [+0]
        LRanges.append(tuple(LRange)+(last_value,))

def compress_ord_ranges(DOrds):
    """
    Returns (LRanges, DOrds)
    
    makes it so that consecutive character ordinals which 
    have the same value are compressed into ranges, e.g.
    
    DOrds of {0: 'q', 1: 'a', 2: 'a', (3-8 the same), 9: 'a', 10: 'a'}
    might be compressed into
    DOrds -> {0: 'q'}
    LRanges -> [[(1, 11), 'a']]
    """
    
    DOrds = uncompress_ranges(DOrds)
    
    # Add ranges to save space for similar properties
    LRanges = []
    if DOrds:
        LDelOrds = []
        LRange = [-2, -2]
        
        # a magic value as some values are `None`!
        last_value = 'NO_LAST_VALUE'
        
        for ord_ in xrange(max(DOrds)+1):
            if ord_ in DOrds:
                same_as_last_time = last_value == DOrds[ord_]
                is_next_ordinal = ord_-1 == LRange[1]
                
                if same_as_last_time and is_next_ordinal:
                    # It's [+1] from last time and the value 
                    # hasn't changed, so append to the range
                    LRange[1] = ord_
                    LDelOrds.append(ord_)
                    
                else: 
                    # Append and reset the previous values
                    append(DOrds, LRanges, LRange, last_value, LDelOrds)
                    
                    LDelOrds = [ord_]
                    LRange = [ord_, ord_]
                    last_value = DOrds[ord_]
        
        # Add the last values
        append(DOrds, LRanges, LRange, last_value, LDelOrds)
    LRanges.sort()
    
    return LRanges, DOrds
    