DFallbackExc = {
    #'Hiragana': 'Japanese',
    #'Katakana': 'Japanese',
    #'Han': 'All', # FIXME!
    #'Hangul': 'Korean',
    #'Bopomofo': 'ChineseTraditional'
}


def get_font_script(ord_):
    """
    HACK: Get the fallback from the first character
    """
    from char_data import char_data

    try:
        font_script = char_data.formatted('script', ord_)
    except KeyError:
        # WARNING! =====================================================================================================
        font_script = None

    if (font_script=='Common' or font_script=='Inherited') and False:
        # HACK: Keep trying for Common/Inherited as e.g. Arabic might
        # have common punctuation marks but should use the Arabic fallback
        return None

    if font_script in DFallbackExc:
        font_script = DFallbackExc[font_script]

    #print 'FALLBACK:', font_script, ord_
    return font_script
