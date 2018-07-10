# -*- coding: utf-8 -*-
import array
import codecs
from Radical import get_D_rads
from toolkit.list_operations.rem_dupes import fast_rem_dupes, rem_dupes
from toolkit.caching.cache_funct import cache_funct
from input.WidthConv import full_to_halfwidth
DRadicals = get_D_rads()
#from Chars.CharData import CharData # FIXME! ====================================================


'''
if rad in DAlternate:
    rad = DAlternate[rad]

if rad in DRadAliases:
    print 'ADDING ALIAS:', rad.encode('utf-8')
    key = DRadAliases[rad][-1]
    
    if not key in DRads: 
        DRads[key] = ''
    
    DRads[key] += ''.join(LChars)
    
    for char in LChars: 
        DChars[char] += key # Add to DChars

if rad in DRadAppend:
    # Add aliases to disambiguate more complicated radicals
    # TODO: What if there're DUPES?
    print 'APPENDING:', rad.encode('utf-8')
    
    for iRad in DRadAppend[rad]:
        if not iRad in DRads: 
            DRads[iRad] = ''
        
        DRads[iRad] += DRads[rad]
        
        for char in LChars: 
            DChars[char] += rad # Add to DChars

if rad in DRadAppend:
    # Add aliases to disambiguate more complicated radicals
    # TODO: What if there're DUPES?
    print 'APPENDING:', rad.encode('utf-8')
    
    for iRad in DRadAppend[rad]:
        if not iRad in DRads: 
            DRads[iRad] = ''
        
        DRads[iRad] += DRads[rad]
        
        for char in LChars: 
            DChars[char] += rad # Add to DChars

if rad in DRadAliases:
    print 'ADDING ALIAS:', rad.encode('utf-8')
    key = DRadAliases[rad][1]
    
    if not key in DRads: 
        DRads[key] = ''
    
    DRads[key] += ''.join(LChars)
    
    for char in LChars: 
        DChars[char] += key # Add to DChars
'''


def get_L_multi_rads(Trad):
    if Trad == 'Both': Rads = LBothRads
    elif Trad: Rads = LTradRads
    else: Rads = LSimpRads
    return Rads


# CHECK ME!
LTradRads = [(i[0], i[1].split('\t')) for i in get_disp_rads(Trad=True)]
LSimpRads = [(i[0], i[1].split('\t')) for i in get_disp_rads(Trad=False)]
LBothRads = [(i[0], i[1].split('\t')) for i in get_disp_rads(Trad='Both')]

#print DRads[u'一'].encode('utf-8')
#print DChars[u'一'].encode('utf-8')
#print 'DRads:', ''.join(DRads.keys()).encode('utf-8')
