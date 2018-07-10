from char_data.data_sources.external.importers.radicals.j_simplified import get_trad_ja_maps
from char_data.data_sources.external.property_formatters import ExternalBaseClass
from char_data.data_sources.consts import HEADER_VARIANTS

DTradToJa, DJaToTrad = get_trad_ja_maps()


class JaSimplified(ExternalBaseClass):
    def __init__(self, parent, key):
        self.key = key
        self.DOpposite = DTradToJa if key == 'japanesesimplified' else DJaToTrad

        ExternalBaseClass.__init__(
            self, parent, HEADER_VARIANTS, original_name=key, short_desc=key,
            LISOs=['ja'] if key == 'japanesesimplified' else 'traditionalvariant'
        )

    def raw_data(self, ord_):
        from char_data import char_data
        L = []

        for i_ord, _ in ((ord_, 0),)+(char_data.raw_data('traditionalvariant', ord_) or ()):
            i_c = unichr(i_ord)

            if i_c in self.DOpposite:
                L.extend(
                    [ord(i) for i in self.DOpposite[i_c]]
                )

        return L or None

    def _format_data(self, ord_, data):
        from char_data import char_data
        L = []

        for i_ord, _ in ((ord_, 0),)+(char_data.raw_data('traditionalvariant', ord_) or ()):
            i_c = unichr(i_ord)

            if i_c in self.DOpposite:
                L.extend(self.DOpposite[i_c]) # FIXME!

        return L or None

