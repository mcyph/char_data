from toolkit.escape import E
from multi_translit.translit.Defines import *
from multi_translit.translit.TranslitLoad import DIDToStr, DTranslitChars, DISOToDSet, DStrToISO

def compare(a, b):
    if a == 'Latin': return -1
    elif b == 'Latin': return 1
    else: return cmp(a, b)

CmpCaseInsensitive1 = lambda x: x[0].lower()
CmpCaseInsensitive2 = lambda x: x.lower()

def get_translit_map(CodePoint):
    # Add transliteration mappings
    if CodePoint in DTranslitChars:
        # TODO: Make DTranslitChars use CODEPOINTS for higher ranges?
        # TODO: Group the items together?
        # TODO: Use dotpoints to reduce space using both columns?
        # TODO: Only show the language and "to" script?
        DRtn = {}
        D = DTranslitChars[CodePoint]
        for Id in D:
            if not Id in DIDToStr: continue # FIXME!
            Name = DIDToStr[Id]
            
            # [ModMode, [LastIf, PosIfAfter, PosIfBefore, NegIf], DTranslit]
            LVals = D[Id]
            
            LAppend = []
            for LVal in LVals:
                ModMode = LVal[0]
                LastIf = LVal[1][0]
                PosIfAfter = LVal[1][1]
                PosIfBefore = LVal[1][2]
                NegIf = LVal[1][3]
                DVal = LVal[2]
                if AFTER in DVal: del DVal[AFTER] # HACK!
                if BEFORE in DVal: del DVal[BEFORE] # HACK!
                
                cVal = '%s =' % (DVal[CONV])
                for StrKey, IntKey in [('self', SELF), 
                            ('initial', INITIAL), 
                            ('final', FINAL), 
                            ('medial', MEDIAL), 
                            ('sylinitial', SYLINITIAL), 
                            ('sylfinal', SYLFINAL), 
                            ('allforms', ALLFORMS)]:
                    
                    if IntKey in DVal:
                        if len(DVal) == 2 and StrKey == 'allforms':
                            cVal = '%s %s' % (cVal, DVal[IntKey])
                        else: cVal = '%s %s(%s)' % (cVal, StrKey, DVal[IntKey])
                
                # TODO: ADD SUPPORT FOR ignore( values!
                if PosIfAfter: cVal = 'if after(%s): %s' % (LastIf[1], cVal)
                if PosIfBefore: cVal = 'if before(%s): %s' % (LastIf[1], cVal)
                if ModMode: pass # FIXME!
                cVal = cVal.replace('||', ' [or] ')
                LAppend.append(cVal)
            
            # Add a unique key so that e.g. Allworth will group all systems together into 
            # a separate dotpoint under a unique header e.g. Latin to reduce clutter is 
            # listed as a separate dotpoint only 
            # TODO: APPEND e.g. Latin as a separate header entirely?
            LISOCode = DStrToISO[Name][1]
            DSet = DISOToDSet[LISOCode]
            if DSet['Path'][0] == 'From-To':
                FontScript = DSet['LFonts'][1]
                #ShortScript = DSet['LProvides'][1][1].replace('%s ' % DSet['LFonts'][1], '')
                #ShortOtherScript = DSet['LProvides'][0][1].replace('%s ' % DSet['LFonts'][0], '')
            elif DSet['Path'][0] == 'To-From':
                FontScript = DSet['LFonts'][0]
                #ShortScript = DSet['LProvides'][0][1].replace('%s ' % DSet['LFonts'][0], '')
                #ShortOtherScript = DSet['LProvides'][1][1].replace('%s ' % DSet['LFonts'][1], '')
            
            if ' ' in DSet['LProvides'][0][1]:
                ShortOtherScript = ' '.join(DSet['LProvides'][0][1].split(' ')[1:])
            elif ' ' in DSet['LProvides'][1][1]:
                ShortOtherScript = ' '.join(DSet['LProvides'][1][1].split(' ')[1:])
            else: ShortOtherScript = FontScript # HACK!
            
            Append = '; '.join([E(i) for i in LAppend])
            LKey = (ShortOtherScript, Append)
            if not FontScript in DRtn: DRtn[FontScript] = {}
            if not LKey in DRtn[FontScript]: DRtn[FontScript][LKey] = []
            DRtn[FontScript][LKey].append(DSet['FormatString'].replace(' %s', ''))
        
        # Convert to HTML and return
        DUniqueLangs = {}
        LRtn = []
        LKeys = list(DRtn.keys())
        LKeys.sort(cmp=compare)
        for Key in LKeys: # Key is e.g. "Latin" or "IPA"
            LItem = []
            D = DRtn[Key]
            LSubKeys = [i for i in D]
            LSubKeys.sort(key=CmpCaseInsensitive1)
            for LKey in LSubKeys: # LKey is [System, TranslitVal]
                D[LKey].sort(key=CmpCaseInsensitive2)
                
                # Get the list of languages
                LLangs = D[LKey]
                for Lang in LLangs:
                    DUniqueLangs[Lang] = None
                #Langs = ', '.join(D[LKey])
                
                # Get the system, e.g. 'ALA-LC'
                System = LKey[0]
                
                # Get the translit value, e.g. 'ch' etc
                TranslitVal = LKey[1]
                LItem.append([LLangs, System, TranslitVal])
                #LItem.append('<li><B>%s</B> <I>(%s)</I>: %s</li>' % (System, Langs, TranslitVal))
            
            #List = '<ul style="font-size: 0.9em">%s</ul>' % '\n'.join(LItem)
            LRtn.append(['%s Transliterations' % Key, LItem])
            # TODO: Add support for multiple translit headings in Data!
            #LRtn.append(['Transliteration', [Key, LItem]])
        return tuple(DUniqueLangs.keys()), LRtn
    else: return [], []
