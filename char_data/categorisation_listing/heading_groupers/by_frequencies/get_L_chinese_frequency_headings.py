from char_data import formatted


DGrades = {
    'Hong Kong Grade': 'Hong Kong Grade',
    'Japanese Grade': 'Japanese'
}


def get_L_chinese_frequency_headings(LRanges, LSortBy):
    """
    Group by frequencys/grade etc under subheadings
    """
    DRanges = {}
    for ord_ in LRanges:
        freq = formatted(LSortBy[0], ord_)
        
        if freq is None:
            if False: 
                continue
            elif ord_ > 65536: 
                freq = 'extremely uncommon'
            else: 
                freq = 'very uncommon'
        
        elif LSortBy[0] in DGrades:
            freq = '%s %s' % (DGrades[LSortBy[0]], freq)
        
        if not freq in DRanges:
            DRanges[freq] = []
        DRanges[freq].append(ord_)
    
    # Group by secondary sort key
    LRtn = []
    LKeys = DRanges.keys()
    if LSortBy[0] in DGrades or True:
        nLKeys = []
        for key in LKeys:
            if key == 'extremely uncommon':
                nLKeys.append((65538, key))
            elif key == 'very uncommon':
                nLKeys.append((65537, key))
            else: 
                #print key
                try:
                    if key.split('/')[0].isalnum():
                        nLKeys.append((int(key.split('/')[0]), key))
                    else: 
                        nLKeys.append((int(key.split()[-1]), key))
                except: 
                    nLKeys.append((65536, key)) # HACK!
        
        nLKeys.sort()
        LKeys = [i[1] for i in nLKeys]
    else: 
        LKeys.sort()
    
    for key in LKeys:
        LRtn.append(('sub_block', key))
        LRtn.append(['chars', []])
        
        for ord_ in DRanges[key]:
            LCodePointOrder = []
            
            for sort in LSortBy[1:]:
                freq = chars.formatted(sort, ord_)
                LCodePointOrder.append(freq)
            
            LRtn[-1][1].append((LCodePointOrder, ord_))
        
        LRtn[-1][1].sort()
        LRtn[-1][1] = [i[1] for i in LRtn[-1][1]]
    return LRtn


if __name__ == '__main__':
    # TODO: Add a test here!!!!!! =========================================================================
    pass
