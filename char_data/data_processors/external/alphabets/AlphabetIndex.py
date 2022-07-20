from lang_data import LangData, get_possible_isos_list as _get_L_possible_isos
from iso_tools.ISOTools import ISOTools
from iso_tools.ISOCodes import ISOCodes


def get_possible_isos_list():
    # NOTE ME: The below get_possible_isos_list is **really** slow, so this is the cached output
    #from warnings import warn
    #warn("Please add a better caching solution to get_possible_isos_list")

    return ['aa', 'af', 'agq', 'ak', 'am', 'ar', 'as', 'asa', 'az', 'az_Cyrl', 'az_Latn', 'bas', 'be', 'bem', 'bez', 'bg',
     'bm', 'bn', 'bo', 'br', 'brx', 'bs', 'byn', 'ca', 'cch', 'cgg', 'chr', 'cs', 'cy', 'da', 'dav', 'de', 'de-CH',
     'de-LI', 'dje', 'dua', 'dyo', 'dz', 'ebu', 'ee', 'el', 'en', 'en-BE', 'en-GB', 'en-ZA', 'en_Dsrt', 'en_Shaw', 'eo',
     'es', 'et', 'eu', 'ewo', 'fa', 'fa-AF', 'ff', 'fi', 'fil', 'fo', 'fr', 'fr-BE', 'fr-CA', 'fr-CH', 'fr-LU', 'fur',
     'ga', 'gaa', 'gd', 'gl', 'gsw', 'gu', 'guz', 'gv', 'ha', 'ha_Latn', 'haw', 'he', 'hi', 'hr', 'hu', 'hy', 'ia',
     'id', 'ig', 'ii', 'is', 'it', 'it-CH', 'ja', 'jmc', 'ka', 'kab', 'kaj', 'kam', 'kcg', 'kde', 'kea', 'khq', 'ki',
     'kk', 'kk_Cyrl', 'kl', 'kln', 'km', 'kn', 'ko', 'kok', 'ksb', 'ksf', 'ksh', 'kw', 'ky', 'lag', 'lg', 'ln', 'lo',
     'lt', 'lu', 'luo', 'luy', 'lv', 'mas', 'mer', 'mfe', 'mg', 'mgh', 'mk', 'ml', 'mn', 'mn_Cyrl', 'mn_Mong', 'mr',
     'ms', 'ms-BN', 'mt', 'mua', 'my', 'naq', 'nb', 'nd', 'nds', 'ne', 'nl', 'nmg', 'nn', 'nr', 'nso', 'nus', 'nyn',
     'oc', 'om', 'or', 'pa', 'pa_Arab', 'pa_Guru', 'pl', 'ps', 'pt', 'pt-PT', 'rm', 'rn', 'ro', 'rof', 'ru', 'rw',
     'rwk', 'sah', 'saq', 'sbp', 'se', 'seh', 'ses', 'sg', 'shi', 'shi_Latn', 'shi_Tfng', 'si', 'sid', 'sk', 'sl', 'sn',
     'so', 'sq', 'sr', 'sr_Cyrl', 'sr_Latn', 'ss', 'ssy', 'st', 'sv', 'sv-FI', 'sw', 'swc', 'ta', 'te', 'teo', 'tg',
     'tg_Cyrl', 'th', 'ti', 'ti-ER', 'tig', 'tn', 'to', 'tr', 'trv', 'ts', 'twq', 'tzm', 'tzm_Latn', 'uk', 'ur', 'uz',
     'uz_Arab', 'uz_Cyrl', 'uz_Latn', 'vai', 'vai_Latn', 'vai_Vaii', 've', 'vi', 'vun', 'wae', 'wal', 'xh', 'xog',
     'yav', 'yo', 'zh', 'zh_Hans', 'zh_Hans-MO', 'zh_Hant', 'zu']


"""
def get_possible_isos_list():
    D = {}
    L = _get_L_possible_isos()

    for iso in L:
        print('ALPHABETINDEX GET_L_POSSIBLE_ISOS:', iso)
        lang_data = LangData(iso)
        D[iso] = dumps(
            [lang_data.get_alpha_list(), lang_data.get_symbols_list()]
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

    r = list(sorted(D.keys()))
    return r
"""


class AlphabetIndex:
    typ = 'alphabets'

    def __init__(self, lang_data, original_name):
        self.lang_data = lang_data
        self.__add_to_two_level_mappings()

    def __add_to_two_level_mappings(self):
        # TODO: ADD TO DTwoLevelMappings!!!
        DOut = {}

        for iso in get_possible_isos_list():
            iso_info = ISOTools.split(iso)
            if iso_info.territory:
                from iso_tools.ISOCodes import DCountries
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

        from char_data.data_processors.consts import DTwoLevelMappings
        DTwoLevelMappings['cldr_alphabets.alphabets'] = LOut  # HACK!

    def values(self):
        return get_possible_isos_list()

    def get_value_info(self, value):
        from char_data.data_info_types.CharIndexValueInfo import CharIndexValueInfo
        pretty_printed = self.lang_data.prettify_lang(value)
        return CharIndexValueInfo(value, str(pretty_printed))

    def search(self, search):
        lang_data = LangData(search)
        from char_data.unicodeset import UnicodeSet

        return_list = []
        for heading, ranges in lang_data.get_alpha_list():
            LOut = []
            for i_s in UnicodeSet(ranges):
                LOut.extend([ord(i) for i in i_s])
            return_list.extend(LOut)
            #return_list.append((heading, LOut))

        for typ1, typ2, i_L in lang_data.get_symbols_list():
            for heading, chars in i_L:
                if typ2:
                    # ??? What does typ1/typ2 do again??
                    heading = '%s %s' % (typ2, heading)

                if typ1:
                    heading = '%s %s' % (typ1, heading)

                LExtend = [ord(i) for i in chars]
                return_list.extend(LExtend)
                #return_list.append((heading, LExtend))

        from pprint import pprint
        pprint(return_list)

        #lang_data.get_currency_symbol()
        #lang_data.locale_pattern()
        #lang_data.ellipsis()
        #lang_data.quotes('')
        #lang_data.paranthesis('')
        return return_list


if __name__ == '__main__':
    print(_get_L_possible_isos())
