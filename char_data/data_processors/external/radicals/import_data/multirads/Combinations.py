from char_data.toolkit.list_operations.combs import get_L_unique_combs
from char_data.toolkit.list_operations.rem_dupes import fast_rem_dupes


def get_D_kanji_combs(DKanji):
    DRtn = {}
    
    num_items = 0
    for kanji, LRads in list(DKanji.items()):
        for x in range(1, 3):
            for comb in get_L_unique_combs(LRads, x):
                comb = tuple(sorted(comb))
                DRtn.setdefault(comb, []).append(kanji)
                num_items += 1
    
    for comb in DRtn:
        DRtn[comb] = fast_rem_dupes(DRtn[comb])
    
    print(('kanji combinations number:', num_items, len(DRtn)))
    return DRtn


if __name__ == '__main__':
    from os import chdir
    chdir('../../../../')
    from char_data.importer.parsers.multirads.RadKFile import get_D_rads, get_D_kanji, combine_radkfile_2
    
    DRads = combine_radkfile_2(get_D_rads('Chars/Data/Radicals/radkfile'),
                               get_D_rads('Chars/Data/Radicals/radkfile2'))
    DKanji = get_D_kanji(DRads)
    DCombs = get_D_kanji_combs(DKanji)
    
    for comb in sorted(DCombs.keys()):
        print((''.join(comb), ''.join(DCombs[comb])))
