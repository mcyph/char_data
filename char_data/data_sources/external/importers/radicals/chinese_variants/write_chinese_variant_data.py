# -*- coding: utf-8 -*-
from toolkit.json_tools import loads
from flazzle.dicts.Edict.CEDict.JSimplified import DTradToSimp, DSimpToTrad


def get_D_variants():
    File = open('Variants.json', 'rb')
    DVariants = loads(File.read().decode('utf-8'))
    File.close()
    return DVariants


def write_forward(DVariants):
    """
    Output variants, including Japanese data
    """
    DFwd = DVariants['DFwd']
    File = open('CnVariants.txt', 'w', encoding='utf-8', errors='replace')
    File.write('# Chinese Variants File - encoded using UTF-8\n')
    File.write('# Extracted from CEDict and Chinese Traditional->Japanese Simplified data\n')
    File.write('# Format: <Variant Type>\\t<Hanzi>\\t<Traditional Variant>\\t<Simplified Variant>\\n\n')
    File.write('# For example, "JVariants\t広 \t廣\t广"\n')
    File.write('#   Means "The Japanese character 広 has Chinese Variants 廣 and 广"\n')
    File.write('# NOTE: Japanese variants can only be converted Chinese Traditional <-> Japanese for now!\n')
    File.write('# Extracted with a script created using trial-and-error - MAY HAVE ERRORS!\n')
    for Type in DFwd:
        if Type == 'DJVariants':
            File.write('# Begin "Japanese Simplified Traditional" Character Mappings\n')
            for Char in DTradToSimp:
                for iChar in DTradToSimp[Char]:
                    File.write('%s\t%s\t%s\t%s\n' % (Type[1:], iChar, Char, Char)) # HACK - CHECK ME!
            File.write('# End "Japanese Simplified Traditional" Character Mappings (CEDict data follows)\n')

        for Char in DFwd[Type]:
            L = DFwd[Type][Char]
            for Trad, Simp in L:
                File.write('%s\t%s\t%s\t%s\n' % (Type[1:], Char, Trad, Simp))
    File.close()


def write_reverse(DVariants):
    """
    Output reverse variants
    """
    DRev = DVariants['DRev']
    File = open('CnVariantsReversed.txt', 'wb', encoding='utf-8', errors='replace')
    for Type in DRev:
        if Type == 'DJVariants':
            File.write('# Begin "Japanese Simplified Traditional" Character Mappings\n')
            for Char in DSimpToTrad:
                for iChar in DSimpToTrad[Char]:
                    File.write('%s\t%s\t%s\t%s\n' % (Type[1:], iChar, Char, Char)) # HACK - CHECK ME!
            File.write('# End "Japanese Simplified Traditional" Character Mappings (CEDict data follows)\n')

        for Char in DRev[Type]:
            L = DRev[Type][Char]
            for Trad, Simp in L:
                File.write('%s\t%s\t%s\t%s\n' % (Type[1:], Char, Trad, Simp))
    File.close()


if __name__ == '__main__':
    DVariants = get_D_variants()
    write_forward(DVariants)
    write_reverse(DVariants)

