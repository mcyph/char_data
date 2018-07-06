def get_adjusted_code_point(ord_, LIgnoreRanges):
    """
    Get the codepoint, subtracting the ignored ranges
    """
    i_ord = ord_
    last_to = -1

    for from_, to in LIgnoreRanges:
        assert last_to < from_, "Range %s-%s should be less than %s!" % (from_, to, last_to)
        last_to = to

        if i_ord >= from_ and i_ord <= to:
            # If between an ignored range, return None
            return None
        elif i_ord > from_:
            # If after an ignored range, subtract the difference
            # TODO: Is [+1] correct here?
            ord_ -= (to - from_) + 1
        else:
            # If no more ranges, then stop consuming CPU
            # cycles (the ranges are sorted in ascending order)
            break

    return ord_
