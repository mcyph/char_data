from char_data.misc import get_font_script, get_smallest_name


def get_L_unicode_name_headings(LRanges, name=None):
    from char_data import char_data

    if name is None:
        first_ord = LRanges[0]
        if type(first_ord) == tuple:
            first_ord = first_ord[0]

        script = char_data.raw_data('unicodedata.script', first_ord)
        name = script if script else None
        #print '**NAME:', name

    LRtn = []
    font_script = None
    
    for ord_ in LRanges:
        if type(ord_) == tuple:
            # A range. If the first BlockName item is None and the last item is None
            # OR the last BlockName doesn't equal the first BlockName
            from_, to = ord_
            
            #if FirstCodePoint is None:
            #    for i_code in xrange(from_, to+1):
            #        #print 'SUBTUPLE FALLBACK!'
            #        font_script = get_fallback(i_code)
            #        if font_script: break
            
            for i_code in range(from_, to+1):
                name = char_data.formatted('unicodedata.name', i_code)
                if not name:
                    name = '(Unknown)'
                else:
                    append = get_smallest_name(
                        name
                        #CharData.get_L_names(i_code, types=('general',))[0]
                    )
                
                if name=='Cyrillic' and append[0]=='e' and len(append)>1:
                    append = append[1] # HACK: fix e.g. 'ef' and 'em' and 'es' (f/m/s)
                
                LRtn.append((append, i_code))
            
        else: 
            # A codepoint, only one SubName required
            
            #if FirstCodePoint is None:
                #print 'SUBSINGLE FALLBACK!'
                #font_script = get_fallback(ord_)

            name = char_data.formatted('unicodedata.name', ord_)
            if not name:
                name = '(Unknown)'
            else:
                append = get_smallest_name(
                    name
                    #CharData.get_L_names(ord_, Types=('general',))[0]
                )
            
            if name=='Cyrillic' and append[0]=='e' and len(append)>1:
                append = append[1] # HACK: fix e.g. 'ef' and 'em' and 'es' (f/m/s)
            
            LRtn.append((append, ord_))
    
    #if not font_script: font_script = 'All'
    LRtn.sort()
    
    n_LRtn = []
    n_LRtn.append(('block', name)) # HACK!
    
    last_key = None
    for sort_key, ord_ in LRtn:
        if not font_script:
            font_script = get_font_script(ord_)
        
        if sort_key == 'zz': # zz are Symbols - probably shouldn't be in Latin :-P
            chk_key = 'zz'
        else: 
            chk_key = sort_key[0]
        
        if last_key != chk_key:
            last_key = chk_key
            
            if chk_key == 'zz':
                n_LRtn.append(
                    ['sub_block', ['Miscellaneous Symbols', None]]
                )
            else: 
                n_LRtn.append(
                    ['sub_block', ['characters starting with "%s"' % chk_key.lower(), None]]
                )
            
            n_LRtn.append(['chars', []])
        n_LRtn[-1][-1].append(ord_)
    
    #LRtn = [['chars', [i[1] for i in LRtn]]]
    return font_script, n_LRtn


if __name__ == '__main__':
    print((get_L_unicode_name_headings([ord('e'), ord('c')])))

