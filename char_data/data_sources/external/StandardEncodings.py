from .ExternalBase import ExternalBase
from char_data.data_sources.external.property_formatters.encoding import Encoding


class StandardEncodings(ExternalBase):
    def __init__(self):
        ExternalBase.__init__(self, 'standard_encodings')

        #================================================================#
        #                         all languages                          #
        #================================================================#

        self.utf_16 = Encoding(self, 'utf_16', 'all languages')
        self.utf_7 = Encoding(self, 'utf_7', 'all languages')
        self.utf_8 = Encoding(self, 'utf_8', 'all languages')

        #================================================================#
        #                    all languages (BMP only)                    #
        #================================================================#

        self.utf_16_be = Encoding(self, 'utf_16_be', 'all languages (BMP only)')
        self.utf_16_le = Encoding(self, 'utf_16_le', 'all languages (BMP only)')

        #================================================================#
        #                             Arabic                             #
        #================================================================#

        self.cp1256 = Encoding(self, 'cp1256', 'Arabic', ['ar'])
        self.cp864 = Encoding(self, 'cp864', 'Arabic', ['ar'])
        self.iso8859_6 = Encoding(self, 'iso8859_6', 'Arabic', ['ar'])

        #================================================================#
        #                         Baltic languages                       #
        #================================================================#

        self.cp1257 = Encoding(self, 'cp1257', 'Baltic languages')
        self.cp775 = Encoding(self, 'cp775', 'Baltic languages')
        self.iso8859_13 = Encoding(self, 'iso8859_13', 'Baltic languages')
        self.iso8859_4 = Encoding(self, 'iso8859_4', 'Baltic languages')

        #================================================================#
        #     Bulgarian, Byelorussian, Macedonian, Russian, Serbian      #
        #================================================================#

        self.cp1251 = Encoding(self, 
            'cp1251',
            'Bulgarian, Byelorussian, Macedonian, Russian, Serbian',
            ['bg', 'be', 'mk', 'ru', 'sr']
        )
        self.cp855 = Encoding(self, 
            'cp855',
            'Bulgarian, Byelorussian, Macedonian, Russian, Serbian',
            ['bg', 'be', 'mk', 'ru', 'sr']
        )
        self.iso8859_5 = Encoding(self, 
            'iso8859_5',
            'Bulgarian, Byelorussian, Macedonian, Russian, Serbian',
            ['bg', 'be', 'mk', 'ru', 'sr']
        )
        self.mac_cyrillic = Encoding(self, 
            'mac_cyrillic',
            'Bulgarian, Byelorussian, Macedonian, Russian, Serbian',
            ['bg', 'be', 'mk', 'ru', 'sr']
        )

        #================================================================#
        #                          Canadian                              #
        #================================================================#

        self.cp863 = Encoding(self, 'cp863', 'Canadian', ['fr'])

        #================================================================#
        #                      Celtic languages                          #
        #================================================================#

        self.iso8859_14 = Encoding(self, 
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

        self.cp1250 = Encoding(self, 
            'cp1250', 'Central and Eastern Europe',
            ['pl', 'cz', 'sl', 'hu', '??', 'bs', 'cr']   # FIXME!!! ========================================================
        )
        self.cp852 = Encoding(self, 
            'cp852', 'Central and Eastern Europe'
        )
        self.iso8859_2 = Encoding(self, 
            'iso8859_2', 'Central and Eastern Europe'
        )
        self.mac_latin2 = Encoding(self, 
            'mac_latin2', 'Central and Eastern Europe'
        )

        #================================================================#
        #                       Danish, Norwegian                        #
        #================================================================#

        self.cp865 = Encoding(self, 'cp865', 'Danish, Norwegian', ['da', 'no'])

        #================================================================#
        #                           English                              #
        #================================================================#

        self.ascii = Encoding(self, 'ascii', 'English', ['en'])
        self.cp037 = Encoding(self, 'cp037', 'English', ['en'])
        self.cp437 = Encoding(self, 'cp437', 'English', ['en'])

        #================================================================#
        #                      Esperanto, Maltese                        #
        #================================================================#

        self.iso8859_3 = Encoding(self, 'iso8859_3', 'Esperanto, Maltese')

        #================================================================#
        #                            Greek                               #
        #================================================================#

        self.cp1253 = Encoding(self, 'cp1253', 'Greek', ['el'])
        self.cp737 = Encoding(self, 'cp737', 'Greek', ['el'])
        self.cp869 = Encoding(self, 'cp869', 'Greek', ['el'])
        self.cp875 = Encoding(self, 'cp875', 'Greek', ['el'])
        self.iso8859_7 = Encoding(self, 'iso8859_7', 'Greek', ['el'])
        self.mac_greek = Encoding(self, 'mac_greek', 'Greek', ['el'])

        #================================================================#
        #                            Hebrew                              #
        #================================================================#

        self.cp1255 = Encoding(self, 'cp1255', 'Hebrew', ['he'])
        self.cp424 = Encoding(self, 'cp424', 'Hebrew', ['he'])
        self.cp856 = Encoding(self, 'cp856', 'Hebrew', ['he'])
        self.cp862 = Encoding(self, 'cp862', 'Hebrew', ['he'])
        self.iso8859_8 = Encoding(self, 'iso8859_8', 'Hebrew', ['he'])

        #================================================================#
        #                           Icelandic                            #
        #================================================================#

        self.cp861 = Encoding(self, 'cp861', 'Icelandic')
        self.mac_iceland = Encoding(self, 'mac_iceland', 'Icelandic', ['is'])

        #================================================================#
        #                           Japanese                             #
        #================================================================#

        self.cp932 = Encoding(self, 'cp932', 'Japanese', ['ja'])
        self.euc_jis_2004 = Encoding(self, 'euc_jis_2004', 'Japanese', ['ja'])
        self.euc_jisx0213 = Encoding(self, 'euc_jisx0213', 'Japanese', ['ja'])
        self.euc_jp = Encoding(self, 'euc_jp', 'Japanese', ['ja'])
        self.iso2022_jp = Encoding(self, 'iso2022_jp', 'Japanese', ['ja'])
        self.iso2022_jp_1 = Encoding(self, 'iso2022_jp_1', 'Japanese', ['ja'])
        self.iso2022_jp_2004 = Encoding(self, 'iso2022_jp_2004', 'Japanese', ['ja'])
        self.iso2022_jp_3 = Encoding(self, 'iso2022_jp_3', 'Japanese', ['ja'])
        self.iso2022_jp_ext = Encoding(self, 'iso2022_jp_ext', 'Japanese', ['ja'])
        self.shift_jis = Encoding(self, 'shift_jis', 'Japanese', ['ja'])
        self.shift_jis_2004 = Encoding(self, 'shift_jis_2004', 'Japanese', ['ja'])
        self.shift_jisx0213 = Encoding(self, 'shift_jisx0213', 'Japanese', ['ja'])

        #================================================================#
        #  Japanese, Korean, Simplified Chinese, Western Europe, Greek   #
        #================================================================#

        self.iso2022_jp_2 = Encoding(self, 
            'iso2022_jp_2',
            'Japanese, Korean, Simplified Chinese, Western Europe, Greek',
            ['ja', 'ko', 'zh', 'el']  # FIXME!! =================================================
        )

        #================================================================#
        #                      Kazakh                      #
        #================================================================#

        self.ptcp154 = Encoding(self, 'ptcp154', 'Kazakh')

        #================================================================#
        #                      Korean                      #
        #================================================================#

        self.cp949 = Encoding(self, 'cp949', 'Korean', ['ko'])
        self.euc_kr = Encoding(self, 'euc_kr', 'Korean', ['ko'])
        self.iso2022_kr = Encoding(self, 'iso2022_kr', 'Korean', ['ko'])
        self.johab = Encoding(self, 'johab', 'Korean', ['ko'])

        #================================================================#
        #                      Nordic languages                      #
        #================================================================#

        self.iso8859_10 = Encoding(self, 'iso8859_10', 'Nordic languages')

        #================================================================#
        #                      Portuguese                      #
        #================================================================#

        self.cp860 = Encoding(self, 'cp860', 'Portuguese', ['pt'])

        #================================================================#
        #                      Russian                      #
        #================================================================#

        self.cp866 = Encoding(self, 'cp866', 'Russian', ['ru'])
        self.koi8_r = Encoding(self, 'koi8_r', 'Russian', ['ru'])

        #================================================================#
        #                      Simplified Chinese                      #
        #================================================================#

        self.gb2312 = Encoding(self, 'gb2312', 'Simplified Chinese', ['zh'])
        self.hz = Encoding(self, 'hz', 'Simplified Chinese', ['zh'])

        #================================================================#
        #                      Thai                      #
        #================================================================#

        self.cp874 = Encoding(self, 'cp874', 'Thai', ['th'])

        #================================================================#
        #                      Traditional Chinese                      #
        #================================================================#

        self.big5 = Encoding(self, 
            'big5', 'Traditional Chinese', ['zh_Hant']
        )
        self.big5hkscs = Encoding(self, 
            'big5hkscs', 'Traditional Chinese', ['zh_Hant']
        )
        self.cp950 = Encoding(self, 
            'cp950', 'Traditional Chinese', ['zh_Hant']
        )

        #================================================================#
        #                      Turkish                      #
        #================================================================#

        self.cp1026 = Encoding(self, 'cp1026', 'Turkish', ['tu'])
        self.cp1254 = Encoding(self, 'cp1254', 'Turkish', ['tu'])
        self.cp857 = Encoding(self, 'cp857', 'Turkish', ['tu'])
        self.iso8859_9 = Encoding(self, 'iso8859_9', 'Turkish', ['tu'])
        self.mac_turkish = Encoding(self, 'mac_turkish', 'Turkish', ['tu'])

        #================================================================#
        #                           Ukrainian                            #
        #================================================================#

        self.koi8_u = Encoding(self, 'koi8_u', 'Ukrainian', ['uk'])

        #================================================================#
        #                        Unified Chinese                         #
        #================================================================#

        self.gb18030 = Encoding(self, 
            'gb18030', 'Unified Chinese', ['zh', 'zh_Hant']
        )
        self.gbk = Encoding(self, 
            'gbk', 'Unified Chinese', ['zh', 'zh_Hant']
        )

        #================================================================#
        #                             Urdu                               #
        #================================================================#

        self.cp1006 = Encoding(self, 'cp1006', 'Urdu', ['ur'])

        #================================================================#
        #                           Vietnamese                           #
        #================================================================#

        self.cp1258 = Encoding(self, 'cp1258', 'Vietnamese', ['vi'])

        #================================================================#
        #                          West Europe                           #
        #================================================================#

        self.latin_1 = Encoding(self, 'latin_1', 'West Europe')

        #================================================================#
        #                         Western Europe                         #
        #================================================================#

        self.cp1140 = Encoding(self, 'cp1140', 'Western Europe')
        self.cp1252 = Encoding(self, 'cp1252', 'Western Europe')
        self.cp500 = Encoding(self, 'cp500', 'Western Europe')
        self.cp850 = Encoding(self, 'cp850', 'Western Europe')
        self.iso8859_15 = Encoding(self, 'iso8859_15', 'Western Europe')
        self.mac_roman = Encoding(self, 'mac_roman', 'Western Europe')


if __name__ == '__main__':
    from toolkit.encodings.LEncodings import LEncodings
    from pprint import pprint
    pprint(LEncodings)

    prev_for_lang = None

    for for_lang, encoding in LEncodings:
        if prev_for_lang != for_lang:
            print(('''
#================================================================#
#                      %s                      #
#================================================================#
''' % for_lang))


            prev_for_lang = for_lang

        print(("self.%s = Encoding(self, '%s', '%s')" % (
            encoding, encoding, for_lang
        )))


