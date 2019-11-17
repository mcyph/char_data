from lang_data import LangData
from iso_tools.ISOTools import ISOTools
from toolkit.documentation.copydoc import copydoc

from char_data.unicodeset.UnicodeSet import UnicodeSet
from char_data.misc.BlockHeadings import BlockHeadings
from char_data.misc import get_font_script, get_smallest_name
from char_data.abstract_base_classes.CharDataBase import CharDataBase


class HeadingGrouperBase:
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

        LRtn = []
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

                    LRtn.append((append, i_code))

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

                LRtn.append((append, ord_))

        # if not font_script: font_script = 'All'
        LRtn.sort()

        n_LRtn = []
        n_LRtn.append(('block', name))  # HACK!

        last_key = None
        for sort_key, ord_ in LRtn:
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
                    n_LRtn.append(
                        ['sub_block', ['Miscellaneous Symbols', None]]
                    )
                else:
                    n_LRtn.append(
                        ['sub_block', ['characters starting with "%s"' %
                                           chk_key.lower(),
                                       None]]
                    )

                n_LRtn.append(['chars', []])
            n_LRtn[-1][-1].append(ord_)

        # LRtn = [['chars', [i[1] for i in LRtn]]]
        return font_script, n_LRtn

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

        ld = LangData(search)
        script = ISOTools.split(ISOTools.guess_omitted_info(search)).script

        LRtn = []
        for heading, ranges_string in ld.get_L_alpha():
            LOut = []
            for i_s in UnicodeSet(self, char_indexes, ranges_string):
                LOut.extend([ord(i) for i in i_s])
            # LRtn.extend(LOut)

            LRtn.append(('block', (heading, '')))
            LRtn.append(('chars', LOut))
            # LRtn.append((heading, LOut))

        for typ1, typ2, i_L in ld.get_L_symbols():
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
                LRtn.append(('block', (heading, '')))
                LRtn.append(('chars', LExtend))
                # LRtn.extend(LExtend)
                # LRtn.append((heading, LExtend))

        # from pprint import pprint
        # pprint(LRtn)

        # ld.get_currency_symbol()
        # ld.locale_pattern()
        # ld.ellipsis()
        # ld.quotes('')
        # ld.paranthesis('')
        return LRtn

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
        LRtn = []
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
            LRtn.append(('sub_block', [key, None]))
            LRtn.append(['chars', []])

            for ord_ in DRanges[key]:
                LCodePointOrder = []

                for sort in LSortBy[1:]:
                    freq = self.formatted(sort, ord_)
                    LCodePointOrder.append(freq)

                LRtn[-1][1].append((LCodePointOrder, ord_))

            LRtn[-1][1].sort()
            LRtn[-1][1] = [i[1] for i in LRtn[-1][1]]
        return LRtn

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

        LRtn = []
        for key in LKeys:
            if type(key) == int:
                from_ = key * JFREQ_AMOUNT
                to = from_ + (JFREQ_AMOUNT - 1)
                sub_block = 'Japanese frequencies %s - %s' % (from_, to)
            else:
                sub_block = key

            DRanges[key].sort()

            LRtn.append(('sub_block', [sub_block, None]))
            LRtn.append(['chars', [i[1] for i in DRanges[key]]])
        return LRtn
