
ALLOW_WIDE_CHARS = True


def open_unihan(LPaths, CCDict=False):
    LLines = []
    for path in LPaths:
        if LLines: 
            LLines.append('') # HACK!
        
        with open(path, 'r', encoding='utf-8', errors='replace') as f:
            for line in f:
                '''
                HACK: CCDict sometimes trails lines, for example 
                U+3424.0    fEnglish     implore; beseech; seek after, beg; 
                pray
                So this checks the next line for tabs.
                '''
                
                if line.strip() and line.strip()[0] == '#': 
                    continue # HACK: Ignore comments!
                elif not line.strip(): 
                    continue
                
                if '\t' in line:
                    LLines.append(line.strip('\r\n '))
                elif LLines:
                    LLines[-1] += ' %s' % line.strip('\r\n ')
    
    def get_code_point(uni_hex):
        '''
        Convert a Unicode codepoint (i.e. "U+XXXX") 
        to an integer codepoint.
        '''
        hex_ = "0x" + uni_hex[2:]
        hex_ = hex_.split('.')[0] # CCDict HACK!
        return int(hex_, 16)
    
    last_char = None
    for line in LLines:
        if not line.strip(): 
            continue
        elif line[0] == '#': 
            continue
        elif not line.strip().strip('\t'): 
            continue
        elif line == 'ld': 
            continue
        
        #print line.encode('utf-8')
        LLine = line.split('\t')
        try: 
            uni_hex, key, value = LLine
        except: 
            print(('ERROR ON LINE:', LLine))
            continue
        
        if 'Unihan' in LPaths[0] and key[0] == 'k':
            # Remove e.g. 'k' from 'kDefinition'
            key = key[1:]
        
        ord_ = get_code_point(uni_hex)
        
        if not last_char: 
            last_char = ord_
            D = {'codepoint': ord_}
        
        if (last_char != ord_) and D:
            yield D
            D = {'codepoint': ord_}
        
        last_char = ord_
        D[key] = value
    yield D
