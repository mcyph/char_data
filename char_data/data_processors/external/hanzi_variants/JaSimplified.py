from char_data.data_processors.external.radicals.import_data.j_simplified import get_trad_ja_maps
from char_data.abstract_base_classes.formatters.ExternalFormatterBase import ExternalFormatterBase
from char_data.data_processors.consts import HEADER_VARIANTS

DTradToJa, DJaToTrad = get_trad_ja_maps()


class JaSimplified(ExternalFormatterBase):
    def __init__(self, parent, char_data, key):
        self.key = key
        self.DOpposite = DTradToJa if key == 'japanese_simplified' else DJaToTrad

        ExternalFormatterBase.__init__(
            self, parent, HEADER_VARIANTS, original_name=key, short_desc=key,
            LISOs=['ja'] if key == 'japanese_simplified' else 'chinese_traditional'
        )
        self.char_data = char_data

    def raw_data(self, ord_):
        L = []

        for i_ord, _ in ((ord_, 0),)+(self.char_data.raw_data('traditionalvariant', ord_) or ()):
            i_c = chr(i_ord)

            if i_c in self.DOpposite:
                L.extend(
                    [ord(i) for i in self.DOpposite[i_c]]
                )

        return L or None

    def _format_data(self, ord_, data):
        L = []

        for i_ord, _ in ((ord_, 0),)+(self.char_data.raw_data('traditionalvariant', ord_) or ()):
            i_c = chr(i_ord)

            if i_c in self.DOpposite:
                L.extend(self.DOpposite[i_c]) # FIXME!

        return L or None
