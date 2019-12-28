
from char_data.toolkit.list_operations.rem_dupes import fast_rem_dupes


class RadKFile:
    def __init__(self):
        """
        Open the "radkfile" and "radkfile2" euc-jp
        multiradical files by Michael Raine and Jim Breen
        http://www.csse.monash.edu.au/~jwb/kradinf.html
        """
        DRads1 = self.get_D_rads('FIXME/radkfile')
        DRads2 = self.get_D_rads('FIXME/radkfile2')

        self.DRads = self.combine_radkfile_2(DRads1, DRads2)
        self.DKanji = self.get_D_kanji(self.DRads)

    def get_D_rads(self, path):
        """
        returns {radical: [kanji, ...], ...}
        """
        rad = None
        DRads = {}
        LChars = []

        with open(path, 'r', encoding='euc-jp') as f:
            for line in f:
                line = line.rstrip('\r\n')

                if not line:
                    continue

                if line[0] == '#':
                    # Ignore comments
                    continue

                elif line[0] == '$':
                    # Add previous item to DChars/DRads
                    if rad:
                        DRads.setdefault(rad, []).extend(LChars)

                    # Change radical/number strokes
                    LLine = line.strip().split()

                    rad = LLine[1]
                    LChars = []
                else:
                    # Add to list of characters
                    LChars.extend(line.strip())

        # Add the last item
        DRads.setdefault(rad, []).extend(LChars)
        return DRads

    def combine_radkfile_2(self, DRads1, DRads2):
        for rad, LKanji in list(DRads2.items()):
            L = DRads1.setdefault(rad, [])
            L.extend(LKanji)
            DRads1[rad] = fast_rem_dupes(L)
        return DRads1

    def get_D_kanji(self, DRads):
        """
        Reverses the result from `get_D_rads` above
        returns {kanji: [radical, ...], ..}
        """
        DRtn = {}
        for radical, LChars in list(DRads.items()):
            for char in LChars:
                DRtn.setdefault(char, []).append(radical)
        return DRtn

rad_k_file = RadKFile()
