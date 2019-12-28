from char_data.toolkit.encodings.surrogates import w_unichr


def conv_hex(key, s):
    #print 'KEY:', key
    if key == 'Block Subnames' or key == 'Name' or \
        key == 'Unicode 1.0 Name' or \
        key == 'Xiandai Hanyu Pinlu':
        return s # HACK!
    
    elif key == 'Names List' and s.startswith('# '):
        #print 'COMPAT:', s.encode('utf-8')
        try:
            L1 = []
            L2 = []
            
            for hex in s.split():
                try: 
                    assert len(hex) == 4
                    ord_ = int(hex, 16)
                except:
                    # Not hex, e.g. "<super>" in the trademark symbol?
                    L1.append(hex)
                    continue
                
                L1.append('U+%s' % hex)
                L2.append(w_unichr(ord_))
            return '%s (%s)' % (' '.join(L1), ''.join(L2))
        
        except: 
            return s
    
    try: 
        t_s = s.strip('() ')
        hex = t_s.split(' ')[-1].upper().replace('U+', '')
        assert len(hex) == 4
        ord_ = int(hex, 16)
        t_s = ' '.join(t_s.split(' ')[:-1]).strip(' -')
        t_s = '%s U+%s (%s)' % (t_s, hex, w_unichr(ord_))
        #print 'CONVHEX:', t_s.encode('utf-8')
        return t_s.strip()
    except: 
        return s
