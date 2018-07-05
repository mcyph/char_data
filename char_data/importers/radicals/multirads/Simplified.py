from char_data import raw_data
from toolkit.encodings.surrogates import w_unichr, w_ord


def get_simp_chars(Char, DTradChars=None):
    if type(Char) == int:
        Char = w_unichr(Char)
    
    LSubChars = []
    if DTradChars:
        # convert the converted characters/radicals Traditional-Simplified
        LVariants = ['unihan.simplifiedvariant',
                     'unihan.semanticvariant', # CHECK ME!
                     'unihan.specializedsemanticvariant', # CHECK ME!
                     'unihan.zvariant']
        
        for Variant in LVariants:
            V = raw_data(Variant, w_ord(Char))
            if V:
                LSubChars += [w_unichr(i) for i in V]
                print 'Char:', Char.encode('utf-8'), 'LSubChars:', ''.join(LSubChars).encode('utf-8'), 'V:', V
    
    # Use the transliteration system to convert from T-S,
    # only allowing if different and MultiRad data not 
    # already available for that character
    from multi_translit.translit.TranslitEngine import get_engine
    TradToSimp = get_engine('Chinese Traditional-Simplified')
    Conv = TradToSimp.convert(Char)
    LSubChars.append(Conv)
    
    # HACK: Make sure characters that are already 
    # Traditional aren't converted so information isn't lost!
    # NOTE: This shouldn't be performed for RADICAL conversion, 
    # just the CHARS as it can stuff up the radical lists :-(
    if DTradChars: 
        LSubChars = [i for i in LSubChars if not i in DTradChars]
    return rem_dupes(LSubChars)


def get_simp_multi_rads():
    # convert DRads Traditional-Simplified
    DTrad, DTradChars = get_trad_multi_rads()
    DSimp = {}
    for rad, LChars in DTrad.items():
        # Go through each radical and get the T-S conversion
        LRads = get_simp_chars(rad, None) # Rads T-S
        for iRad in LRads:
            for Char in LChars:
                LSubChars = get_simp_chars(Char, DTradChars) # Chars T-S
                if not iRad in DSimp: DSimp[iRad] = []
                DSimp[iRad].extend(LSubChars)
    
    # convert DChars Traditional-Simplfied
    DSimpChars = {}
    for Char, LRads in DTradChars.items():
        LChars = get_simp_chars(Char, DTradChars) # Chars T-S
        for iChar in LChars:
            for iRad in LRads:
                LSubRads = get_simp_chars(iRad, None) # Rads T-S
                if not iChar in DSimpChars: DSimpChars[iChar] = []
                DSimpChars[iChar].extend(LSubRads)
    return conv_to_array(DSimp), DSimpChars
