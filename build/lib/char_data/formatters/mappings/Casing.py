from toolkit.surrogates import w_unichr

class Casing:
    def __init__(self, typ):
        """
        Provides basic lower/upper casing etc
        OPEN ISSUE: Use the Unicode data directly?
        """
        self.typ = typ
        
    def raw_data(self, ord_):
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
    
    def formatted(self, ord_):
        return self.raw_data(ord_)
