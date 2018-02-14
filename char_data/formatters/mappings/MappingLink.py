from toolkit.json_tools import dumps
from char_data.datatypes.read import StringData
from char_data.datatypes.write.write_string_data import write_string_data

def write(f, key, DOrds):
    n_DOrds = {}
    for ord_, value in DOrds.items():
        n_DOrds[ord_] = dumps(value) # MULTIPLE VALUE WARNING! ===========================================
    
    return write_string_data(f, key, n_DOrds)

class MappingLink(StringData):
    writer = staticmethod(write)
    
    def __init__(self, key, f, DJSON):
        """
        Intended to provide for 'block see also', 'see also':
        (codepoint, name)
         
        'decomposed form', 'compatibility mapping'
        (mapping, mapping type, name) 
        
        and pretty-print the above data
        """
        StringData.__init__(self, key, f, DJSON)
    
    def formatted(self, ord_):
        # TODO: Provide a pretty link etc!
        return self.raw_data(ord_)
    