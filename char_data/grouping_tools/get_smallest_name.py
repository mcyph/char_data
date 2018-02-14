def get_smallest_name(LName):
    """
    Most of the time, e.g. in "latin small letter z with swash tail"
    the "z" is the smallest part, and allows easy sorting.
    Therefore, get the smallest characters to allow grouping.
    """
    cur_len = 32768 # ??? ==============================================================
    
    DNameExc = {
        'latin small letter n preceded by apostrophe': 'n',
        'latin small letter sharp s': 'ss',
        'feminine ordinal indicator': 'a', # SPANISH HACK!
        'masculine ordinal indicator': 'o' # SPANISH HACK!
    }
 
    if LName[-1] in DNameExc:
        return DNameExc[LName[-1]]
    else:
        LNames = LName[-1].split()
    
    DExc = {
        'alpha': 'a',
        'eng': 'n',
        'esh': 's',
        'ezh': 'z',
        'is': 's',
        'schwa': 's',
        'gamma': 'g',
        'phi': 'f', # alike to Cyrillic 'ef'
        'lambda': 'l',
        'hwair': 'h',

        # Controversial characters
        'thorn': 't',
        'delta': 'd',
        'laryngeal': 'l',
        'upsilon': 'u',
        'kelvin': 'k',
        'angstrom': 'a',

        'stop': 'zz', # Glottal stop?
        'click': 'zz',
        'sign': 'zz',
        'combining': 'zz',
        'arrow': 'zz',
        'at': 'zz',
        'asterisk': 'zz',
        'square': 'zz',
        'broken': 'zz',
        'colon': 'zz',
        'light': 'zz',
        'semicolon': 'zz',
        'accent': 'zz',
        'hyphen-minus': 'zz',
        'ampersand': 'zz',
        'parenthesis': 'zz',
        'digit': 'zz',
        'numeral': 'zz',
        'solidus': 'zz',
        'bracket': 'zz',
        'mark': 'zz'
    }
    
    LNums = (
        'one', 'two', 'three', 'four', 'fifty', 'five',
        'six', 'seven', 'eight', 'nine', 'ten'
    )
    
    LSpecial = (
        'comma', 'dot', 'line', 'apostrophe', 'tilde',
        'macron'
    )
    
    if [i for i in LNames if i in LNums]:
        return 'zz'
    elif any((i in LNames) for i in LSpecial) and not 'with' in LNames:
        return 'zz'
    
    for name in LNames:
        if name=='big' or LName=='small':
            continue
        elif name == 'with':
            continue
        
        if name in DExc:
            return DExc[name]
        elif len(name) < cur_len:
            rtn = name
            cur_len = len(name)
    
    #print 'SMALLESTNAME:', LNames, rtn
    #if rtn == 'ef': 
    #    rtn = 'f' # CYRILLIC HACK!
    
    if rtn == 'latin': 
        return 'zz' # HACK!
    return rtn
