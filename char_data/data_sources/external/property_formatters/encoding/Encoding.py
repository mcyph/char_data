import binascii
from toolkit.encodings.surrogates import w_unichr
#from Dicts.Other.Import.DelimText import Encodings

from char_data.data_sources.external.property_formatters import ExternalBaseClass


class Encoding(ExternalBaseClass):
    def __init__(self, encoding):
        self.encoding = encoding
        ExternalBaseClass.__init__(
            self, parent, HEADER_FIXME, original_name=encoding,
            short_desc=encoding, LISOs=FIXME
        )
    
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
    
    def _format_data(self, ord_, data):
        if isinstance(data, basestring):
            LHex = ['%s' % binascii.hexlify(i).upper() for i in data]
            return ' '.join(LHex)
        else:
            return None
