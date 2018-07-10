from ExternalBase import ExternalBase
from char_data.data_sources.external.property_formatters.encoding import Encoding


class StandardEncodings(ExternalBase):
    def __init__(self, key):
        ExternalBase.__init__(self, key)

        #================================================================#
        #                         all languages                          #
        #================================================================#

        self.utf_16 = Encoding('utf_16', 'all languages')
        self.utf_7 = Encoding('utf_7', 'all languages')
        self.utf_8 = Encoding('utf_8', 'all languages')

        #================================================================#
        #                    all languages (BMP only)                    #
        #================================================================#

        self.utf_16_be = Encoding('utf_16_be', 'all languages (BMP only)')
        self.utf_16_le = Encoding('utf_16_le', 'all languages (BMP only)')

        #================================================================#
        #                             Arabic                             #
        #================================================================#

        self.cp1256 = Encoding('cp1256', 'Arabic', ['ar'])
        self.cp864 = Encoding('cp864', 'Arabic', ['ar'])
        self.iso8859_6 = Encoding('iso8859_6', 'Arabic', ['ar'])

        #================================================================#
        #                         Baltic languages                       #
        #================================================================#

        self.cp1257 = Encoding('cp1257', 'Baltic languages')
        self.cp775 = Encoding('cp775', 'Baltic languages')
        self.iso8859_13 = Encoding('iso8859_13', 'Baltic languages')
        self.iso8859_4 = Encoding('iso8859_4', 'Baltic languages')

        #================================================================#
        #     Bulgarian, Byelorussian, Macedonian, Russian, Serbian      #
        #================================================================#

        self.cp1251 = Encoding(
            'cp1251',
            'Bulgarian, Byelorussian, Macedonian, Russian, Serbian',
            ['bg', 'be', 'mk', 'ru', 'sr']
        )
        self.cp855 = Encoding(
            'cp855',
            'Bulgarian, Byelorussian, Macedonian, Russian, Serbian',
            ['bg', 'be', 'mk', 'ru', 'sr']
        )
        self.iso8859_5 = Encoding(
            'iso8859_5',
            'Bulgarian, Byelorussian, Macedonian, Russian, Serbian',
            ['bg', 'be', 'mk', 'ru', 'sr']
        )
        self.mac_cyrillic = Encoding(
            'mac_cyrillic',
            'Bulgarian, Byelorussian, Macedonian, Russian, Serbian',
            ['bg', 'be', 'mk', 'ru', 'sr']
        )

        #================================================================#
        #                          Canadian                              #
        #================================================================#

        self.cp863 = Encoding('cp863', 'Canadian', ['fr'])

        #================================================================#
        #                      Celtic languages                          #
        #================================================================#

        self.iso8859_14 = Encoding(
            'iso8859_14', 'Celtic languages',
            ['ga', 'gv', 'gd', 'cy', 'kw', 'br']
        )

        #================================================================#
        #                   Central and Eastern Europe                   #
        #================================================================#

        # Polish, Czech, Slovak, Hungarian, Slovene, Bosnian, Croatian,
        # Serbian (Latin script), Romanian (before 1993 spelling reform)
        # and Albanian. It may also be used with the German language;
        # German-language texts encoded with Windows-1250 and
        # Windows-1252 are identical.

        self.cp1250 = Encoding(
            'cp1250', 'Central and Eastern Europe',
            ['pl', 'cz', 'sl', 'hu', '??', 'bs', 'cr', FIXME]
        )
        self.cp852 = Encoding(
            'cp852', 'Central and Eastern Europe'
        )
        self.iso8859_2 = Encoding(
            'iso8859_2', 'Central and Eastern Europe'
        )
        self.mac_latin2 = Encoding(
            'mac_latin2', 'Central and Eastern Europe'
        )

        #================================================================#
        #                       Danish, Norwegian                        #
        #================================================================#

        self.cp865 = Encoding('cp865', 'Danish, Norwegian', ['da', 'no'])

        #================================================================#
        #                           English                              #
        #================================================================#

        self.ascii = Encoding('ascii', 'English', ['en'])
        self.cp037 = Encoding('cp037', 'English', ['en'])
        self.cp437 = Encoding('cp437', 'English', ['en'])

        #================================================================#
        #                      Esperanto, Maltese                        #
        #================================================================#

        self.iso8859_3 = Encoding('iso8859_3', 'Esperanto, Maltese')

        #================================================================#
        #                            Greek                               #
        #================================================================#

        self.cp1253 = Encoding('cp1253', 'Greek', ['el'])
        self.cp737 = Encoding('cp737', 'Greek', ['el'])
        self.cp869 = Encoding('cp869', 'Greek', ['el'])
        self.cp875 = Encoding('cp875', 'Greek', ['el'])
        self.iso8859_7 = Encoding('iso8859_7', 'Greek', ['el'])
        self.mac_greek = Encoding('mac_greek', 'Greek', ['el'])

        #================================================================#
        #                            Hebrew                              #
        #================================================================#

        self.cp1255 = Encoding('cp1255', 'Hebrew', ['he'])
        self.cp424 = Encoding('cp424', 'Hebrew', ['he'])
        self.cp856 = Encoding('cp856', 'Hebrew', ['he'])
        self.cp862 = Encoding('cp862', 'Hebrew', ['he'])
        self.iso8859_8 = Encoding('iso8859_8', 'Hebrew', ['he'])

        #================================================================#
        #                           Icelandic                            #
        #================================================================#

        self.cp861 = Encoding('cp861', 'Icelandic')
        self.mac_iceland = Encoding('mac_iceland', 'Icelandic', ['is'])

        #================================================================#
        #                           Japanese                             #
        #================================================================#

        self.cp932 = Encoding('cp932', 'Japanese', ['ja'])
        self.euc_jis_2004 = Encoding('euc_jis_2004', 'Japanese', ['ja'])
        self.euc_jisx0213 = Encoding('euc_jisx0213', 'Japanese', ['ja'])
        self.euc_jp = Encoding('euc_jp', 'Japanese', ['ja'])
        self.iso2022_jp = Encoding('iso2022_jp', 'Japanese', ['ja'])
        self.iso2022_jp_1 = Encoding('iso2022_jp_1', 'Japanese', ['ja'])
        self.iso2022_jp_2004 = Encoding('iso2022_jp_2004', 'Japanese', ['ja'])
        self.iso2022_jp_3 = Encoding('iso2022_jp_3', 'Japanese', ['ja'])
        self.iso2022_jp_ext = Encoding('iso2022_jp_ext', 'Japanese', ['ja'])
        self.shift_jis = Encoding('shift_jis', 'Japanese', ['ja'])
        self.shift_jis_2004 = Encoding('shift_jis_2004', 'Japanese', ['ja'])
        self.shift_jisx0213 = Encoding('shift_jisx0213', 'Japanese', ['ja'])

        #================================================================#
        #  Japanese, Korean, Simplified Chinese, Western Europe, Greek   #
        #================================================================#

        self.iso2022_jp_2 = Encoding(
            'iso2022_jp_2',
            'Japanese, Korean, Simplified Chinese, Western Europe, Greek',
            ['ja', 'ko', 'zh', 'el', FIXME]
        )

        #================================================================#
        #                      Kazakh                      #
        #================================================================#

        self.ptcp154 = Encoding('ptcp154', 'Kazakh')

        #================================================================#
        #                      Korean                      #
        #================================================================#

        self.cp949 = Encoding('cp949', 'Korean', ['ko'])
        self.euc_kr = Encoding('euc_kr', 'Korean', ['ko'])
        self.iso2022_kr = Encoding('iso2022_kr', 'Korean', ['ko'])
        self.johab = Encoding('johab', 'Korean', ['ko'])

        #================================================================#
        #                      Nordic languages                      #
        #================================================================#

        self.iso8859_10 = Encoding('iso8859_10', 'Nordic languages')

        #================================================================#
        #                      Portuguese                      #
        #================================================================#

        self.cp860 = Encoding('cp860', 'Portuguese', ['pt'])

        #================================================================#
        #                      Russian                      #
        #================================================================#

        self.cp866 = Encoding('cp866', 'Russian', ['ru'])
        self.koi8_r = Encoding('koi8_r', 'Russian', ['ru'])

        #================================================================#
        #                      Simplified Chinese                      #
        #================================================================#

        self.gb2312 = Encoding('gb2312', 'Simplified Chinese', ['zh'])
        self.hz = Encoding('hz', 'Simplified Chinese', ['zh'])

        #================================================================#
        #                      Thai                      #
        #================================================================#

        self.cp874 = Encoding('cp874', 'Thai', ['th'])

        #================================================================#
        #                      Traditional Chinese                      #
        #================================================================#

        self.big5 = Encoding(
            'big5', 'Traditional Chinese', ['zh_Hant']
        )
        self.big5hkscs = Encoding(
            'big5hkscs', 'Traditional Chinese', ['zh_Hant']
        )
        self.cp950 = Encoding(
            'cp950', 'Traditional Chinese', ['zh_Hant']
        )

        #================================================================#
        #                      Turkish                      #
        #================================================================#

        self.cp1026 = Encoding('cp1026', 'Turkish', ['tu'])
        self.cp1254 = Encoding('cp1254', 'Turkish', ['tu'])
        self.cp857 = Encoding('cp857', 'Turkish', ['tu'])
        self.iso8859_9 = Encoding('iso8859_9', 'Turkish', ['tu'])
        self.mac_turkish = Encoding('mac_turkish', 'Turkish', ['tu'])

        #================================================================#
        #                           Ukrainian                            #
        #================================================================#

        self.koi8_u = Encoding('koi8_u', 'Ukrainian', ['uk'])

        #================================================================#
        #                        Unified Chinese                         #
        #================================================================#

        self.gb18030 = Encoding(
            'gb18030', 'Unified Chinese', ['zh', 'zh_Hant']
        )
        self.gbk = Encoding(
            'gbk', 'Unified Chinese', ['zh', 'zh_Hant']
        )

        #================================================================#
        #                             Urdu                               #
        #================================================================#

        self.cp1006 = Encoding('cp1006', 'Urdu', ['ur'])

        #================================================================#
        #                           Vietnamese                           #
        #================================================================#

        self.cp1258 = Encoding('cp1258', 'Vietnamese', ['vi'])

        #================================================================#
        #                          West Europe                           #
        #================================================================#

        self.latin_1 = Encoding('latin_1', 'West Europe')

        #================================================================#
        #                         Western Europe                         #
        #================================================================#

        self.cp1140 = Encoding('cp1140', 'Western Europe')
        self.cp1252 = Encoding('cp1252', 'Western Europe')
        self.cp500 = Encoding('cp500', 'Western Europe')
        self.cp850 = Encoding('cp850', 'Western Europe')
        self.iso8859_15 = Encoding('iso8859_15', 'Western Europe')
        self.mac_roman = Encoding('mac_roman', 'Western Europe')


if __name__ == '__main__':
    from toolkit.encodings.LEncodings import LEncodings
    from pprint import pprint
    pprint(LEncodings)

    prev_for_lang = None

    for for_lang, encoding in LEncodings:
        if prev_for_lang != for_lang:
            print '''
#================================================================#
#                      %s                      #
#================================================================#
''' % for_lang


            prev_for_lang = for_lang

        print "self.%s = Encoding('%s', '%s')" % (
            encoding, encoding, for_lang
        )


