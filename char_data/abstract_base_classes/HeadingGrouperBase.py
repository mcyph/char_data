from typing import Union
from abc import ABC, abstractmethod

from lang_data import LangData
from iso_tools.ISOTools import ISOTools
from char_data.unicodeset.UnicodeSet import UnicodeSet
from char_data.misc.BlockHeadings import BlockHeadings
from char_data.toolkit.documentation.copydoc import copydoc
from char_data.misc import get_font_script, get_smallest_name
from char_data.abstract_base_classes.CharDataBase import CharDataBase


class HeadingGrouperBase(ABC):
    @abstractmethod
    def raw_data(self,
                 key: str,
                 ord_: Union[int, chr]):
        pass

    @abstractmethod
    def formatted(self,
                  key: str,
                  ord_: Union[int, chr]):
        pass

    #===================================================================#
    #               Group Ranges by Unicode Name Headings               #
    #===================================================================#

    @copydoc(CharDataBase.group_by_unicode_name)
    def group_by_unicode_name(self, LRanges, name=None):
        if name is None:
            first_ord = LRanges[0]
            if type(first_ord) == tuple:
                first_ord = first_ord[0]

            script = self.raw_data('unicodedata.script', first_ord)
            name = script if script else None
            # print '**NAME:', name

        return_list = []
        font_script = None

        for ord_ in LRanges:
            if type(ord_) == tuple:
                # A range. If the first BlockName item is None and the last item is None
                # OR the last BlockName doesn't equal the first BlockName
                from_, to = ord_

                # if FirstCodePoint is None:
                #    for i_code in xrange(from_, to+1):
                #        #print 'SUBTUPLE FALLBACK!'
                #        font_script = get_fallback(i_code)
                #        if font_script: break

                for i_code in range(from_, to + 1):
                    name = self.formatted('unicodedata.name', i_code)
                    if not name:
                        name = '(Unknown)'
                    else:
                        append = get_smallest_name(
                            name
                            # CharData.get_L_names(i_code, types=('general',))[0]
                        )

                    if (
                        name == 'Cyrillic' and
                        append[0] == 'e' and
                        len(append) > 1
                    ):
                        # HACK: fix e.g. 'ef' and 'em' and 'es' (f/m/s)
                        append = append[1]

                    return_list.append((append, i_code))

            else:
                # A codepoint, only one SubName required

                # if FirstCodePoint is None:
                # print 'SUBSINGLE FALLBACK!'
                # font_script = get_fallback(ord_)

                name = self.formatted('unicodedata.name', ord_)
                if not name:
                    name = '(Unknown)'
                else:
                    append = get_smallest_name(
                        name
                        # CharData.get_L_names(ord_, Types=('general',))[0]
                    )

                if (
                    name == 'Cyrillic' and
                    append[0] == 'e' and
                    len(append) > 1
                ):
                    # HACK: fix e.g. 'ef' and 'em' and 'es' (f/m/s)
                    append = append[1]

                return_list.append((append, ord_))

        # if not font_script: font_script = 'All'
        return_list.sort()

        new_return_list = []
        new_return_list.append(('block', name))  # HACK!

        last_key = None
        for sort_key, ord_ in return_list:
            if not font_script:
                font_script = get_font_script(self, ord_)

            # zz are Symbols - probably shouldn't be in Latin :-P
            if sort_key == 'zz':
                chk_key = 'zz'
            else:
                chk_key = sort_key[0]

            if last_key != chk_key:
                last_key = chk_key

                if chk_key == 'zz':
                    new_return_list.append(
                        ['sub_block', ['Miscellaneous Symbols', None]]
                    )
                else:
                    new_return_list.append(
                        ['sub_block', ['characters starting with "%s"' %
                                           chk_key.lower(),
                                       None]]
                    )

                new_return_list.append(['chars', []])
            new_return_list[-1][-1].append(ord_)

        # return_list = [['chars', [i[1] for i in return_list]]]
        return font_script, new_return_list

    #===================================================================#
    #                  Group Ranges by Block Headings                   #
    #===================================================================#

    @copydoc(CharDataBase.group_by_block)
    def group_by_block(self, LRanges):
        block_headings = BlockHeadings(self)
        return block_headings.get_L_block_headings(LRanges)

    #===================================================================#
    #                Group Ranges by Alphabet Headings                  #
    #===================================================================#

    @copydoc(CharDataBase.group_by_alphabet)
    def group_by_alphabet(self, search, char_indexes=None):
        """
        The headings are actually provided by the CLDR data directly,
        so if using the alphabet key, grab directly from the original source!
        """
        if char_indexes is None:
            from char_data.CharIndexes import CharIndexes
            char_indexes = CharIndexes(char_data=self)

        lang_data = LangData(search)
        script = ISOTools.split(ISOTools.guess_omitted_info(search)).script

        return_list = []
        for heading, ranges_string in lang_data.get_alpha_list():
            LOut = []
            for i_s in UnicodeSet(self, char_indexes, ranges_string):
                LOut.extend([ord(i) for i in i_s])
            # return_list.extend(LOut)

            return_list.append(('block', (heading, '')))
            return_list.append(('chars', LOut))
            # return_list.append((heading, LOut))

        for typ1, typ2, i_L in lang_data.get_symbols_list():
            for heading, chars in i_L:
                if typ2:
                    # ??? What does typ1/typ2 do again??
                    heading = '%s %s' % (typ2, heading)

                if typ1:
                    heading = '%s %s' % (typ1, heading)

                if heading.startswith("latn") and script != 'Latn':
                    # Ignore Latin perMille etc for langauge
                    # which don't use Latin scripts
                    continue

                if heading.startswith('arab') and script != 'Arab':
                    # Ignore arabic group, etc for languages
                    # which don't use the Arabic script
                    continue

                LExtend = [ord(i) for i in chars]
                return_list.append(('block', (heading, '')))
                return_list.append(('chars', LExtend))
                # return_list.extend(LExtend)
                # return_list.append((heading, LExtend))

        # from pprint import pprint
        # pprint(return_list)

        # lang_data.get_currency_symbol()
        # lang_data.locale_pattern()
        # lang_data.ellipsis()
        # lang_data.quotes('')
        # lang_data.paranthesis('')
        return return_list

    #===================================================================#
    #            Group Ranges by Chinese Frequency Headings             #
    #===================================================================#

    DGrades = {
        'unihan.grade': 'Hong Kong Grade',
        'kanjidic.grade': 'Japanese Grade'
    }

    @copydoc(CharDataBase.group_by_chinese_frequency)
    def group_by_chinese_frequency(self, LRanges, LSortBy):
        """
        Group by frequencys/grade etc under subheadings
        """

        DRanges = {}
        for ord_ in LRanges:
            freq = self.formatted(LSortBy[0], ord_)

            if freq is None:
                if False:
                    continue
                elif ord_ > 65536:
                    freq = 'extremely uncommon'
                else:
                    freq = 'very uncommon'

            elif LSortBy[0] in DGrades:
                freq = '%s %s' % (DGrades[LSortBy[0]], freq)

            if not freq in DRanges:
                DRanges[freq] = []
            DRanges[freq].append(ord_)

        # Group by secondary sort key
        return_list = []
        LKeys = list(DRanges.keys())
        if LSortBy[0] in DGrades or True:
            nLKeys = []
            for key in LKeys:
                if key == 'extremely uncommon':
                    nLKeys.append((65538, key))
                elif key == 'very uncommon':
                    nLKeys.append((65537, key))
                else:
                    # print key
                    try:
                        if key.split('/')[0].isalnum():
                            nLKeys.append((int(key.split('/')[0]), key))
                        else:
                            nLKeys.append((int(key.split()[-1]), key))
                    except:
                        nLKeys.append((65536, key))  # HACK!

            nLKeys.sort()
            LKeys = [i[1] for i in nLKeys]
        else:
            LKeys.sort()

        for key in LKeys:
            return_list.append(('sub_block', [key, None]))
            return_list.append(['chars', []])

            for ord_ in DRanges[key]:
                LCodePointOrder = []

                for sort in LSortBy[1:]:
                    freq = self.formatted(sort, ord_)
                    LCodePointOrder.append(freq)

                return_list[-1][1].append((LCodePointOrder, ord_))

            return_list[-1][1].sort()
            return_list[-1][1] = [i[1] for i in return_list[-1][1]]
        return return_list

    #===================================================================#
    #           Group Ranges by Japanese Frequency Headings             #
    #===================================================================#

    # Please DON'T over-experiment - it may make some queries
    # nicer, but there are *always* exceptions :-)
    JFREQ_AMOUNT = 500

    @copydoc(CharDataBase.group_by_japanese_frequency)
    def group_by_japanese_frequency(self, LRanges):
        # Group by frequency/grade etc under subheadings
        DRanges = {}
        for ord_ in LRanges:
            frequency = self.raw_data('kanjidic.freq', ord_)

            if frequency is None:
                if False:
                    continue
                elif ord_ > 65536:
                    key = 'extremely uncommon'
                else:
                    key = 'very uncommon'
            else:
                frequency = frequency[0]
                key = frequency // JFREQ_AMOUNT

            if not key in DRanges:
                DRanges[key] = []
            DRanges[key].append((frequency, ord_))

        LKeys = list(DRanges.keys())
        LKeys.sort()

        return_list = []
        for key in LKeys:
            if type(key) == int:
                from_ = key * JFREQ_AMOUNT
                to = from_ + (JFREQ_AMOUNT - 1)
                sub_block = 'Japanese frequencies %s - %s' % (from_, to)
            else:
                sub_block = key

            DRanges[key].sort()

            return_list.append(('sub_block', [sub_block, None]))
            return_list.append(['chars', [i[1] for i in DRanges[key]]])
        return return_list
