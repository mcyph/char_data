# TODO: REMOVE ME! ----------------------------------------------------------------------------------------
DISO2Lang = {
    None: 'All', 
    'yue': 'Cantonese', 
    'hak': 'Hakka', 
    'jpn': 'Japanese',
    'kor': 'Korean', 
    'cmn': 'Mandarin', 
    'ltc': 'Tang', # "Middle Chinese" http://en.wikipedia.org/wiki/Middle_Chinese
    'vie': 'Vietnamese'
}

DLang2ISO = {}
for key, value in DISO2Lang.items():
    DLang2ISO[value] = key
del key, value

# TODO: REMOVE ME! ----------------------------------------------------------------------------------------
DISO2LFullText = {
    'yue': [['Cantonese', 'Cantonese Readings'], ['Cantonese Definition']], # MULTIPLE?
    'jpn': [['Japanese Kun', 'Japanese On', 'Japanese Nanori'], ['Japanese Definition']],
    'hak': [['Hakka'], ['Cantonese Definition']],
    'kor': [['Korean', 'Hangul Readings', 'Korean Hangul'], ['Chinese Meanings']], # MULTIPLE?
    'cmn': [['Mandarin'], ['Chinese Definition']],
    'ltc': [['Tang'], ['Chinese Definition']],
    'vie': [['Vietnamese'], ['Chinese Definition']]
} # PHONETIC WARNING!

DMap = {
    'All': ('cmn:eng', 'jpn:eng', 'yue:eng', 'General', 'NamesList'),
    'cmn:eng': ('cmn:eng', 'General', 'NamesList'),
    'yue:eng': ('yue:eng', 'General', 'NamesList'),
    'jpn:eng': ('jpn:eng', 'General', 'NamesList'),
    'jpn:spa': ('jpn:spa', 'General', 'NamesList'),
    'jpn:por': ('jpn:por', 'General', 'NamesList'),
    'kor:eng': ('cmn:eng', 'General', 'NamesList'),
    'hak:eng': ('yue:eng', 'General', 'NamesList'),
    'ltc:eng': ('cmn:eng', 'General', 'NamesList'),
    'vie:eng': ('cmn:eng', 'General', 'NamesList')
}
