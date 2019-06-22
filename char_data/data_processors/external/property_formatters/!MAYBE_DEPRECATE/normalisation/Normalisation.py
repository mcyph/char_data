import unicodedata

from toolkit.encodings.hex_padding import get_uni_point
from toolkit.encodings.surrogates import w_unichr, w_ord

from char_data.data_processors.external.property_formatters import ExternalBaseClass
from char_data.data_processors.consts import HEADER_NORMALISATION


DShortDesc = {
    'NFD': 'NFD Normalisation',
    'NFKD': 'NFKD (Compatibility) Normalisation'
}


class Normalisation(ExternalBaseClass):
    def __init__(self, parent, typ):
        # Can only
        assert typ in ('NFD', 'NFKD')
        self.typ = typ

        ExternalBaseClass.__init__(
            self, parent, HEADER_NORMALISATION, original_name=typ,
            short_desc=DShortDesc[typ], LISOs=None
        )
    
    def raw_data(self, ord_):
        char = w_unichr(ord_)
        
        try: 
            return unicodedata.normalize(self.typ, char)
        except: 
            return None

    def _format_data(self, ord_, data):
        if len(data) > 1:
            i_ord = ' '.join([get_uni_point(w_ord(i)) for i in data])
            return '%s (%s)' % (data, i_ord)
        else:
            return None
