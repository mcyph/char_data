from toolkit.arrays.ArrayUtils import read_array, read_json
from char_data.datatypes.read import RangeClass

from char_data.importer.misc.char_utilities import get_adjusted_code_point
from char_data.datatypes.write import write_integer_list
from char_data.datatypes.read.RangeClass import  NO_DATA


class IntegerList(RangeClass):
    writer = staticmethod(write_integer_list)
    
    def __init__(self, key, f, DJSON):
        self.DJSON = DJSON
        self.key = key
        
        self.LRanges = read_json(f, DJSON['LRanges'])
        self.LIgnoreRanges = read_json(f, DJSON['LIgnoreRanges'])
        self.DMultiVals = read_json(f, DJSON['DMultiVals'])
        
        self.LShort = read_array(f, DJSON['LShort'])
        
    def raw_data(self, ord_):
        """
        Returns a single integer value for each 
        character for e.g. frequencies, grades etc
        
        TODO: Rewrite to accept multiple integers? ================================================
        """
        ua_ord = ord_
        data = self.get_range_data(ord_)
        if data != NO_DATA:
            return tuple(data)
        
        ord_ = get_adjusted_code_point(ord_, self.LIgnoreRanges)
        if ord_ is None:
            # If the range cancelled, return None
            return None
        
        elif ord_ >= (len(self.LShort)-1):
            # Prevent IndexErrors
            return None
        
        else:
            # Return the short value
            value = self.LShort[ord_]
            
            if value: 
                LRtn = [value-1]
                
                # Add extra integer values if there are 
                # any for this ordinal in DMultiVals
                if ua_ord in self.DMultiVals:
                    LRtn.extend(self.DMultiVals[ua_ord])
                
                return tuple(LRtn)
            else: 
                return None
