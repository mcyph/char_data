def get_multi_rads():
    # Get the Traditional and auto-convert to Simplified data
    # (INTRODUCES ERRORS, but still useful a lot of the time)
    DTradRads, DTradChars = get_trad_multi_rads()
    DSimpRads, DSimpChars = get_simp_multi_rads()

    DBothRads, DBothChars = get_both_multi_rads(
        DSimpRads, DSimpChars,
        DTradRads, DTradChars
    )

    # Get the RadKeys (whatever they are)
    LSimpRadKeys = list(DSimpRads.keys())
    LTradRadKeys = list(DTradRads.keys())
    LSimpRadKeys.sort()
    LTradRadKeys.sort()
    return DBothRads, DBothChars, LSimpRadKeys, LTradRadKeys


get_multi_rads = cache_funct('GetMultiRads', get_multi_rads)
DBothRads, DBothChars, LSimpRadKeys, LTradRadKeys = get_multi_rads()


def get_both_multi_rads(DSimpRads, DSimpChars, DTradRads, DTradChars):
    # Get from both the simplified and traditional radicals
    DBothRads = {}
    for k in DSimpRads:
        if not k in DBothRads:
            DBothRads[k] = []
        DBothRads[k] += DSimpRads[k]
        DBothRads[k] = fast_rem_dupes(DBothRads[k])

    for k in DTradRads:
        if not k in DBothRads:
            DBothRads[k] = []
        DBothRads[k] += DTradRads[k]
        DBothRads[k] = fast_rem_dupes(DBothRads[k])

    DBothChars = {}
    for k in DSimpChars:
        if not k in DBothChars:
            DBothChars[k] = []
        DBothChars[k] += DSimpChars[k]
        DBothChars[k] = fast_rem_dupes(DBothChars[k])

    for k in DTradChars:
        if not k in DBothChars:
            DBothChars[k] = []
        DBothChars[k] += DTradChars[k]
        DBothChars[k] = fast_rem_dupes(DBothChars[k])
    return conv_to_array(DBothRads), DBothChars

