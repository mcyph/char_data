# -*- coding: utf-8 -*-
import array
import codecs
from Radical import get_D_rads
from toolkit.rem_dupes import fast_rem_dupes, rem_dupes
from toolkit.cache_funct import cache_funct
from input.WidthConv import full_to_halfwidth
DRadicals = get_D_rads()
#from Chars.CharData import CharData # FIXME! ====================================================

def get_L_rad_lines():
    # HACK: Get both the radkfile and radkfile2 data and return them together
    with codecs.open('Chars/Data/radkfile', 'rb', 'euc-jp') as f1:
        with codecs.open('Chars/Data/radkfile2', 'rb', 'euc-jp') as f2:
            L = f1.read().split('\n')+f2.read().split('\n')
    return L

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

def get_both_multi_rads(DSimpRads, DSimpChars, DTradRads, DTradChars):
    # Get from both the simplified and traditional radicals
    DBothRads = {}
    for k in DSimpRads:
        if not k in DBothRads:
            DBothRads[k] = []
        DBothRads[k] += DSimpRads[k]
        DBothRads[k] = fast_rem_dupes(DBothRads[k])
    
    for k in DTradRads:
        if not k in DBothRads:
            DBothRads[k] = []
        DBothRads[k] += DTradRads[k]
        DBothRads[k] = fast_rem_dupes(DBothRads[k])
    
    DBothChars = {}
    for k in DSimpChars:
        if not k in DBothChars:
            DBothChars[k] = []
        DBothChars[k] += DSimpChars[k]
        DBothChars[k] = fast_rem_dupes(DBothChars[k])
    
    for k in DTradChars:
        if not k in DBothChars:
            DBothChars[k] = []
        DBothChars[k] += DTradChars[k]
        DBothChars[k] = fast_rem_dupes(DBothChars[k])
    return conv_to_array(DBothRads), DBothChars

def get_disp_rads(Trad):
    # Returns [[NumStrokes, RadChars, EngDef], ...]
    
    # TODO: Should there be Japanese-specific info?
    #print 'get_disp_rads:', Trad
    if Trad == 'Both':
        LKeys = fast_rem_dupes(LTradRadKeys+LSimpRadKeys)
        LKeys = list(LKeys)
        LKeys.sort()
    elif Trad: 
        LKeys = LTradRadKeys
        #LKeys.sort()
    else: 
        LKeys = LSimpRadKeys
        #LKeys.sort()
    
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
                try: strokes = DStrokeCounts[rad]
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
        else: LRtn.append(LFound[0])
        
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

# 一夂刀斉刈而鼠馬气化香力匚毛尤言身鼎犯｜癶水買戈方尸麻示羽疋皿血立齊母行ハ舌金青
# 囗鬯忙日飛魚川食非止工士韭黹耒凵穴豸勿亀冂禹缶冊二小匕五冖舛艮舟無亠鬥走音風髟犬
# 耳色攵谷厶爻爿禾十聿乃黄片釆酉手及免里彑竹角麦高牛瓜也彡衣矢入卩ヨ火自韋屯曰米已
# 廴用歹糸見广巾頁爪亅雨文門肉月王牙厂井斗世甘辛尚貝亡欠尢木冫个革臣竜田殳鬲鬼丶隹
# 礼品心羊奄无毋父黍扎子氏戸巛卜口鳥赤瓦鼓屮杰石干并勹夕幺黽虫艾老宀玄弋首矛弓疔初
# 土阡龠斤大邦豆女支皮辰生隶鼻人岡込儿滴汁元面久又車虍至ノ鹿黒豕比乙九マ几ユ巨足歯目
# 山彳鹵巴長骨寸白臼西廾

def get_by_multi_rads(LRads, Trad):
    xx = 0
    DRads = DBothRads
    DPossible = {}
    for iRad in LRads:
        #print 'iRad:', iRad.encode('utf-8')
        # Only append if either the first radical or already 
        # found by previous radicals to filter down to only 
        # characters with those multirads
        nDPossible = {}
        for SearchForRad in iRad:
            if SearchForRad in DRads:
                for AppendChar in DRads[SearchForRad]:
                    #print 'AppendChar:', AppendChar.encode('utf-8')
                    if (xx == 0) or (AppendChar in DPossible):
                        nDPossible[AppendChar] = None
        DPossible = nDPossible
        xx += 1
    
    # HACK: Add z-variants
    # NOT RECOMMENDED as 變 is shown under 亠
    if False:
        for Char in tuple(DPossible.keys()):
            LZVariant = raw_data('unihan.zvariant', Char)
            if LZVariant:
                for Variant in LZVariant:
                    DPossible[Variant] = None
    LRtn = list(DPossible.keys())
    LRtn.sort()
    return LRtn

def get_L_multi_rads(Trad):
    if Trad == 'Both': Rads = LBothRads
    elif Trad: Rads = LTradRads
    else: Rads = LSimpRads
    return Rads

def get_multi_rads():
    # Get the Traditional and auto-convert to Simplified data
    # (INTRODUCES ERRORS, but still useful a lot of the time)
    DTradRads, DTradChars = get_trad_multi_rads()
    DSimpRads, DSimpChars = get_simp_multi_rads()
    DBothRads, DBothChars = get_both_multi_rads(DSimpRads, DSimpChars, 
                                             DTradRads, DTradChars)
    
    # Get the RadKeys (whatever they are)
    LSimpRadKeys = list(DSimpRads.keys())
    LTradRadKeys = list(DTradRads.keys())
    LSimpRadKeys.sort()
    LTradRadKeys.sort()
    
    return DBothRads, DBothChars, LSimpRadKeys, LTradRadKeys
get_multi_rads = cache_funct('GetMultiRads', get_multi_rads)
DBothRads, DBothChars, LSimpRadKeys, LTradRadKeys = get_multi_rads()

# CHECK ME!
LTradRads = [(i[0], i[1].split('\t')) for i in get_disp_rads(Trad=True)]
LSimpRads = [(i[0], i[1].split('\t')) for i in get_disp_rads(Trad=False)]
LBothRads = [(i[0], i[1].split('\t')) for i in get_disp_rads(Trad='Both')]

#print DRads[u'一'].encode('utf-8')
#print DChars[u'一'].encode('utf-8')
#print 'DRads:', ''.join(DRads.keys()).encode('utf-8')
