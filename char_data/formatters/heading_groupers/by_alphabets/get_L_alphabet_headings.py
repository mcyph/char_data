from lang_data import LangData
from iso_tools.ISOTools import ISOTools


def get_L_alphabet_headings(search):
    """
    The headings are actually provided by the CLDR data directly,
    so if using the alphabet key, grab directly from the original source!
    """
    ld = LangData(search)
    script = ISOTools.split(ISOTools.guess_omitted_info(search)).script
    from char_data.unicodeset import unicodeset_from_range

    LRtn = []
    for heading, ranges_string in ld.get_L_alpha():
        LOut = []
        for i_s in unicodeset_from_range(ranges_string):
            LOut.extend([ord(i) for i in i_s])
        #LRtn.extend(LOut)

        LRtn.append(('block', (heading, '')))
        LRtn.append(('chars', LOut))
        # LRtn.append((heading, LOut))

    for typ1, typ2, i_L in ld.get_L_symbols():
        for heading, chars in i_L:
            if typ2:
                # ??? What does typ1/typ2 do again??
                heading = '%s %s' % (typ2, heading)

            if typ1:
                heading = '%s %s' % (typ1, heading)

            if heading.startswith("latn") and script != 'Latn':
                # Ignore Latin perMille etc for langauge which don't use Latin scripts
                continue

            if heading.startswith('arab') and script != 'Arab':
                # Ignore arabic group, etc for languages which don't use the Arabic script
                continue

            LExtend = [ord(i) for i in chars]
            LRtn.append(('block', (heading, '')))
            LRtn.append(('chars', LExtend))
            #LRtn.extend(LExtend)
            # LRtn.append((heading, LExtend))

    #from pprint import pprint
    #pprint(LRtn)

    # ld.get_currency_symbol()
    # ld.locale_pattern()
    # ld.ellipsis()
    # ld.quotes('')
    # ld.paranthesis('')
    return LRtn