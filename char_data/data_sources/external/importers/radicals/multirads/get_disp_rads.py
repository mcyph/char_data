# -*- coding: utf-8 -*-


def get_disp_rads(Trad):
    # Returns [[NumStrokes, RadChars, EngDef], ...]

    # TODO: Should there be Japanese-specific info?
    # print 'get_disp_rads:', Trad
    if Trad == 'Both':
        LKeys = fast_rem_dupes(LTradRadKeys + LSimpRadKeys)
        LKeys = list(LKeys)
        LKeys.sort()
    elif Trad:
        LKeys = LTradRadKeys
        # LKeys.sort()
    else:
        LKeys = LSimpRadKeys
        # LKeys.sort()

    LRtn = []

    for rad in LKeys:
        LFound = []
        LNames = [i[-1] for i in CharData.get_L_names(ord(rad)) if i[-1]]
        tName = LNames[0].split(',')[0].split(';')[0]
        if False or 'KangXi' in tName or 'radical' in tName.lower():
            # If True, use the existing radical definition in Radicals
            for Key in DRadicals:
                for strokes, Radical, EngName in DRadicals[Key]:
                    if rad in Radical:
                        LFound.append([int(strokes), rad, EngName])

        if not LFound:
            # If not found or the existing radical def disabled above, get from Unihan
            strokes = CharData.raw_data('Chinese strokes', ord(rad))

            if strokes != None:
                strokes = int(strokes)
            else:
                try:
                    strokes = DStrokeCounts[rad]
                except:
                    print 'RAD STROKE ERROR in get_disp_rads:', rad.encode('utf-8')
                    continue
            name = LNames[0].replace('fullwidth ', '').replace('katakana letter ', 'katakana ')

            # Add Kanjidic definition
            if len(LNames) > 1: name = '%s; %s' % (name, LNames[1])
            LFound.append([strokes, rad, name])

        if LFound[0][1] == u'尚':
            # HACK: THIS CHARACTER DOESN'T SEEM TO BE ENCODED!
            # THIS RADICAL IS ASSIGNED WRONGLY/HAS THE WRONG MEANING!
            # It's actually 5 strokes (like a lid with three dots above)
            LRtn.append([5, u'尚学', 'roof with three lines above, lid'])
            LRtn.append([3, u'尚学', 'three lines above'])
        else:
            LRtn.append(LFound[0])

        # 辶 has multiple stroke values depending on Japanese/Chinese
        # (2/3/4 strokes), so add that as an alias
        if rad == u'辶':
            LRtn.append([2, rad, name])
            LRtn.append([3, rad, name])

    def append_rads(L, Trad):
        # Append the "normal" rads (i.e. the ones not in the
        # "multirad" to allow accessing all radicals)
        import Radical

        Lst, Idx = Radical.get_rads(Trad)
        DAppended = {}
        DMap = {}
        for NumStrokes, RadChars, EngDef in L:
            for c in RadChars: DAppended[c] = ''

        for rad in Lst:
            LRad = rad.split(' ')
            NumStrokes = int(LRad[0])
            RadChars = LRad[1]
            EngDef = ' '.join(LRad[2:])

            Found = False
            for RadChar in RadChars:
                if RadChar in DAppended:
                    Found = True

            for RadChar in RadChars:
                for iChar in RadChars:
                    if not iChar in DMap:
                        DMap[iChar] = ''
                    DMap[iChar] += ''.join([i for i in RadChar if not i in DAppended])

            if not Found:
                for RadChar in RadChars: DAppended[RadChar] = None
                print 'APPENDRADS:', RadChar.encode('utf-8')
                L.append((str(NumStrokes), RadChars, EngDef))

        nL = []
        for NumStrokes, RadChars, EngDef in L:
            # Append "alternate" characters
            oRadChars = RadChars
            for Char in RadChars:
                if Char in DMap and DMap[Char]:
                    oRadChars += DMap[Char]
                    for iChar in DMap[Char]:
                        DMap[iChar] = ''
                    DMap[Char] = ''
            RadChars = ''.join(fast_rem_dupes(oRadChars))
            nL.append((NumStrokes, RadChars, EngDef))
        return nL

    LRtn = append_rads(LRtn, Trad)

    # Sort by strokes -> English Def -> Radical
    LRtn = [((i[0], i[2].lower(), i[1]), i) for i in LRtn]
    LRtn.sort()
    LRtn = [i[1] for i in LRtn]

    nL = []
    for strokes, rad, name in LRtn:
        try:
            nL.append([rad, '%s\t%s\t%s' % (strokes, rad, name)])
        except:
            print 'MULTIRAD ERROR:', [strokes, rad, name]
    return nL


get_disp_rads = cache_funct('GetDispRads', get_disp_rads)