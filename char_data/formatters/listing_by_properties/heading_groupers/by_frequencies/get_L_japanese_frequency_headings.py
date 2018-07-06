from char_data import char_data


# Please DON'T fiddle - it may make some queries
# nicer, but there are *always* exceptions :-) 
JFREQ_AMOUNT = 500


def get_L_japanese_frequency_headings(LRanges):
    # Group by frequency/grade etc under subheadings
    DRanges = {}
    for ord_ in LRanges:
        frequency = raw_data('kanjidic.frequency', ord_)
        
        if frequency is None:
            if False: 
                continue
            elif ord_ > 65536: 
                key = 'extremely uncommon'
            else: 
                key = 'very uncommon'
        else:
            key = frequency // JFREQ_AMOUNT
        
        if not key in DRanges: 
            DRanges[key] = []
        DRanges[key].append((frequency, ord_))
    
    LKeys = DRanges.keys()
    LKeys.sort()
    
    LRtn = []
    for key in LKeys:
        if type(key) == int:
            from_ = key*JFREQ_AMOUNT
            to = from_+(JFREQ_AMOUNT-1)
            sub_block = 'Japanese frequencies %s - %s' % (from_, to)
        else: 
            sub_block = key
        
        DRanges[key].sort()
        
        LRtn.append(('sub_block', sub_block))
        LRtn.append(['chars', [i[1] for i in DRanges[key]]])
    return LRtn
