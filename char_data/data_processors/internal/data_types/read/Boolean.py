from toolkit.arrays import read_array, read_json

from char_data.misc.get_adjusted_code_point import get_adjusted_code_point
from char_data.data_processors.internal.data_types.write.write_boolean import write_boolean

from char_data.abstract_base_classes.formatters.InternalFormatterBase import InternalFormatterBase, NO_DATA


DBool = {
    '1': True,
    '0': False,
    'U': None
}


class Boolean(InternalFormatterBase):
    writer = staticmethod(write_boolean)
    
    def _load_data(self, key, f, DJSON):
        self.DJSON = DJSON
        self.key = key
        
        self.LRanges = read_json(f, DJSON['LRanges'])
        self.LIgnoreRanges = read_json(f, DJSON['LIgnoreRanges'])
        
        self.LValues = read_array(f, DJSON['LValues'])
        
    def raw_data(self, ord_):
        data = self.get_range_data(ord_)
        if data != NO_DATA:
            return data
        
        ord_ = get_adjusted_code_point(ord_, self.LIgnoreRanges)
        if ord_ is None:
            # If the range cancelled, return None
            return None
        
        elif ord_ >= (len(self.LValues)-1):
            # Prevent IndexErrors
            return None
        
        else:
            # Return the boolean value
            
            # This is useful for character properties which only have
            # a True or False value, e.g. IICore in Unihan indicating
            # that a character is/isn't common in East Asia

            value = self.LValues.get_ascii_char(ord_)
            #print("BOOLEAN:", self.LValues, value)
            return DBool[value]
