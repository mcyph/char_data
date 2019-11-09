from toolkit.arrays import read_array, read_json

from char_data.misc import get_adjusted_code_point
from char_data.data_processors.internal.data_types.write import write_encoding

from char_data.abstract_base_classes.formatters.InternalBaseClass import InternalBaseClass, NO_DATA


class Encoding(InternalBaseClass):
    writer = staticmethod(write_encoding)
    
    def _load_data(self, key, f, DJSON):
        self.DJSON = DJSON
        self.key = key
        
        self.LRanges = read_json(f, DJSON['LRanges'])
        self.LIgnoreRanges = read_json(f, DJSON['LIgnoreRanges'])
        
        self.LSeek = read_array(f, DJSON['LSeek']) # written with get_int_array
        self.LValues = read_array(f, DJSON['LValues']) # written with get_int_array
        
        self.flags = 'DFlags' in DJSON
        
        if self.flags:
            self.DFlags = read_json(f, DJSON['DFlags'])
            self.LFlags = read_array(f, DJSON['LFlags'])
        else:
            self.DFlags = {}
        
        # OPEN ISSUE: Create an index by encodings? ======================================================
        
    def get_L_by_flags(self, flags):
        LRtn = []
        for pow_ in range(len(self.DFlags)):
            flag = 2**pow_
            #print flag, flag& flags, self.DFlags[str(flag)]
            if flag& flags:
                LRtn.append(self.DFlags[str(flag)])
        return LRtn
        
    def raw_data(self, ord_):
        #print 'CODEPOINT:', ord_, self.LIgnoreRanges
        data = self.get_range_data(ord_)
        if data != NO_DATA:
            return tuple(data)
        
        ord_ = get_adjusted_code_point(ord_, self.LIgnoreRanges)
        if ord_ is None:
            # If the range cancelled, return None
            return None
        
        elif ord_ >= (len(self.LSeek)-1):
            # Prevent IndexErrors
            return None
        
        else:
            '''
            Return the encoding value, each item in LRtn 
            is a single int, representing a single byte,
            showing how the character is represented in 
            this encoding
            '''
            seek = self.LSeek[ord_]
            
            if seek == 0: 
                return None
            else: 
                seek -= 1 # [+1]
            
            LRtn = []
            for i in range(self.LValues[seek]):
                seek += 1
                enc = self.LValues[seek]
                
                if self.flags:
                    flag = self.LFlags[seek]
                else:
                    flag = 0
                
                LRtn.append((enc, flag))
            return tuple(LRtn)
