from json import dumps
from lang_data import LangData, get_L_possible_isos as _get_L_possible_isos
from iso_tools import ISOTools, NONE, TERRITORY, VARIANT
from iso_tools.iso_codes import ISOCodes


def get_L_possible_isos():
    D = {}
    L = _get_L_possible_isos()

    for iso in L:
        ld = LangData(iso)
        D[iso] = dumps(
            [ld.get_L_alpha(), ld.get_L_symbols()]
        )

    for iso in L:
        for i_iso in ISOTools.get_L_removed(
            iso,
            [
                TERRITORY, VARIANT,
                VARIANT | TERRITORY
            ],
            rem_dupes=True
        ):
            if i_iso == iso:
                continue

            if i_iso in D and D[i_iso] == D[iso]:
                del D[iso]
                break

    return sorted(D.keys())


class AlphabetIndex:
    typ = 'alphabets'

    def __init__(self, ld, original_name):
        self.ld = ld
        self.__add_to_two_level_mappings()

    def __add_to_two_level_mappings(self):
        # TODO: ADD TO DTwoLevelMappings!!!
        DOut = {}

        for iso in get_L_possible_isos():
            iso_info = ISOTools.split(iso)
            if iso_info.territory:
                from iso_tools.iso_codes.ISOCodes import DCountries
                region = DCountries.get(iso_info.territory, ['Unknown'])[0]  # TODO: ALLOW FOR i18n etc!!!
            else:
                part3 = iso_info.lang
                # OPEN ISSUE: Use LCountry[2] here, to use continent rather than country??
                try:
                    region = ISOCodes.get_D_iso(part3)['LCountry'][1]
                except KeyError:
                    region = 'Unknown'

            DOut.setdefault(region, []).append(iso)

        LOut = []
        for region, LValues in sorted(DOut.items()):
            LOut.append((region, LValues))

        from char_data.data_sources.consts import DTwoLevelMappings
        DTwoLevelMappings['cldr_alphabets.alphabets'] = LOut  # HACK!

    def values(self):
        return get_L_possible_isos()

    def get_value_info(self, value):
        from char_data.data_sources.internal.indexes.read.CharIndexValueInfo import CharIndexValueInfo
        pretty_printed = self.ld.prettify_lang(value)
        return CharIndexValueInfo(value, str(pretty_printed))

    def search(self, search):
        ld = LangData(search)
        from char_data.unicodeset import unicodeset_from_range

        LRtn = []
        for heading, ranges in ld.get_L_alpha():
            LOut = []
            for i_s in unicodeset_from_range(ranges):
                LOut.extend([ord(i) for i in i_s])
            LRtn.extend(LOut)
            #LRtn.append((heading, LOut))

        for typ1, typ2, i_L in ld.get_L_symbols():
            for heading, chars in i_L:
                if typ2:
                    # ??? What does typ1/typ2 do again??
                    heading = '%s %s' % (typ2, heading)

                if typ1:
                    heading = '%s %s' % (typ1, heading)

                LExtend = [ord(i) for i in chars]
                LRtn.extend(LExtend)
                #LRtn.append((heading, LExtend))

        from pprint import pprint
        pprint(LRtn)

        #ld.get_currency_symbol()
        #ld.locale_pattern()
        #ld.ellipsis()
        #ld.quotes('')
        #ld.paranthesis('')
        return LRtn
