# -*- coding: utf-8 -*-
from _kangxi_data import KANGXI_BOTH, KANGXI_SIMPLIFIED, KANGXI_TRADITIONAL


def get_D_rads():
    RADS = _get_rads(KANGXI_BOTH)
    
    D = {}
    for line in RADS.split('\n'):
        line = line.strip('\r\n').strip()
        line = line.split()
        
        strokes, key, radical = line[:3]
        english = ' '.join(line[3:])
        
        if key in D: 
            D[key].append([strokes, radical, english])
        else: 
            D[key] = [[strokes, radical, english]]
    return D


def get_D_multi_to_rad_num():
    DRtn = {}
    DRads = get_D_rads()
    for RadNum in DRads:
        for L in DRads[RadNum]:
            for Char in L[1]:
                DRtn[Char] = RadNum
    return DRtn


def get_rads(kangxi_kind):
    RADS = _get_rads(kangxi_kind)
    
    DSimp = {}
    LList = []
    LIndex = []
    
    for line in RADS.split('\n'):
        line = line.strip('\r\n').strip()
        LLine = line.split()
        if "'" in line:
            DSimp[' '.join(LLine[3:])] = None
        
    for line in RADS.split('\n'):
        line = line.strip('\r\n').strip()
        LLine = line.split()
        
        if not is_trad and ' '.join(LLine[3:]) in DSimp and not "'" in line:
            # Use the simplified form as needed.
            # TODO: What if the simplified form 
            # is SHORTER than the traditional form?
            #print 'IGNORING:', line.encode('utf-8')
            continue
            
        elif is_trad == True and "'" in line: 
            continue
        else: 
            pass # Get all!
        
        if len(LLine) == 3: 
            LList.append('%s %s' % (LLine[0], LLine[2]))
            LIndex.append(LLine[1])
        elif len(LLine) > 3: 
            LList.append('%s %s %s' % (LLine[0], LLine[2], ' '.join(LLine[3:])))
            LIndex.append(LLine[1])
        else: 
            raise Exception
    return LList, LIndex


def get_i_rads():
    import os
    os.chdir('../')
    
    RADS = _get_rads(KANGXI_BOTH)
    
    LList = []
    for line in RADS.split('\n'):
        line = line.strip('\r\n').strip()
        LLine = line.split()
        LList.append([LLine[1], LLine[2]])
    return LList


"""L = []; i = 0
for Rad, Chr in get_i_rads():
    Name = unicodedata.name(unichr(int(Rad.strip("'"))+12031)).replace('KANGXI RADICAL ', '').lower()
    try: strokes = Unihan.Select(['strokes'], 'Word', unicode(Chr))
    except: strokes = None
    #print strokes
    
    #print Name
    if strokes: L.append([int(strokes[0]), Name, Rad, Chr])
    else: print 'ERROR:', i, Name, Chr.encode('utf-8')
    i += 1
L.sort()


for i in L:
    print i[0], i[2], i[3].encode('utf-8'), i[1]

#print L"""
