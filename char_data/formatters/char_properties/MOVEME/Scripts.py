#from char_data.CharData import CharData
#from char_data.ranges.IterRanges import iter_ranges

LScriptOrder = [
    'East Asian Scripts', # TEMPORARY!
    'Symbols and Punctuation',
    'European Scripts',

    'Middle Eastern Scripts',
    'Indic Scripts',
    'South East Asian',
    'African Scripts',
    'American Scripts',
    'Central Asian Scripts',
    'Phillipine Scripts',
    'Ancient Scripts',
    'Miscellaneous'
]

script_types = '''
Avestan    Middle Eastern Scripts
Bamum    African Scripts
Egyptian Hieroglyphs    African Scripts
Format Characters    Symbols and Punctuation
Imperial Aramaic    Middle Eastern Scripts
Inscriptional Pahlavi    Middle Eastern Scripts
Inscriptional Parthian    Middle Eastern Scripts
Javanese    South East Asian
Kaithi    Indic Scripts
Lisu    South East Asian
Meetei Mayek    South East Asian
Old South Arabian    Middle Eastern Scripts
Old Turkic    Middle Eastern Scripts
Samaritan    Middle Eastern Scripts
Tai Tham    South East Asian
Tai Viet    South East Asian

Arabic    Middle Eastern Scripts
Armenian    European Scripts
Balinese    South East Asian
Bengali    Indic Scripts
Bopomofo    East Asian Scripts
Braille    Miscellaneous
Buginese    South East Asian
Buhid    Phillipine Scripts
Canadian Aboriginal    American Scripts
Cherokee    American Scripts
Common    Miscellaneous
Coptic    European Scripts
Cuneiform    Ancient Scripts
Cypriot    Ancient Scripts
Cyrillic    European Scripts
Deseret    American Scripts
Devanagari    Indic Scripts
Ethiopic    African Scripts
Georgian    European Scripts
Glagolitic    Miscellaneous
Gothic    Ancient Scripts
Greek    European Scripts
Gujarati    Indic Scripts
Gurmukhi    Indic Scripts
Han    East Asian Scripts
Hangul    East Asian Scripts
Hanunoo    Phillipine Scripts
Hebrew    Middle Eastern Scripts
Hiragana    East Asian Scripts
Inherited    Miscellaneous
Kannada    Indic Scripts
Katakana    East Asian Scripts
Kharoshthi    Central Asian Scripts
Khmer    South East Asian
Lao    South East Asian
Latin    European Scripts
Limbu    Indic Scripts
Linear B    Ancient Scripts
Malayalam    Indic Scripts
Mongolian    Central Asian Scripts
Myanmar    South East Asian
New Tai Lue    South East Asian
Nko    African Scripts
Ogham    Ancient Scripts
Old Italic    Ancient Scripts
Old Persian    Ancient Scripts
Oriya    Indic Scripts
Osmanya    Miscellaneous
Phags Pa    Central Asian Scripts
Phoenician    Ancient Scripts
Runic    Ancient Scripts
Shavian    Miscellaneous
Sinhala    Indic Scripts
Syloti Nagri    Indic Scripts
Syriac    Middle Eastern Scripts
Tagalog    Phillipine Scripts
Tagbanwa    Phillipine Scripts
Tai Le    South East Asian
Tamil    Indic Scripts
Telugu    Indic Scripts
Thaana    Middle Eastern Scripts
Thai    South East Asian
Tibetan    Central Asian Scripts
Tifinagh    African Scripts
Ugaritic    Ancient Scripts
Yi    East Asian Scripts

Kayah Li    South East Asian
Lepcha    Central Asian Scripts
Rejang    South East Asian
Sundanese    South East Asian
Saurashtra    Indic Scripts
Cham    South East Asian
Ol Chiki    Indic Scripts
Vai African    Scripts
Carian    European Scripts
Lycian    European Scripts
Lydian    European Scripts

CJK Symbols    East Asian Scripts
Phaistos Disc    Ancient Scripts
Vai    African Scripts
Control Characters    Miscellaneous

Currency Signs    Symbols and Punctuation
General Punctuation    Symbols and Punctuation
Geometric Shapes    Symbols and Punctuation
IPA Alphabet    Symbols and Punctuation
Letterlike Symbols    Symbols and Punctuation
Mathematical Signs    Symbols and Punctuation
Modifier and Combining Characters    Symbols and Punctuation
Musical Symbols    Miscellaneous
Numbers    Symbols and Punctuation
Pictures and Miscellaneous Symbols    Symbols and Punctuation
Spaces    Symbols and Punctuation
Technical Symbols    Symbols and Punctuation
'''


def get_D_scripts():
    DScripts = {}
    
    for line in script_types.split('\n'): # from Data/ScriptTypes.txt
        line = line.strip()
        if not line: 
            continue
        
        try: 
            script, mapping = line.replace('    ', '\t').split('\t')
        except: 
            print "ERROR ON LINE:", line.encode('utf-8')
            raise
        
        if not mapping in DScripts:
            DScripts[mapping] = []
        DScripts[mapping].append(script)
    
    return DScripts

DScripts = get_D_scripts()


def get_L_scripts():
    # Add by script region, e.g. "Middle East"
    #LScripts = sorted(DScripts.keys())
    SUsedScripts = set()
    
    LRtn = []
    for region in LScriptOrder: # from ScriptOrder.txt
        if not region in DScripts: 
            continue
        
        DScripts[region].sort()
        
        LSubRanges = []
        for script in DScripts[region]:
            LSubRanges.append(script)  # HACK!!!!! ======================================================================
            #LSubRanges.append(get_script_subranges(script))
            SUsedScripts.add(script)
        
        #print 'LAPPEND:', LAppend
        LRtn.append((region, LSubRanges))

    return LRtn


def get_script_subranges(typ):
    #
    range = CharData.search('General Scripts', typ)
    del_font_script, LRanges = iter_ranges(range)

    LRtn = []
    for i_type, value in LRanges:
        if i_type == 'Block':
            LRtn.append(value)

    if typ == 'Common' or typ == 'Inherited':
        LRtn.sort()
    return (typ, LRtn)


if __name__ == '__main__':
    from pprint import pprint
    pprint(get_L_scripts(), indent=4)
