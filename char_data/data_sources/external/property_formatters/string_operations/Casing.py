from toolkit.encodings.surrogates import w_unichr

from char_data.data_sources.external.property_formatters import ExternalBaseClass


class Casing(ExternalBaseClass):
    def __init__(self, typ):
        """
        Provides basic lower/upper casing etc
        OPEN ISSUE: Use the Unicode data directly?
        """
        self.typ = typ
        
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
