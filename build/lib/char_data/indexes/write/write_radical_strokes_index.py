from toolkit.arrays import get_int_array
from toolkit.arrays.ArrayUtils import write_arrays

def write_radical_strokes_index(f, key, DData, DJSON):
    '''
    Stores the Kangxi radical/additional strokes in a dict e.g.
    
    {"150'.5": [array.array('I'), ...],
     "150'": [array.array('I')]}
    
    Stores by both: 
    * (radical).(additional strokes)
    format as well as:
    * (radical)
    so that you can search even if you don't know the number of strokes.
    
    Simplified radicals are indicated by a final "'".
    '''
    DArrays = {}
    for ord_ in DData:
        for value in DData[ord_]:
            no_strokes_value = value.split('.')[0] # no added strokes
            
            if not value in DArrays:
                DArrays[value] = get_int_array()
            
            if not no_strokes_value in DArrays:
                DArrays[no_strokes_value] = get_int_array()
            
            DArrays[value].append(ord_)
            DArrays[no_strokes_value].append(ord_)
    
    # Write to disk
    return write_arrays(f, DArrays)
