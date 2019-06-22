from toolkit.arrays import read_arrays, read_json

from char_data.misc import get_adjusted_code_point
from char_data.data_processors.internal.data_types.write import write_indices

from .InternalBaseClass import InternalBaseClass, NO_DATA


class Indices(InternalBaseClass):
    writer = staticmethod(write_indices)
    
    def _load_data(self, key, f, DJSON):
        self.DJSON = DJSON
        self.key = key
        
        self.LOrder, self.DArrays = read_arrays(f, DJSON['DArrays'])
        self.LRanges = read_json(f, DJSON['LRanges'])
        self.LIgnoreRanges = read_json(f, DJSON['LIgnoreRanges'])
        self.DMultiVals = read_json(f, DJSON['DMultiVals'])
    
    def raw_data(self, ord_):
        LOrder = self.LOrder
        
        data = self.get_range_data(ord_)
        if data != NO_DATA:
            return LOrder, data
        
        ua_ord = ord_
        ord_ = get_adjusted_code_point(ord_, self.LIgnoreRanges)
        
        if ord_ is None:
            # If the range cancelled, return None
            return None
        
        elif ord_ >= (len(self.DArrays[LOrder[0]])-1):
            # Prevent IndexErrors
            return None
        
        else:
            '''
            Returns a dict with numeric or string values, 
            e.g. {'page': 555, ...} allowing referencing
            where a character appears in a dictionary or 
            textbook etc.
            
            TODO: PLEASE UPDATE TO ALLOW MULTIPLE
            e.g. pages for the same character! ====================================================
            '''
            
            DRtn = {}
            for key in LOrder:
                L = self.DArrays[key]
                
                if hasattr(L, 'typecode') and L.typecode in ('u', 'c'):
                    value = L.get_ascii_char(ord_) # UNICODE WARNING! ==================================================================
                    if value != '\v': 
                        DRtn[key] = value
                    else: 
                        DRtn[key] = None
                else:
                    value = L[ord_]
                    if value: 
                        DRtn[key] = value-1
                    else: 
                        DRtn[key] = None
            
            LRtn = [DRtn]
            
            if ua_ord in self.DMultiVals:
                LRtn.extend(self.DMultiVals[ua_ord])
            
            return LOrder, LRtn
