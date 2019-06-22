from toolkit.json_tools import dumps
from char_data.data_processors.internal.data_types.read import StringData
from char_data.data_processors.internal.data_types.write.write_string_data import write_string_data


def write(f, key, DOrds):
    n_DOrds = {}
    for ord_, value in list(DOrds.items()):
        n_DOrds[ord_] = dumps(value) # MULTIPLE VALUE WARNING! ===========================================
    
    return write_string_data(f, key, n_DOrds)


class MappingLink(StringData):
    writer = staticmethod(write)
    
    """
    Intended to provide for 'block see also', 'see also':
    (codepoint, name)
     
    'decomposed form', 'compatibility mapping'
    (mapping, mapping type, name) 
    
    and pretty-print the above data
    """

    def _format_data(self, ord_, data):
        # TODO: Provide a pretty link etc!
        return data
