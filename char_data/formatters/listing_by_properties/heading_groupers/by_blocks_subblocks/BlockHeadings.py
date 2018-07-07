from char_data.data_paths import data_path
import sys
print sys.modules.keys()

from char_data import char_data
from char_data.misc.get_font_script import get_font_script


BLOCK_CHANGE = 0
NO_BLOCK_CHANGE = 1


class BlockHeadings:
    #=============================================================================#
    #                           Iterate Through Ranges                            #
    #=============================================================================#

    def get_L_block_headings(self, LRanges):
        DState = {
            'font_script': None,
            'last_block': -1,
            'last_sub_block': -1
        }

        LRtn = []
        for ord_ in LRanges:
            if type(ord_) == tuple:
                self._process_range(LRtn, DState, ord_)
            else:
                self._process_codepoint(LRtn, DState, ord_)

        return DState['font_script'] or 'All', LRtn

    def _process_range(self, LRtn, DState, ord_):
        """
        A range. If the first BlockName item is None and the last item is None
        OR the last BlockName doesn't equal the first BlockName
        """
        from_, to = ord_

        if (
            DState['font_script'] is None or
            DState['font_script'] in ('Common', 'Inherited')
        ):
            # **Guess** the font class to use, e.g. "Latin" or "Cyrillic"
            # based on the first character found with both a script and
            # a script which has a font class in CSS

            for i_code in xrange(from_, to+1):
                #print 'TUPLE FALLBACK!'
                new_font_script = get_font_script(i_code)
                if new_font_script:
                    DState['font_script'] = new_font_script
                    break

        from_block = char_data.formatted('block', from_)
        to_block = char_data.formatted('block', to)

        # Define various conditionals
        last_equal = DState['last_block'] == from_block
        from_equals_to = from_block == to_block
        from_is_None = from_block is None

        if last_equal and from_equals_to and not from_is_None:
            # block unchanged, so only iter sub_block without changing block
            self.iter_sub_range(LRtn, ord_, DState, NO_BLOCK_CHANGE)

        elif from_equals_to and not from_is_None:
            # block changed, change and iter sub_block without changing block
            LRtn.append(('block', from_block))
            DState['last_block'] = from_block

            self.iter_sub_range(LRtn, ord_, DState, NO_BLOCK_CHANGE)

        else:
            # Otherwise, the following are possible:
            # 1: The from_block != to_block, so check each ord_ for changes
            # 2: The from_block is None, in which case it could change mid-range
            # 3: A combination of the above two
            self.iter_sub_range(LRtn, ord_, DState, BLOCK_CHANGE)

    def _process_codepoint(self, LRtn, DState, ord_):
        """
        A codepoint, only one SubName required
        """
        block = char_data.formatted('block', ord_)
        sub_block = None

        if block and not 'CJK' in block:
            sub_block = char_data.formatted('subblock heading', ord_)

        if (
            DState['font_script'] is None or
            DState['font_script'] in ('Common', 'Inherited')
        ):
            #print 'SINGLE FALLBACK!'
            new_font_script = get_font_script(ord_)
            if new_font_script:
                DState['font_script'] = new_font_script

        # Update block name/block subnames if they've changed
        if block != DState['last_block']:
            LRtn.append(('block', block))
            DState['last_block'] = block

        if sub_block and sub_block != DState['last_sub_block']:
            LRtn.append(('sub_block', sub_block))
            DState['last_sub_block'] = sub_block

        # Append to the last "chars" entry to save space if possible
        if LRtn[-1][0] != 'chars':
            LRtn.append(('chars', []))
        LRtn[-1][1].append(ord_)

    #=============================================================================#
    #                         Iterate Through Sub-Ranges                          #
    #=============================================================================#

    def iter_sub_range(self, LRtn, LRange, DState, flag):
        from_, to = LRange
        from_sub_block = char_data.formatted('subblock heading', from_)
        to_sub_block = char_data.formatted('subblock heading', to)

        # Define various conditionals
        last_equal = DState['last_sub_block'] == from_sub_block
        from_equals_to = from_sub_block == to_sub_block
        from_none = from_sub_block is None

        if last_equal and from_equals_to and not from_none:
            # Subblock unchanged, so just append the range
            if LRtn[-1][0] != 'chars':
                LRtn.append(('chars', []))
            LRtn[-1][1].append(LRange)

        elif from_equals_to and not from_none:
            # Subblock changed, change and iter sub_block without changing block
            LRtn.append(('sub_block', from_sub_block))
            DState['last_sub_block'] = from_sub_block

            if LRtn[-1][0] != 'chars':
                LRtn.append(('chars', []))
            LRtn[-1][1].append(LRange)

        else:
            # Otherwise, the following are possible:
            # 1: The FromBlock != ToBlock, so check each ord_ for changes
            # 2: The FromBlock is None, in which case it could change mid-range
            # 3: A combination of the above two

            # TODO: ADD RANGE SUPPORT!
            # TODO: ADD FROMBLOCK == TOBLOCK BREAKING FOR e.g. Hangul!

            for ord_ in xrange(from_, to+1):
                if flag == BLOCK_CHANGE:
                    block = char_data.formatted('block', ord_)

                    if block != DState['last_block']:
                        # Change block, but only if changed as this code
                        # can be triggered if from_ equals None
                        LRtn.append(('block', block))
                        DState['last_block'] = block

                sub_block = char_data.formatted('subblock heading', ord_)

                if sub_block != DState['last_sub_block']:
                    LRtn.append(('sub_block', sub_block))
                    DState['last_sub_block'] = sub_block

                if LRtn[-1][0] != 'chars':
                    LRtn.append(('chars', []))

                # TODO: Add range support!
                LRtn[-1][1].append(ord_)


block_headings = BlockHeadings()
get_L_block_headings = block_headings.get_L_block_headings


if __name__ == '__main__':
    from char_data import char_indexes, char_data

    from pprint import pprint
    pprint(char_indexes.keys())
    pprint(char_data.keys())

    pprint(get_L_block_headings(
        char_indexes.search('unicodedata.script', 'Latin')
    ))

