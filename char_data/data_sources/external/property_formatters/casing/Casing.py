from toolkit.encodings.surrogates import w_unichr

from char_data.data_sources.external.property_formatters import ExternalBaseClass
from char_data.data_sources.consts import HEADER_CASING


DDesc = {
    'lower': 'Lowercased',
    'upper': 'Uppercased',
    'title': 'Titlecased',
    'capitalize': 'Capitalized'
}


class Casing(ExternalBaseClass):
    def __init__(self, parent, typ):
        """
        Provides basic lower/upper casing etc
        OPEN ISSUE: Use the Unicode data directly?
        """
        self.typ = typ

        ExternalBaseClass.__init__(
            self, parent, HEADER_CASING, original_name=typ,
            short_desc=DDesc[typ], LISOs=FIXME
        )
        
    def raw_data(self, ord_, data):
        char = w_unichr(ord_)

        if self.typ == 'lower':
            return char.lower()
        elif self.typ == 'upper':
            return char.upper()
        elif self.typ == 'title':
            return char.title()
        elif self.typ == 'capitalize':
            return char.capitalize()
        else:
            raise Exception("unknown casing type %s" % self.typ)
    
    def _format_data(self, ord_, data):
        return data
