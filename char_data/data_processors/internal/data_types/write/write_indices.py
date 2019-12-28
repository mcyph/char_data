from char_data.toolkit.arrays import write_arrays, write_json
from char_data.misc import get_char_gaps, iter_ranges
from char_data.toolkit.arrays import get_uni_array, get_int_array

from char_data.data_processors.internal.data_types.write import indice_tools
from char_data.data_processors.internal.data_types.write.range_gen_tools import compress_ord_ranges


def write_indices(f, key, DOrds):
    """
    Indices [Storing Page Positions as Either Numeric or Char Data]
    Variables: DArrays
    """
    LArrays, DOrds = indice_tools.parse_indices(key, DOrds)
    DArrays = {}
    
    LRanges, DOrds = compress_ord_ranges(DOrds)
    
    LIgnoreRanges = get_char_gaps(DOrds)
    
    # Create the various arrays
    for name, typ in LArrays:
        if typ == 'char':
            # [\v] indicates None
            DArrays[name] = get_uni_array()
        elif typ == 'integer': 
            # [+1] to allow 0 for None
            DArrays[name] = get_int_array()
        else:
            raise Exception("Unknown indice type %s" % typ)
    
    # Fill the data gaps
    DMultiVals = {}
    for ord_ in iter_ranges(LIgnoreRanges, max(DOrds)):
        if ord_ in DOrds and DOrds[ord_]:
            LValues = DOrds[ord_]
            D = LValues[0]
            
            # Add to DMultiVals if more than one value
            if len(LValues) > 1:
                assert not str(ord_) in DMultiVals
                DMultiVals[str(ord_)] = LValues[1:]
            
            for k in D:
                value = D[k]
                LArray = DArrays[k]
                
                if value in (None, ''):
                    if LArray.typecode in ('u', 'c'):
                        LArray.append('\v')
                    else: 
                        LArray.append(0)
                else:
                    try:
                        if LArray.typecode in ('u', 'c'):
                            assert len(value) == 1
                            # WARNING: StrArray's only allow indexing of single ASCII
                            # chars, as they're encoded using utf-8 (!)

                            # Hopefully that's all it will need, though
                            LArray.append(str(value))
                        else: 
                            LArray.append(int(value)+1)
                    except:
                        print(('Error on value: %s key: %s typecode: %s' % (value, k, LArray.typecode)))
                        raise
        else: 
            for k in DArrays:
                # Append blank values
                LArray = DArrays[k]
                if LArray.typecode in ('u', 'c'):
                    LArray.append('\v')
                else: 
                    LArray.append(0)
    
    # Write to disk
    DRtn = {}
    DRtn['DArrays'] = write_arrays(f, [(name, DArrays[name]) for name, typ in LArrays])
    DRtn['LIgnoreRanges'] = write_json(f, LIgnoreRanges)
    DRtn['LRanges'] = write_json(f, LRanges)
    DRtn['DMultiVals'] = write_json(f, DMultiVals)
    return DRtn
