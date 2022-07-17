from heapq import nsmallest
do_print = True


def adv_sort(LSort):
    """
    Sort by a percentage value, e.g. 
        [[0.4, [...]], [0.6, [...]]]
    giving each a different weight
    """
    LPos = []
    for percent, text, LValues in LSort:
        i = 0
        DPos = {}
        LValues.sort()
        for _, char in LValues:
            #print percent, delSort, char
            DPos[char] = i
            i += 1
        
        if do_print:
            print('%s:' % text, ''.join([i[1] for i in LValues]).encode('utf-8')[:20])
        LPos.append((percent, DPos))
    
    SAdded = set()
    return_list = []
    for _, i_DPos in LPos:
        for k in i_DPos:
            if k in SAdded: 
                continue
            
            SAdded.add(k)
            c_val = 0.0
            for percent, DPos in LPos:
                if not k in DPos: 
                    continue
                
                plus = float(DPos[k])
                c_val += plus*percent
            
            if 0: 
                c_val = pow(c_val, 2)
            
            return_list.append((c_val, k))
    
    return_list.sort()
    return_list = [i[1] for i in return_list]
    return return_list


compare = lambda a: a[0]


def chunk_sort(LSort, LChunkKeys):
    # Sort by a percentage value in exponential chunks, e.g. 
    #     [[0.4, [...]], [0.6, [...]]]
    # giving each a different weight
    
    DChunk = {}
    DLens = {}
    for text, LValues in LSort:
        LValues = nsmallest(140/len(LChunkKeys), LValues, key=compare)
        LValues.sort(key=compare)
        
        DChunk[text] = [i[1] for i in LValues]
        DLens[text] = len(DChunk[text])
        
        if do_print:
            print('%s: %s' % (text, ''.join(DChunk[text][:20]).encode('utf-8')))
    
    return_list = []
    c_index = 0
    DAdded = {}
    while 1:
        remaining = 0
        for key in LChunkKeys:
            if DLens[key] > c_index:
                remaining = 1
                char = DChunk[key][c_index]
                
                if not char in DAdded:
                    DAdded[char] = None
                    return_list.append(char)
        
        if not remaining: 
            break
        c_index += 1
        
        if c_index > 121: 
            break # SPEED HACK!
    return return_list


if __name__ == '__main__':
    print(adv_sort(
        [[0.4, [[1, 1], [2, 2]]],
        [0.6, [[2, 1], [1, 2]]]]
    ))
