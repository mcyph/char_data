from toolkit.encodings.hex_padding import get_uni_point
from toolkit.encodings.surrogates import w_unichr

from char_data.storage.data.read import Encoding


class UnicodeHex(Encoding):
    def _format_data(self, ord_, data):
        # TODO: If the data is in decimal, return a visual representation:
        # %(Repr)s (U+%(hex)s)[padded to 4 OR 8 hex digits depending on size]
        # If the data is string, split into the right side of <, -, : etc
        # and convert the hex on the left hand side
        #print 'FORMATUHEX:', key, data
        
        if not data:
            return None
        
        elif type(data) in (str, unicode):
            pass
        
        elif type(data) in (list, tuple):
            #print 'LIST/TUPLE IN FORMATUHEX!'
            LRtn = []
            for ord_, flags in data:
                char = w_unichr(ord_)
                # TODO: PAD the HEX DIGITS!
                
                a = '%s (%s)' % (char, get_uni_point(ord_))
                LFlags = self.get_L_by_flags(flags)
                
                if LFlags:
                    LRtn.append('%s: %s' % (','.join(LFlags), a))
                else:
                    LRtn.append(a)
            data = ' '.join(LRtn)
        
        return data
