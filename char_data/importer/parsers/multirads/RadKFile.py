from __future__ import with_statement
import codecs
from toolkit.rem_dupes import fast_rem_dupes


def get_D_rads(path):
    '''
    Open the "radkfile" and "radkfile2" euc-jp 
    multiradical files by Michael Raine and Jim Breen
    http://www.csse.monash.edu.au/~jwb/kradinf.html
    
    returns {radical: [kanji, ...], ...}
    '''
    rad = None
    DRads = {}
    LChars = []
    
    with codecs.open(path, 'rb', 'euc-jp') as f:
        for line in f:
            line = line.rstrip('\r\n')
            
            if not line: 
                continue
            
            if line[0] == '#': 
                # Ignore comments
                continue
            
            elif line[0] == '$':
                # Add previous item to DChars/DRads
                if rad:
                    DRads.setdefault(rad, []).extend(LChars)
                
                # Change radical/number strokes
                LLine = line.strip().split()
                
                rad = LLine[1]
                LChars = []
            else:
                # Add to list of characters
                LChars.extend(line.strip())
    
    # Add the last item
    DRads.setdefault(rad, []).extend(LChars)
    return DRads


def get_D_kanji(DRads):
    '''
    Reverses the result from `get_D_rads` above
    returns {kanji: [radical, ...], ..}
    '''
    DRtn = {}
    for radical, LChars in DRads.items():
        for char in LChars:
            DRtn.setdefault(char, []).append(radical)
    return DRtn


def combine_radkfile_2(DRads1, DRads2):
    for rad, LKanji in DRads2.items():
        L = DRads1.setdefault(rad, [])
        L.extend(LKanji)
        DRads1[rad] = fast_rem_dupes(L)
    return DRads1
