from char_data.CharData import CharData
from char_data.data.Languages.Langs import DLangs

# Provide a map from languages to characters 
# to ask "does x language use x character"?
# TODO: Use a single dict with IDs to minimize overhead?


def get_L_alphabet_langs():
    # Returns ((language name, a set of the alphabet of that language))
    # (in order to test whether a language has a specific 
    LAlpha = []
    for iso in DLangs:
        default_profile, DProfiles = DLangs[iso]
        
        for profile, DLang in list(DProfiles.items()):
            if 'LAlpha' in DLang and DLang['LAlpha']:
                S = set()
                for header, LChars in DLang['LAlpha']:
                    for chars in LChars:
                        for char in chars:
                            S.add(char)
                
                LAlpha.append((DLang['name'], S))
    return LAlpha


def get_L_alphabet_list_items(key='general blocks'):
    # Add by first letter in blocks
    LBlocks = CharData.property_keys(key)
    
    LRtn = []
    for char in 'abcdefghijklmnopqrstuvwxyz':
        LKeys = [i for i in LBlocks if i.lower().startswith(char)]
        if LKeys:
            LKeys.sort()
            LRtn.append(('Starting with "%s"' % (char.upper()), LKeys))
    return LRtn


def get_L_langs():
    LLangs = []
    DName2ISO = {}
    
    for iso, L in list(DLangs.items()):
        default_profile, DVariants = L
        
        for profile, DLang in list(DVariants.items()):
            if not 'LAlpha' in DLang or not DLang['LAlpha']:
                continue
            
            if profile and len(DLang) > 1: 
                LLangs.append('%s (%s)' % (DLang['name'], profile))
            else: 
                LLangs.append(DLang['name'])
            
            DName2ISO[LLangs[-1]] = (iso, profile)
    
    LLangs.sort(key=lambda x: x.lower())
    return DName2ISO, LLangs
#DName2ISO, LLangs = get_L_langs()
