# -*- coding: utf-8 -*-
from char_data.CharData import CharData
from char_data.CharIndexes import CharIndexes
from char_data.toolkit.encodings.surrogates import w_unichr

from char_data.misc import get_smallest_name


class LatinAccents:
    def __init__(self, char_data, char_indexes):
        self.char_data = char_data
        self.char_indexes = char_indexes
        self.DLatin = self.get_D_latin()

    def get_D_latin(self, script='Latin'):
        """
        This can also work for Latin-like scripts such as
        Cyrillic to an extent, but works best for Latin.

        It provides a map from e.g. "e" to "é" etc for allowing input popups
        (giving a choice of accented characters after a non-accented character
        is pressed) and grouping into like headers etc
        """
        DLatin = {}

        LLatin = self.char_indexes.search('unicodedata.script', script)
        for L in LLatin:
            if not type(L) in (list, tuple):
                L = [L, L]
            from_, to = L

            for ord_ in range(from_, to+1):
                char = w_unichr(ord_)

                # Find the relevant key
                name = [_.lower() for _ in self.char_data.raw_data('name', ord_)]
                letters = get_smallest_name(name)
                #print 'SMALLEST NAME:', name, letters, unichr(ord_)

                if not char in DLatin:
                    DLatin[char] = []
                DLatin[char].append(letters)

                if len(letters) > 1:
                    DLatin[char].append(letters[0])

                # TODO: What about "alternates" for characters which
                # look like e.g. an 'o' but sound like another letter?

                # Adjust case as appropriate
                if char.istitle():
                    DLatin[char] = [i.title() for i in DLatin[char]]
                elif char.isupper():
                    DLatin[char] = [i.upper() for i in DLatin[char]]
                elif char.islower():
                    DLatin[char] = [i.lower() for i in DLatin[char]]

        # Spanish HACKS!
        DLatin['!'] = ['¡']
        DLatin['?'] = ['¿']
        DLatin['¡'] = ['!']
        DLatin['¿'] = ['?']
        return DLatin
    #get_D_latin = cache_funct('get_D_latin', get_D_latin)

    def get_D_accents(self, LChars):
        """
        Get a map from a basic character
        e.g. "a" to any accented "a" characters

        OPEN ISSUE: Support punctuation as well?
        """
        DRtn = {}
        for chars in LChars:
            if chars[0] in self.DLatin:
                for map_ in self._get_L_mappings(chars):
                    #print 'map:', map_, chars
                    DRtn.setdefault(map_, []).append(chars)

            else:
                for char in chars:
                    if not char in self.DLatin:
                        import warnings
                        warnings.warn("character not found: %s" % ord(char))
                        continue

                    for map_ in self.DLatin[char]:
                        if char == map_:
                            # HACK: Don't include e.g. 'e' without any accents!
                            #print('CONTINUE:', map_, chars)
                            continue

                        DRtn.setdefault(map_, []).append(chars)

        return DRtn

    def _get_L_mappings(self, s):
        LRtn = []
        for i_s in [s[:x] for x in range(1, len(s)+1)]:
            #print 'i_s:', i_s
            if all(_ in self.DLatin for _ in i_s):
                key = ''
                for c in i_s:
                    # FIXME: Make this work with all permutations
                    # in DLatin, not just the first character!
                    #print 'CHAR:', c, self.DLatin[c]
                    key += self.DLatin[c][0] # HACK!

                LRtn.append(key)

        assert LRtn, s
        return LRtn

    def get_D_latin_to_L_chars(self, script='Latin'):
        DRtn = {}

        LChars = self.char_indexes.search('unicodedata.script', script)
        for LRange in LChars:
            if type(LRange) != tuple:
                LRange = (LRange, LRange+1)

            for ord_ in range(*LRange):
                name = self.char_data.raw_data('name', ord_)
                key = get_smallest_name(name).lower()
                #print key, unichr(ord_).encode('utf-8'), name

                if key != 'zz':
                    key = key[0] # HACK!

                L = DRtn.setdefault(key, [])
                L.append(w_unichr(ord_))
        return DRtn


if __name__ == '__main__':
    print((LatinAccents().get_D_latin()))

    print((LatinAccents().get_D_accents([
        "ü",
        "e"
        "á",
        "é",
        "í",
        "ñ",
        "ó",
        "ú"
    ])))
