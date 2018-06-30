import json
from codecs import open
from char_data.data_paths import data_path


# HACK!
from dicts.chinese.variants import (
    DLinkKeys, DReverseLinkKeys, NORMAL, REVERSE
)

from warnings import warn
warn("PLEASE FIX CEDictVariants to be not reliant on Flazzle dictionary modules!!!")
# HACK!
#DReverseLinkKeys = {}
#REVERSE = None

LLinkKeys = list(DReverseLinkKeys.keys())


with open(
    data_path('chardata', 'cedict/variants.json'),
    'rb', 'utf-8'
) as f:
    DVariants = json.loads(f.read())


class CEDictVariants:
    def __init__(self, key):
        self.LKeys = DReverseLinkKeys[key]
        self.key = key

    def raw_data(self, ord_):
        c = unichr(ord_)

        L = []
        for typ, key in self.LKeys:
            D = DVariants['DRev'] if typ == REVERSE else DVariants['DFwd']

            if c in D[key]:
                L.extend(
                    [i[1] for i in D[key][c]]
                )

        return L or None

    def formatted(self, ord_):
        c = unichr(ord_)
        L = self.raw_data(ord_)
        if not L:
            return None

        LOut = []

        for simp, trad, pinyin in L:
            if c == simp and c == trad:
                continue
            elif c == simp or trad == simp:
                out = trad
            elif c == trad:
                out = simp
            else:
                out = '%s/%s' % (trad, simp)

            if pinyin:
                out = '%s (%s)' % (out, pinyin)
            LOut.append(out)

        return ' '.join(LOut)

