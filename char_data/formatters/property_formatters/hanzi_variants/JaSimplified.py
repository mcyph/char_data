from char_data.importers.radicals.j_simplified import get_trad_ja_maps

DTradToJa, DJaToTrad = get_trad_ja_maps()


class JaSimplified:
    def __init__(self, key):
        self.key = key
        self.D = DTradToJa if key == 'japanesesimplified' else DJaToTrad

    def raw_data(self, ord_):
        from char_data import char_data
        L = []

        for i_ord, _ in ((ord_, 0),)+(char_data.raw_data('traditionalvariant', ord_) or ()):
            i_c = unichr(i_ord)

            if i_c in self.D:
                L.extend(
                    [ord(i) for i in self.D[i_c]]
                )

        return L or None

    def formatted(self, ord_):
        from char_data import char_data
        L = []

        for i_ord, _ in ((ord_, 0),)+(char_data.raw_data('traditionalvariant', ord_) or ()):
            i_c = unichr(i_ord)

            if i_c in self.D:
                L.extend(self.D[i_c]) # FIXME!

        return L or None

