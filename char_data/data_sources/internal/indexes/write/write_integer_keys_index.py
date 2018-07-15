from toolkit.arrays import get_int_array
from toolkit.arrays.ArrayUtils import write_arrays

def write_integer_keys_index(f, key, DData, prefix=None):
    '''
    DNum -> {value: number of items} where 
    `value` might be a grade number
    '''
    DNum = {}
    for ord_ in DData:
        if isinstance(DData[ord_], (list, tuple)):
            # HACK: Use only the first value if there are multiple grades etc
            # FIXME: Support multiple values! ===================================================
            DData[ord_] = DData[ord_][0]
        
        value = int(DData[ord_])
        if not value in DNum:
            DNum[value] = 0
        DNum[value] += 1
    
    # The maximum value migth be e.g. 10 for 
    # grade 10 < CHECK USED CORRECTLY! =============================================================
    max_ = max(DNum)
    min_ = min(DNum)
    
    DRtn = {}
    if len(DNum) > 50:
        '''
        Frequency values, usually thousands of possible values
        Filter them down by Max/50 to allow rough frequency browsing
        TODO: Make it a bit less "linear" than dividing by 50?
        
        For example:
        * Frequencies 0-49
        * Frequencies 50-99
        * Frequencies 100-149
        ...etc
        '''
        
        i = min_
        step = int(max_/50.0) or 1
        while 1:
            if i > max_:
                from_ = i
                to = max_
            else:
                from_ = i
                to = i+step-1
                i += step
            
            format = '%s - %s' % (from_, to)
            if prefix: 
                format = '%s %s' % (prefix, format)
            
            L = get_int_array()
            for ord_ in DData:
                if (int(DData[ord_]) >= int(from_) and 
                    int(DData[ord_]) <= int(to)):
                    #print 'ADDED:', from_, to, unicode(DData[ord_]).encode('utf-8')
                    L.append(ord_)
                #else: 
                #   print 'NOT ADDED:', from_, to, unicode(DData[ord_]).encode('utf-8')
            
            if len(L): 
                DRtn[format] = L
            
            # Stop looping if no more items!
            if i > max_: 
                break
        
    else:
        '''
        If less than 15 values, they're usually grade values which have 
        few possibilities, so divides into 'sets' of 100 or so, 
        
        For example:
        * Grade 1 (0-99)
        * Grade 1 (100-177)
        * Grade 2 (0-99)
        ...etc
        '''
        
        LValues = list(DNum.keys())
        LValues.sort()
        
        # 
        for value in LValues:
            num_steps = int(DNum[value]/100.0)+1
            for i in range(num_steps):
                # Add on the last maximum
                from_ = i*100
                to = from_+99
                
                if to > DNum[value]:
                    # If no more items, use the max number for "to"
                    to = DNum[value]
                
                # Write the index to DRtn
                # TODO: Add "Page" etc for indices?
                xx = 0
                format = '%s (%s - %s)' % (value, from_+1, to+1)
                L = get_int_array()
                for ord_ in DData:
                    if unicode(DData[ord_]) == unicode(value):
                        if xx>=from_ and xx<=to:
                            #print 'ADDED:', i, xx, unicode(value).encode('utf-8')
                            L.append(ord_)
                        #else: 
                        #   print 'NOT ADDED:', i, xx, unicode(value).encode('utf-8')
                        xx += 1
                
                if len(L): 
                    DRtn[format] = L
    
    # Write out to disk using unsigned integer arrays
    return write_arrays(f, DRtn)
