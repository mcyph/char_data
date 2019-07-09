from toolkit.escape import E
from toolkit.json_tools import dumps, loads
from toolkit.encodings.surrogates import w_unichr
from toolkit.encodings.hex_padding import get_uni_point
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
        if isinstance(data, str) and data.startswith('[') and data.endswith(']'):
            value = loads(data)

            LOut = []

            for i_tuple in value:
                assert isinstance(i_tuple, (list, tuple))

                if len(i_tuple) == 2:
                    # See also, e.g. [96, "grave accent"]
                    # for combining grave accents
                    LOut.append(
                        f'{ get_uni_point(i_tuple[0]) } '
                        f'{ w_unichr(int(i_tuple[0])) } '
                        f'{ i_tuple[1] }'
                    )

                elif len(i_tuple) == 3:
                    if isinstance(i_tuple[0], (list, tuple)):
                        # e.g. [[[65, 769], null, null]] as in combining char decompositions
                        codepoints = ''
                        uni_chars = ''

                        for codepoint in i_tuple[0]:
                            codepoints += f"{ get_uni_point(codepoint) } "
                            uni_chars += f"{ w_unichr(codepoint) }"

                        LOut.append(
                            f'{ codepoints.strip() } { uni_chars } '
                            f'{ str(i_tuple[1]) if i_tuple[1] else "" } '
                            f'{ str(i_tuple[2]) if i_tuple[2] else "" }'
                        )
                    else:
                        # ???
                        LOut.append(
                            f'{ get_uni_point(i_tuple[0]) } '
                            f'{ w_unichr(i_tuple[0]) } '
                            f'{ str(i_tuple[1:]) }'
                        )

            if LOut:
                return LOut
        return data
