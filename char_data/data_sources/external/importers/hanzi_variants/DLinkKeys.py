DLinkKeys = {
    'DVariants': (
        'variant of', 'other variant'
    ),
    'DSameAs': (
        'same as', 'same as'
    ),
    'DSeeAlso': (
        'see also', 'see also'
    ),
    'DAbbr': (
        'unabbreviated form', 'abbreviated form'
    ),
    'DAntonyms': (
        'antonym', 'antonym'
    ),


    'DObscureVariants': (
        'popular variant', 'obscure variant'
    ),
    'DArchaicVariants': (
        'modern variant', 'archaic variant'
    ),
    'DLessCommonVariants': (
        'more common variant', 'less common variant'
    ),
    'DOldVariants': (
        'modern form', 'archaic form'
    ),


    #'DTradVariants': (
    #    'simplified variant', 'traditional variant'
    #),
    'DJapaneseVariants': (
        'non-Japanese variant', 'Japanese variant'
    ), # OPEN ISSUE: TRAD ONLY?

    #'DKoreanVariants': (
    #    'non-Korean variant', 'Korean variant'
    #),
    'DNonPRCVariants': (
        'PRC variant', 'non-PRC Variant'
    ),
    #'DTaiwanVariants': (
    #    'Non-Taiwan variant', 'Taiwan variant'
    #),


    # TODO: Provide a link below the dotpoints for DClassifier?
    # http://en.wikipedia.org/wiki/Chinese_measure_word
    'DClassifier': (
        'Chinese classifier', 'words which can use classifier'
    ),
    'DErhua': (
        'non-Erhua variant', 'Erhua variant'
    ),


    'DErrors': (
        'correct form', 'erroneous form'
    ),
    #'DCompatVariants': (
    #    'noncompatibility variant', 'compatibility variant'
    #)
}

NORMAL = 0
REVERSE = 1

def get_D_reverse_link_keys():
    DReverseLinkKeys = {}

    for k, (from_key, to_key) in list(DLinkKeys.items()):
        DReverseLinkKeys.setdefault(from_key, []).append((NORMAL, k))
        DReverseLinkKeys.setdefault(to_key, []).append((REVERSE, k))

    return DReverseLinkKeys

DReverseLinkKeys = get_D_reverse_link_keys()

#print DReverseLinkKeys.keys()
