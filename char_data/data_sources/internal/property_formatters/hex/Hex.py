from toolkit.encodings.hex_padding import get_hex_point
from char_data.data_sources.internal.data.read import Encoding


class Hex(Encoding):
    def _format_data(self, ord_, data):
        # TODO: If the data is in hex, return a visual representation:
        # %(hex)s[padded to 4 hex digits separated by spaces]
        # If the data is string, split into the right side of <, -, : etc
        # and convert the hex on the left hand side
        if not data:
            return None
        
        elif type(data) in (str, unicode):
            pass
        
        elif type(data) in (list, tuple):
            #print 'LIST/TUPLE IN FORMATHEX!'
            LRtn = []
            for ord_, flags in data:
                # TODO: PAD the HEX DIGITS!
                
                a = get_hex_point(ord_)
                LFlags = self.get_L_by_flags(flags)
                
                if LFlags:
                    LRtn.append('%s: %s' % (','.join(LFlags), a))
                else:
                    LRtn.append(a)
            data = '; '.join(LRtn)
        
        return data
