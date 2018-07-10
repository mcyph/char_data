def get_simp_multi_rads():
    # convert DRads Traditional-Simplified
    DTrad, DTradChars = get_trad_multi_rads()
    DSimp = {}

    for rad, LChars in DTrad.items():
        # Go through each radical and get the T-S conversion
        LRads = get_simp_chars(rad, None)  # Rads T-S
        for iRad in LRads:
            for Char in LChars:
                LSubChars = get_simp_chars(Char, DTradChars)  # Chars T-S

                if not iRad in DSimp:
                    DSimp[iRad] = []
                DSimp[iRad].extend(LSubChars)

    # convert DChars Traditional-Simplfied
    DSimpChars = {}

    for Char, LRads in DTradChars.items():
        LChars = get_simp_chars(Char, DTradChars)  # Chars T-S
        for iChar in LChars:
            for iRad in LRads:
                LSubRads = get_simp_chars(iRad, None)  # Rads T-S

                if not iChar in DSimpChars:
                    DSimpChars[iChar] = []
                DSimpChars[iChar].extend(LSubRads)

    return conv_to_array(DSimp), DSimpChars
