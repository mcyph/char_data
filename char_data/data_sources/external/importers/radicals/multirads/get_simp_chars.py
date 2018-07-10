from char_data import char_data
from toolkit.encodings.surrogates import w_unichr, w_ord


def get_simp_chars(Char, DTradChars=None):
    if type(Char) == int:
        Char = w_unichr(Char)

    LSubChars = []

    if DTradChars:
        # convert the converted characters/radicals Traditional-Simplified
        LVariants = [
            'unihan.simplifiedvariant',
            'unihan.semanticvariant', # CHECK ME!
            'unihan.specializedsemanticvariant', # CHECK ME!
            'unihan.zvariant'
        ]

        for Variant in LVariants:
            V = char_data.raw_data(Variant, w_ord(Char))
            if V:
                LSubChars += [
                    w_unichr(i) for i in V
                ]
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
        LSubChars = [
            i for i in LSubChars if not i in DTradChars
        ]

    return rem_dupes(LSubChars)
