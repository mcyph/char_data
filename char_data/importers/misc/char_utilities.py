import os
import codecs

from char_data.data_paths import data_path

# HACK: I'm using absolute paths for now
# but may change later if it needs to be packaged
#UNIPATH = 'Z:/Mirror/David/Unicode/%s'
#UNIPATH = 'Z:/Mirror/David/Unicode2/%s'
#UNIPATH = r'F:\Documents\Uni_\Uni\6.0.0\%s'
UNIPATH = data_path('chardata', 'unidata/src/%s')


def get_code_point(Hex):
    if '..' in Hex:
        # Two hex values - return an int range
        FromHex, ToHex = Hex.split('..')
        return int(FromHex, 16), int(ToHex, 16)
    else:
        # Return a single int
        try: 
            return int(Hex, 16)
        except: 
            print "ERROR:", Hex
            raise


def uni_open(FileName):
    Path = UNIPATH % FileName
    File = codecs.open(Path, 'rb', 'utf-8', 'replace')
    return File


def open_scsv(Path):
    # Open a Unicode file, separated by semicolons
    print Path, os.getcwdu()
    File = uni_open(Path)
    #File = codecs.open_scsv(Path, 'rb', 'utf-8')
    for line in File:
        line = line.split('#')[0].strip()
        if not line: continue
        LLine = [i.strip() for i in line.split(';')]
        #print 'open_scsv line:', LLine
        
        # Output the codepoint as either a 
        # tuple range or a single codepoint
        LLine[0] = get_code_point(LLine[0])
        
        yield LLine
    File.close()


def get_char_gaps(LCodePoints):
    DCodePoints = {}
    for i in LCodePoints:
        if type(i) in (tuple, list):
            # Ignore ranges
            continue
        DCodePoints[i] = None
    #print 'DCodePoints:', DCodePoints.keys()[:100]
    
    # 300000 should be plenty for now
    LRtn = []
    lowGap = 0
    if DCodePoints:
        for hiGap in xrange(max(DCodePoints)+2):
            if hiGap in DCodePoints:
                if (hiGap-lowGap)>70:
                    LRtn.append((lowGap, hiGap-1))
                lowGap = hiGap+1
    #print 'get_char_gaps:', LRtn
    return sorted(LRtn)


def iter_ranges_1(LIgnoreRanges, max_):
    #print 'MAX iter_ranges:', max_
    lastadjCodePoint = -1
    for ord_ in xrange(max_+1):
        
        # TODO: Make this line faster?
        adjCodePoint = get_adjusted_code_point(ord_, LIgnoreRanges)
        
        if adjCodePoint != None:
            # This shouldn't have any gaps in the data so 
            # the result should be 1, 2, 3, ..., 500, 501 etc
            #print ord_, adjCodePoint, lastadjCodePoint
            assert (adjCodePoint-1) == lastadjCodePoint, \
                '(%s-1) != %s' % (adjCodePoint, lastadjCodePoint)
            
            lastadjCodePoint = adjCodePoint
            #print 'ord_:', ord_, 'adjCodePoint:', adjCodePoint
            yield ord_


def iter_ranges_2(LIgnoreRanges, max_):
    low_range = 0
    LRanges = []
    
    if LIgnoreRanges:
        for from_, to in LIgnoreRanges:
            #print from_, to
            LRanges.append((low_range, from_-1))
            if LRanges[-1] == (0, -1):
                del LRanges[-1]
            low_range = to+1
    
    LRanges.append((low_range, max_))
    
    for from_, to in LRanges:
        for i in xrange(from_, to+1):
            #print from_, to, i
            yield i


def iter_ranges(LIgnoreRanges, max_):
    if 1:
        # Skip CPU cycles at an accuracy cost
        for i in iter_ranges_2(LIgnoreRanges, max_):
            yield i
        print 'iter_ranges OK!'
    else:
        # Make sure all ranges are iterated properly 
        # at an exponentially larger processing overhead
        iter_1 = tuple([i for i in iter_ranges_1(LIgnoreRanges, max_)])
        iter_2 = tuple([i for i in iter_ranges_2(LIgnoreRanges, max_)])
        assert iter_1 == iter_2, "%s should be %s" % (iter_2, iter_1)
        print 'iter_ranges OK!'
        
        for i in iter_2: 
            yield i


def get_adjusted_code_point(ord_, LIgnoreRanges):
    """
    Get the codepoint, subtracting the ignored ranges
    """
    i_ord = ord_
    LastTo = -1
    for from_, to in LIgnoreRanges:
        assert LastTo < from_, "Range %s-%s should be less than %s!" % (from_, to, LastTo)
        LastTo = to
        
        if i_ord >= from_ and i_ord <= to:
            # If between an ignored range, return None
            return None
        elif i_ord > from_:
            # If after an ignored range, subtract the difference
            # TODO: Is [+1] correct here?
            ord_ -= (to-from_)+1
        else: 
            # If no more ranges, then stop consuming CPU 
            # cycles (the ranges are sorted in ascending order)
            break
    return ord_
