from toolkit.arrays.ArrayUtils import read_array, read_json

from char_data.misc import get_adjusted_code_point
from char_data.data_sources.internal.data.write import write_string_data
from char_data.data_sources.internal.data.read.InternalBaseClass import NO_DATA

from InternalBaseClass import InternalBaseClass


class StringData(InternalBaseClass):
    writer = staticmethod(write_string_data)
    
    def _load_data(self, key, f, DJSON):
        self.DJSON = DJSON
        self.key = key
        
        self.LRanges = read_json(f, DJSON['LRanges'])
        self.LIgnoreRanges = read_json(f, DJSON['LIgnoreRanges'])
        
        self.LSeek = read_array(f, DJSON['LSeek'])
        self.LAmount = read_array(f, DJSON['LAmount'])
        self.LWords = read_array(f, DJSON['LWords'])
        
        self.DWordLinkCache = {}
        
    def raw_data(self, ord_):
        # FIXME: Add support for multiple values! =======================================================

        """
        Compresses single string values to a "table", useful when there's 
        lots of the same values. Stores values in ranges as well as single 
        codepoints to reduce wasted space
        """
        
        # First check the ranges
        seek = self.get_range_data(ord_)

        if seek != NO_DATA:
            seek, amount = seek
            return self.get_word(seek, amount)
        
        i_ord = get_adjusted_code_point(ord_, self.LIgnoreRanges)
        #print 'ord_:', ord_, 'Adjusted ord_:', i_ord
        if i_ord is None:
            # Then return None if nothing found
            return None
        elif i_ord >= (len(self.LSeek)-1): # WARNING! ==================================================
            # Prevent IndexErrors
            return None
        else:
            # Return the "short->reference word" value
            seek = self.LSeek[i_ord]
            if seek == 0: 
                return None
            else: 
                return self.get_word(seek-1, self.LAmount[i_ord]) #[+1]
    
    def get_word(self, seek, amount):
        return self.LWords[seek:seek+amount]
