import binascii
from toolkit.encodings.surrogates import w_unichr
#from Dicts.Other.Import.DelimText import Encodings

from char_data.data_processors.external.ExternalFormatterBase import ExternalFormatterBase
from char_data.data_processors.consts import HEADER_ENCODING


class EncodingFormatter(ExternalFormatterBase):
    def __init__(self, parent, encoding, for_languages, LISOs=None):
        self.encoding = encoding
        self.for_languages = for_languages

        ExternalFormatterBase.__init__(
            self, parent, HEADER_ENCODING, original_name=encoding,
            short_desc='%s (%s)' % (encoding, for_languages),
            LISOs=LISOs
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
            from traceback import print_exc
            #print_exc()
            return None
    
    def _format_data(self, ord_, data):
        if isinstance(data, bytes):
            LHex = [hex(i)[2:] for i in data]
            return ' '.join(LHex)
        else:
            return None
