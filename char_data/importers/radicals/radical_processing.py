import sys, os

if __name__ == '__main__':
    os.chdir('../../')
    sys.path.append(os.getcwdu())

#from Chars.CharData import CharData
#import MultiRad # HACK!
#from MultiRad import get_L_multi_rads # in Chars

# Chinese Frequency
# Hong Kong Grade
# IICore
# Japanese Frequency
# Japanese Grade

# NOTE: RSUnicode is essentially the same as RSKangXi so I've excluded it
DRadTypes = {
    'Chinese Unified Radicals': (
        'Both', 'Unicode RS', ('Chinese Frequency',
                               'Hong Kong Grade',
                               'Japanese Frequency')
    ),
    'Chinese Simplified Radicals': (
        False, 'Unicode RS', ('Chinese Frequency',
                               'Hong Kong Grade', 
                               'Japanese Frequency')
    ),
    'Chinese Traditional Radicals': (
        True, 'Unicode RS', ('Chinese Frequency',
                             'Hong Kong Grade',
                             'Japanese Frequency')
    ),
    'Japanese Radicals': (
        True, ('Japanese', 'Unicode RS'), ('Japanese Grade',
                                           'Japanese Frequency')
    ),
    'Korean Radicals': (
        True, ('Korean RS', 'Unicode RS'), ('Chinese Frequency',
                                            'Hong Kong Grade',
                                            'Japanese Frequency')
    ),  # FIXME!
    'Tang Radicals': (
        True, 'Unicode RS', ('Chinese Frequency',
                             'Hong Kong Grade',
                             'Japanese Frequency')
    ),  # FIXME!
    'Vietnamese Radicals': (
        True, 'Unicode RS', ('Chinese Frequency',
                             'Hong Kong Grade',
                             'Japanese Frequency')
    )
}  # FIXME!


'''
def get_rad_list(Key):
    # TODO: Do MultiRads have different radical characters?
    LRadInfo = DRadTypes[Key]
    ListType = 'MultiRadSel' # HACK!
    Traditional = LRadInfo[0]
    
    if ListType in ('Radicals', 'MultiRadSel'):
        # TODO: Add radical support!
        # Returns [[ListType, RadColumn, Traditional], 
        #          [[RadVal, RadChar, RadEnglish], ...]]
        if ListType == 'MultiRadSel': 
            RadColumn = None
            LRtn = [(i[0], i[0], ' '.join(i[1])) for i in get_multi_rads(Traditional)]
        elif ListType == 'Radicals': 
            RadColumn = LRadInfo[0]
            ListType = 'Radical' # HACK!
            LRads, LIdx = Radical.get_rads(Traditional)
            LRtn = []; i = 0
            for Rad in LRads:
                RadVal = LIdx[i]
                #print 'RadVal:', RadVal
                #print 'Rad:', Rad.encode('utf-8')
                LRtn.append((RadVal, Rad.split()[1], Rad))
                i += 1
        LRtn = [[ListType, RadColumn, Traditional], LRtn]
    else: 
        raise Exception("Unknown ListType %s" % ListType)
'''


def compress_rads():
    DIsTrad = {}
    for Key in DRadTypes:
        DIsTrad[Key] = DRadTypes[Key][0]
    
    LTrad = [(i[0], i[0], ' '.join(i[1])) for i in get_L_multi_rads(Trad=0)]
    LSimp = [(i[0], i[0], ' '.join(i[1])) for i in get_L_multi_rads(Trad=1)]
    
    LRtn = []
    for L in LTrad:
        # Number strokes/english name
        SortKey = (int(L[2].split()[0]), 
                   ''.join(L[2].split()[2:]).lower())
        
        if L in LSimp: 
            LRtn.append((SortKey, L, 2))
        else: 
            LRtn.append((SortKey, L, 0))
    
    for L in LSimp:
        # Number strokes/english name
        SortKey = (int(L[2].split()[0]),
                  ''.join(L[2].split()[2:]).lower())
        
        if L in LTrad: 
            continue # Already added :-)
        else: 
            LRtn.append((SortKey, L, 1))
    
    LRtn.sort()
    LRtn = [(i[1], i[2]) for i in LRtn]
    return DIsTrad, LRtn


if __name__ == '__main__':
    print compress_rads()
