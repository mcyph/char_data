import json
from codecs import open
from char_data.data_paths import data_path


# HACK!
from char_data.data_processors.external.hanzi_variants.import_data.DLinkKeys import (
    DReverseLinkKeys, REVERSE
)
from char_data.abstract_base_classes.formatters.ExternalFormatterBase import ExternalFormatterBase
from char_data.data_processors.consts import HEADER_VARIANTS

#from warnings import warn
#warn("PLEASE FIX CEDictVariants to be not reliant on Flazzle dictionary modules!!!")
# HACK!
#DReverseLinkKeys = {}
#REVERSE = None


LLinkKeys = list(DReverseLinkKeys.keys())
#LLinkKeys = ['other variant', 'less common variant', 'popular variant', 'Erhua variant', 'abbreviated form', 'correct form', 'unabbreviated form', 'PRC variant', 'Chinese classifier', 'words which can use classifier', 'non-PRC Variant', 'archaic variant', 'non-Erhua variant', 'see also', 'non-Japanese variant', 'same as', 'obscure variant', 'more common variant', 'modern form', 'archaic form', 'antonym', 'variant of', 'erroneous form', 'Japanese variant', 'modern variant']


with open(
    data_path('chardata', 'cedict/variants.json'),
    'rb', 'utf-8'
) as f:
    DVariants = json.loads(f.read())


class CEDictVariantsFormatter(ExternalFormatterBase):
    def __init__(self, parent, key):
        self.LKeys = DReverseLinkKeys[key]
        self.key = key

        ExternalFormatterBase.__init__(
            self, parent, HEADER_VARIANTS, original_name=key,
            short_desc=key, LISOs=['zh', 'zh_Hant']  # CHECK ME!!!!! =====================================
        )

    def raw_data(self, ord_):
        c = chr(ord_)

        L = []
        for typ, key in self.LKeys:
            D = DVariants['DRev'] if typ == REVERSE else DVariants['DFwd']

            if c in D[key]:
                L.extend(
                    [i[1] for i in D[key][c]]
                )

        return L or None

    def _format_data(self, ord_, data):
        c = chr(ord_)
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


if __name__ == '__main__':
    from char_data.data_processors.external import hanzi_variants

    for key in sorted(hanzi_variants.LHanziVariantKeys):
        use_key = key.lower().replace(' ', '_')
        print(("self.%s = CEDictVariants(self, '%s')" % (use_key, key)))
