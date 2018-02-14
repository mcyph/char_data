import binascii
from toolkit.surrogates import w_unichr
#from Dicts.Other.Import.DelimText import Encodings

class Encodings:
    def __init__(self, encoding):
        self.encoding = encoding
    
    def explain(self, ord_):
        pass
    
    def get_L_keys(self):
        raise NotImplementedError
    
    def raw_data(self, ord_):
        # Add encoding mappings
        char = w_unichr(ord_)
        
        try: 
            return char.encode(self.encoding)
        except Exception: 
            return None
    
    def formatted(self, ord_):
        data = self.raw_data(ord_)
        
        if isinstance(data, basestring):
            LHex = ['%s' % binascii.hexlify(i).upper() for i in data]
            return ' '.join(LHex)
        else:
            return None
