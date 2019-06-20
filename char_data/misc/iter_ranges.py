from .get_adjusted_code_point import get_adjusted_code_point


def iter_ranges(LIgnoreRanges, max_):
    if 1:
        # Skip CPU cycles at an accuracy cost
        for i in iter_ranges_2(LIgnoreRanges, max_):
            yield i
        print('iter_ranges OK!')
    else:
        # Make sure all ranges are iterated properly
        # at an exponentially larger processing overhead
        iter_1 = tuple([i for i in iter_ranges_1(LIgnoreRanges, max_)])
        iter_2 = tuple([i for i in iter_ranges_2(LIgnoreRanges, max_)])
        assert iter_1 == iter_2, "%s should be %s" % (iter_2, iter_1)
        print('iter_ranges OK!')

        for i in iter_2:
            yield i


def iter_ranges_1(LIgnoreRanges, max_):
    # print('MAX iter_ranges:', max_)
    lastadjCodePoint = -1

    for ord_ in range(max_ + 1):
        # TODO: Make this line faster?
        adjCodePoint = get_adjusted_code_point(ord_, LIgnoreRanges)

        if adjCodePoint != None:
            # This shouldn't have any gaps in the data so
            # the result should be 1, 2, 3, ..., 500, 501 etc
            # print(ord_, adjCodePoint, lastadjCodePoint)
            assert (adjCodePoint - 1) == lastadjCodePoint, \
                '(%s-1) != %s' % (adjCodePoint, lastadjCodePoint)

            lastadjCodePoint = adjCodePoint
            # print('ord_:', ord_, 'adjCodePoint:', adjCodePoint)
            yield ord_


def iter_ranges_2(LIgnoreRanges, max_):
    low_range = 0
    LRanges = []

    if LIgnoreRanges:
        for from_, to in LIgnoreRanges:
            #print(from_, to)
            LRanges.append((low_range, from_ - 1))
            if LRanges[-1] == (0, -1):
                del LRanges[-1]
            low_range = to + 1

    LRanges.append((low_range, max_))

    for from_, to in LRanges:
        for i in range(from_, to + 1):
            # print(from_, to, i)
            yield i



