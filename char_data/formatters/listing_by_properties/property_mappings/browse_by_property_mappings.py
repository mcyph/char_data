
THREE_LEVEL_TREE_LIST = 0
TREE_LIST = 1
FLAT = 2
MULTI_RAD_SEL = 3
OTHER_SUB_LIST = 4







def Header(s, LItems):
    return s


def Item(s, kind):
    return (s, kind)


DCharbrowseMappings = {
    'base': [
        Header('scripts/blocks', [
            ThreeLevelTreeList(
                'general scripts',
                lambda: DMappings[FIXME]['LScriptHierarchy'],
                lambda property: FIXME
            ),
            TreeList('general blocks', LBlocks),
            TreeList('conscript blocks', LConscriptBlocks),
        ]),

        Header('other lists', [
            TreeList('alphabets of languages'),
            OtherSubList('other properties')
        ]),

        # 'miscellaneous',
        # ['chinese handwriting', 'Handwriting'],
        # ['paste characters', 'PasteChars'],
        # ['character search', 'NameSubList'],
        # ['by IPA usage', 'IPASubList'],
    ],

    '': [
        # The "other" sublist in the character palette for
        # uncommon properties to reduce clutter
        Header('General Properties'),
        ['General Category', 'TreeList'],
        ['Core Properties', 'TreeList'],
        ['Property List', 'TreeList'],

        Header('Arabic/Bidirectional Properties'),
        ['Arabic Shaping Group', 'Flat'],
        ['Arabic Shaping Type', 'Flat'],
        ['Bidirectional Category', 'TreeList'],
        ['Joining Type', 'TreeList'],

        Header('Combining Properties'),
        ['Canonical Combining Classes', 'TreeList'],
        ['Case Folding Status', 'TreeList'],

        Header('Numeric/Digit Properties'),
        ['Decimal Digit Value	Flat'],
        ['Digit Value    Flat'],
        ['Numeric Value    Flat'],
        ['Primary Numeric    Flat'],

        Header('Breaking Properties'),
        ['Grapheme Break    TreeList'],
        ['Line Break    TreeList'],
        ['Sentence Break    TreeList'],
        ['Word Break    TreeList'],

        Header('Other Properties'),
        ['Age	TreeList'],
        ['East Asian Width	TreeList'],

        Header('By Chinese/Japanese Frequency'),
        ['Chinese Frequency    Flat'],
        ['Hong Kong Grade    Flat'],
        ['Japanese Grade    Flat'],
        ['Japanese Frequency    Flat'],

        Header('Book Indices'),
        ['Kodansha Compact Kanji Guide    Flat'],
        ['Kanji and Kana    Flat'],
        ['Kodansha Kanji Learners Dictionary    Flat'],
        ['Cihai    Flat'],
        ['The Kanji Way to Japanese Language Power    Flat'],
        ['Meyer Wempe    Flat'],
        ['Other Numeric    Flat'],
        ['Hanyu Da Zidian    Flat'],
        ['Cheung Bauer    Flat'],
        ['Essential Kanji    Flat'],
        ['Modern Reader\'s Japanese-English Character Dictionary    Flat'],
        ['Accounting Numeric    Flat'],
        ['New Nelson Japanese-English Character Dictionary    Flat'],
        ['Remembering the Kanji    Flat'],
        ['Japanese Kanji Flashcards    Flat'],
        ['KangXi    Flat'],
        ['Lau    Flat'],
        ['Fenn Dictionary    Flat'],
        ['A Guide to Remembering Japanese Characters    Flat'],
        ['Dae Jaweon    Flat'],
        ['A Guide to Reading and Writing Japanese (Sakade)    Flat'],
        ['Cowles    Flat'],
        ['Matthews    Flat'],
        ['Grammata Serica Recensa    Flat'],
        ['Kanji in Context    Flat'],
        ['Gakken Kanji Dictionary    Flat'],
        ['Morohashi    Flat'],
        ['Tuttle Kanji Cards    Flat'],
        ['Karlgren    Flat'],
        ['Song Ben Guang Yun    Flat'],
        ['HKGlyph    Flat'],
        ['Japanese Names    Flat'],
        ['A Guide to Reading and Writing Japanese (Henshall)    Flat'],
        ['New Japanese-English Character Dictionary    Flat'],
        ['Nelson    Flat'],
    ],

    'radicals': [
        ['Chinese Unified Radicals', 'MultiRadSel'],
        ['Chinese Simplified Radicals', 'MultiRadSel'],
        ['Chinese Traditional Radicals', 'MultiRadSel'],
        ['Japanese Radicals', 'MultiRadSel'],
        ['Korean Radicals', 'MultiRadSel'],
        ['Tang Radicals', 'MultiRadSel'],
        ['Vietnamese Radicals', 'MultiRadSel'],
    ],


}

import warnings

def check_for_unused_properties(property, SUsedScripts, on_error=warnings.warn): # e.g. "General Scripts"
    """
    TODO: Update me to use the new chardata interface!!!
    """
    all_found = True

    LScripts = CharData.MultiIndex.property_keys(property)  # FIXME!!!! ==================================================
    print 'SCRIPTS:', LScripts

    for script in LScripts:
        if not script in SUsedScripts:
            text = "Unused script found: %s" % script

            if on_error == Exception:
                raise Exception(text)
            elif on_error == warnings.warn:
                warnings.warn(text)
            elif on_error:
                on_error(text)

            all_found = False

    return all_found
