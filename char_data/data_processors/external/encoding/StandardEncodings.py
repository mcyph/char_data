from char_data.abstract_base_classes.data_sources.ExternalSourceBase import ExternalSourceBase
from char_data.data_processors.external.encoding import EncodingFormatter


class StandardEncodings(ExternalSourceBase):
    def __init__(self, char_data):
        ExternalSourceBase.__init__(self, char_data, 'standard_encodings')

        #================================================================#
        #                         all languages                          #
        #================================================================#

        self.utf_16 = EncodingFormatter(self, 'utf_16', 'all languages')
        self.utf_7 = EncodingFormatter(self, 'utf_7', 'all languages')
        self.utf_8 = EncodingFormatter(self, 'utf_8', 'all languages')

        #================================================================#
        #                    all languages (BMP only)                    #
        #================================================================#

        self.utf_16_be = EncodingFormatter(self, 'utf_16_be', 'all languages (BMP only)')
        self.utf_16_le = EncodingFormatter(self, 'utf_16_le', 'all languages (BMP only)')

        #================================================================#
        #                             Arabic                             #
        #================================================================#

        self.cp1256 = EncodingFormatter(self, 'cp1256', 'Arabic', ['ar'])
        self.cp864 = EncodingFormatter(self, 'cp864', 'Arabic', ['ar'])
        self.iso8859_6 = EncodingFormatter(self, 'iso8859_6', 'Arabic', ['ar'])

        #================================================================#
        #                         Baltic languages                       #
        #================================================================#

        self.cp1257 = EncodingFormatter(self, 'cp1257', 'Baltic languages')
        self.cp775 = EncodingFormatter(self, 'cp775', 'Baltic languages')
        self.iso8859_13 = EncodingFormatter(self, 'iso8859_13', 'Baltic languages')
        self.iso8859_4 = EncodingFormatter(self, 'iso8859_4', 'Baltic languages')

        #================================================================#
        #     Bulgarian, Byelorussian, Macedonian, Russian, Serbian      #
        #================================================================#

        self.cp1251 = EncodingFormatter(self,
            'cp1251',
            'Bulgarian, Byelorussian, Macedonian, Russian, Serbian',
                                        ['bg', 'be', 'mk', 'ru', 'sr']
                                        )
        self.cp855 = EncodingFormatter(self,
            'cp855',
            'Bulgarian, Byelorussian, Macedonian, Russian, Serbian',
                                       ['bg', 'be', 'mk', 'ru', 'sr']
                                       )
        self.iso8859_5 = EncodingFormatter(self,
            'iso8859_5',
            'Bulgarian, Byelorussian, Macedonian, Russian, Serbian',
                                           ['bg', 'be', 'mk', 'ru', 'sr']
                                           )
        self.mac_cyrillic = EncodingFormatter(self,
            'mac_cyrillic',
            'Bulgarian, Byelorussian, Macedonian, Russian, Serbian',
                                              ['bg', 'be', 'mk', 'ru', 'sr']
                                              )

        #================================================================#
        #                          Canadian                              #
        #================================================================#

        self.cp863 = EncodingFormatter(self, 'cp863', 'Canadian', ['fr'])

        #================================================================#
        #                      Celtic languages                          #
        #================================================================#

        self.iso8859_14 = EncodingFormatter(self,
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

        self.cp1250 = EncodingFormatter(self,
            'cp1250', 'Central and Eastern Europe',
                                        ['pl', 'cz', 'sl', 'hu', '??', 'bs', 'cr']  # FIXME!!! ========================================================
                                        )
        self.cp852 = EncodingFormatter(self,
            'cp852', 'Central and Eastern Europe'
                                       )
        self.iso8859_2 = EncodingFormatter(self,
            'iso8859_2', 'Central and Eastern Europe'
                                           )
        self.mac_latin2 = EncodingFormatter(self,
            'mac_latin2', 'Central and Eastern Europe'
                                            )

        #================================================================#
        #                       Danish, Norwegian                        #
        #================================================================#

        self.cp865 = EncodingFormatter(self, 'cp865', 'Danish, Norwegian', ['da', 'no'])

        #================================================================#
        #                           English                              #
        #================================================================#

        self.ascii = EncodingFormatter(self, 'ascii', 'English', ['en'])
        self.cp037 = EncodingFormatter(self, 'cp037', 'English', ['en'])
        self.cp437 = EncodingFormatter(self, 'cp437', 'English', ['en'])

        #================================================================#
        #                      Esperanto, Maltese                        #
        #================================================================#

        self.iso8859_3 = EncodingFormatter(self, 'iso8859_3', 'Esperanto, Maltese')

        #================================================================#
        #                            Greek                               #
        #================================================================#

        self.cp1253 = EncodingFormatter(self, 'cp1253', 'Greek', ['el'])
        self.cp737 = EncodingFormatter(self, 'cp737', 'Greek', ['el'])
        self.cp869 = EncodingFormatter(self, 'cp869', 'Greek', ['el'])
        self.cp875 = EncodingFormatter(self, 'cp875', 'Greek', ['el'])
        self.iso8859_7 = EncodingFormatter(self, 'iso8859_7', 'Greek', ['el'])
        self.mac_greek = EncodingFormatter(self, 'mac_greek', 'Greek', ['el'])

        #================================================================#
        #                            Hebrew                              #
        #================================================================#

        self.cp1255 = EncodingFormatter(self, 'cp1255', 'Hebrew', ['he'])
        self.cp424 = EncodingFormatter(self, 'cp424', 'Hebrew', ['he'])
        self.cp856 = EncodingFormatter(self, 'cp856', 'Hebrew', ['he'])
        self.cp862 = EncodingFormatter(self, 'cp862', 'Hebrew', ['he'])
        self.iso8859_8 = EncodingFormatter(self, 'iso8859_8', 'Hebrew', ['he'])

        #================================================================#
        #                           Icelandic                            #
        #================================================================#

        self.cp861 = EncodingFormatter(self, 'cp861', 'Icelandic')
        self.mac_iceland = EncodingFormatter(self, 'mac_iceland', 'Icelandic', ['is'])

        #================================================================#
        #                           Japanese                             #
        #================================================================#

        self.cp932 = EncodingFormatter(self, 'cp932', 'Japanese', ['ja'])
        self.euc_jis_2004 = EncodingFormatter(self, 'euc_jis_2004', 'Japanese', ['ja'])
        self.euc_jisx0213 = EncodingFormatter(self, 'euc_jisx0213', 'Japanese', ['ja'])
        self.euc_jp = EncodingFormatter(self, 'euc_jp', 'Japanese', ['ja'])
        self.iso2022_jp = EncodingFormatter(self, 'iso2022_jp', 'Japanese', ['ja'])
        self.iso2022_jp_1 = EncodingFormatter(self, 'iso2022_jp_1', 'Japanese', ['ja'])
        self.iso2022_jp_2004 = EncodingFormatter(self, 'iso2022_jp_2004', 'Japanese', ['ja'])
        self.iso2022_jp_3 = EncodingFormatter(self, 'iso2022_jp_3', 'Japanese', ['ja'])
        self.iso2022_jp_ext = EncodingFormatter(self, 'iso2022_jp_ext', 'Japanese', ['ja'])
        self.shift_jis = EncodingFormatter(self, 'shift_jis', 'Japanese', ['ja'])
        self.shift_jis_2004 = EncodingFormatter(self, 'shift_jis_2004', 'Japanese', ['ja'])
        self.shift_jisx0213 = EncodingFormatter(self, 'shift_jisx0213', 'Japanese', ['ja'])

        #================================================================#
        #  Japanese, Korean, Simplified Chinese, Western Europe, Greek   #
        #================================================================#

        self.iso2022_jp_2 = EncodingFormatter(self,
            'iso2022_jp_2',
            'Japanese, Korean, Simplified Chinese, Western Europe, Greek',
                                              ['ja', 'ko', 'zh', 'el']  # FIXME!! =================================================
                                              )

        #================================================================#
        #                      Kazakh                      #
        #================================================================#

        self.ptcp154 = EncodingFormatter(self, 'ptcp154', 'Kazakh')

        #================================================================#
        #                      Korean                      #
        #================================================================#

        self.cp949 = EncodingFormatter(self, 'cp949', 'Korean', ['ko'])
        self.euc_kr = EncodingFormatter(self, 'euc_kr', 'Korean', ['ko'])
        self.iso2022_kr = EncodingFormatter(self, 'iso2022_kr', 'Korean', ['ko'])
        self.johab = EncodingFormatter(self, 'johab', 'Korean', ['ko'])

        #================================================================#
        #                      Nordic languages                      #
        #================================================================#

        self.iso8859_10 = EncodingFormatter(self, 'iso8859_10', 'Nordic languages')

        #================================================================#
        #                      Portuguese                      #
        #================================================================#

        self.cp860 = EncodingFormatter(self, 'cp860', 'Portuguese', ['pt'])

        #================================================================#
        #                      Russian                      #
        #================================================================#

        self.cp866 = EncodingFormatter(self, 'cp866', 'Russian', ['ru'])
        self.koi8_r = EncodingFormatter(self, 'koi8_r', 'Russian', ['ru'])

        #================================================================#
        #                      Simplified Chinese                      #
        #================================================================#

        self.gb2312 = EncodingFormatter(self, 'gb2312', 'Simplified Chinese', ['zh'])
        self.hz = EncodingFormatter(self, 'hz', 'Simplified Chinese', ['zh'])

        #================================================================#
        #                      Thai                      #
        #================================================================#

        self.cp874 = EncodingFormatter(self, 'cp874', 'Thai', ['th'])

        #================================================================#
        #                      Traditional Chinese                      #
        #================================================================#

        self.big5 = EncodingFormatter(self,
            'big5', 'Traditional Chinese', ['zh_Hant']
                                      )
        self.big5hkscs = EncodingFormatter(self,
            'big5hkscs', 'Traditional Chinese', ['zh_Hant']
                                           )
        self.cp950 = EncodingFormatter(self,
            'cp950', 'Traditional Chinese', ['zh_Hant']
                                       )

        #================================================================#
        #                      Turkish                      #
        #================================================================#

        self.cp1026 = EncodingFormatter(self, 'cp1026', 'Turkish', ['tu'])
        self.cp1254 = EncodingFormatter(self, 'cp1254', 'Turkish', ['tu'])
        self.cp857 = EncodingFormatter(self, 'cp857', 'Turkish', ['tu'])
        self.iso8859_9 = EncodingFormatter(self, 'iso8859_9', 'Turkish', ['tu'])
        self.mac_turkish = EncodingFormatter(self, 'mac_turkish', 'Turkish', ['tu'])

        #================================================================#
        #                           Ukrainian                            #
        #================================================================#

        self.koi8_u = EncodingFormatter(self, 'koi8_u', 'Ukrainian', ['uk'])

        #================================================================#
        #                        Unified Chinese                         #
        #================================================================#

        self.gb18030 = EncodingFormatter(self,
            'gb18030', 'Unified Chinese', ['zh', 'zh_Hant']
                                         )
        self.gbk = EncodingFormatter(self,
            'gbk', 'Unified Chinese', ['zh', 'zh_Hant']
                                     )

        #================================================================#
        #                             Urdu                               #
        #================================================================#

        self.cp1006 = EncodingFormatter(self, 'cp1006', 'Urdu', ['ur'])

        #================================================================#
        #                           Vietnamese                           #
        #================================================================#

        self.cp1258 = EncodingFormatter(self, 'cp1258', 'Vietnamese', ['vi'])

        #================================================================#
        #                          West Europe                           #
        #================================================================#

        self.latin_1 = EncodingFormatter(self, 'latin_1', 'West Europe')

        #================================================================#
        #                         Western Europe                         #
        #================================================================#

        self.cp1140 = EncodingFormatter(self, 'cp1140', 'Western Europe')
        self.cp1252 = EncodingFormatter(self, 'cp1252', 'Western Europe')
        self.cp500 = EncodingFormatter(self, 'cp500', 'Western Europe')
        self.cp850 = EncodingFormatter(self, 'cp850', 'Western Europe')
        self.iso8859_15 = EncodingFormatter(self, 'iso8859_15', 'Western Europe')
        self.mac_roman = EncodingFormatter(self, 'mac_roman', 'Western Europe')


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


