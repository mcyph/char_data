def get_char_gaps(LCodePoints):
    DCodePoints = {}

    for i in LCodePoints:
        if type(i) in (tuple, list):
            # Ignore ranges
            continue
        DCodePoints[i] = None
    # print('DCodePoints:', DCodePoints.keys()[:100])

    # 300000 should be plenty for now
    LRtn = []
    lowGap = 0

    if DCodePoints:
        for hiGap in range(max(DCodePoints) + 2):
            if hiGap in DCodePoints:
                if (hiGap - lowGap) > 70:
                    LRtn.append((lowGap, hiGap - 1))
                lowGap = hiGap + 1

    # print('get_char_gaps:', LRtn)
    return sorted(LRtn)
