from char_data.misc.get_font_script import get_font_script


BLOCK_CHANGE = 0
NO_BLOCK_CHANGE = 1


class BlockHeadings:
    def __init__(self, char_data):
        self.char_data = char_data

    #=============================================================================#
    #                           Iterate Through Ranges                            #
    #=============================================================================#

    def get_L_block_headings(self, LRanges):
        DState = {
            'font_script': None,
            'last_block': -1,
            'last_sub_block': -1
        }

        return_list = []
        for ord_ in LRanges:
            if isinstance(ord_, (tuple, list)):
                for i_ord in range(ord_[0], ord_[1]+1):
                    # HACK: Fix Arabic subblock comment/title issues
                    self._process_codepoint(return_list, DState, i_ord)
                #self._process_range(return_list, DState, ord_)
            else:
                self._process_codepoint(return_list, DState, ord_)

        return DState['font_script'] or 'All', return_list

    def _process_range(self, return_list, DState, ord_):
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

            for i_code in range(from_, to+1):
                #print 'TUPLE FALLBACK!'
                new_font_script = get_font_script(i_code)
                if new_font_script:
                    DState['font_script'] = new_font_script
                    break

        from_block = self.char_data.formatted('block', from_)
        to_block = self.char_data.formatted('block', to)

        # Define various conditionals
        last_equal = DState['last_block'] == from_block
        from_equals_to = from_block == to_block
        from_is_None = from_block is None

        if last_equal and from_equals_to and not from_is_None:
            # block unchanged, so only iter sub_block without changing block
            self.iter_sub_range(return_list, ord_, DState, NO_BLOCK_CHANGE)

        elif from_equals_to and not from_is_None:
            # block changed, change and iter sub_block without changing block
            self.append_block(return_list, from_block, from_)
            DState['last_block'] = from_block

            self.iter_sub_range(return_list, ord_, DState, NO_BLOCK_CHANGE)

        else:
            # Otherwise, the following are possible:
            # 1: The from_block != to_block, so check each ord_ for changes
            # 2: The from_block is None, in which case it could change mid-range
            # 3: A combination of the above two
            self.iter_sub_range(return_list, ord_, DState, BLOCK_CHANGE)

    def _process_codepoint(self, return_list, DState, ord_):
        """
        A codepoint, only one SubName required
        """
        block = self.char_data.formatted('block', ord_)
        sub_block = None
        #print DState['last_sub_block']

        if block and not 'CJK' in block:
            sub_block = self.char_data.formatted('subblock heading', ord_)

        if (
            DState['font_script'] is None or
            DState['font_script'] in ('Common', 'Inherited')
        ):
            #print 'SINGLE FALLBACK!'
            new_font_script = get_font_script(self.char_data, ord_)
            if new_font_script:
                DState['font_script'] = new_font_script

        # Update block name/block subnames if they've changed
        if block != DState['last_block']:
            self.append_block(return_list, block, ord_)
            DState['last_block'] = block

        if sub_block and sub_block != DState['last_sub_block']:
            self.append_sub_block(return_list, sub_block, ord_)
            DState['last_sub_block'] = sub_block

        # Append to the last "chars" entry to save space if possible
        if return_list[-1][0] != 'chars':
            return_list.append(('chars', []))
        return_list[-1][1].append(ord_)

    def append_block(self, return_list, block, ord_):
        """
        Append a block, including block description if it exists
        """
        desc = self.char_data.formatted('block description', ord_)

        if desc:
            return_list.append(
                ('block', [block, '. '.join(i.strip('.') for i in desc)])
            )
        else:
            return_list.append(
                ('block', [block, None])
            )

    #=============================================================================#
    #                         Iterate Through Sub-Ranges                          #
    #=============================================================================#

    def iter_sub_range(self, return_list, LRange, DState, flag):
        from_, to = LRange
        from_sub_block = self.char_data.formatted('subblock heading', from_)
        to_sub_block = self.char_data.formatted('subblock heading', to)

        # Define various conditionals
        last_equal = DState['last_sub_block'] == from_sub_block
        from_equals_to = from_sub_block == to_sub_block
        from_none = from_sub_block is None

        if last_equal and from_equals_to and not from_none:
            # Subblock unchanged, so just append the range
            if return_list[-1][0] != 'chars':
                return_list.append(('chars', []))
            return_list[-1][1].append(LRange)

        elif from_equals_to and not from_none:
            # Subblock changed, change and iter sub_block without changing block
            self.append_sub_block(return_list, from_sub_block, from_)
            DState['last_sub_block'] = from_sub_block

            if return_list[-1][0] != 'chars':
                return_list.append(('chars', []))
            return_list[-1][1].append(LRange)

        else:
            # Otherwise, the following are possible:
            # 1: The FromBlock != ToBlock, so check each ord_ for changes
            # 2: The FromBlock is None, in which case it could change mid-range
            # 3: A combination of the above two

            # TODO: ADD RANGE SUPPORT!
            # TODO: ADD FROMBLOCK == TOBLOCK BREAKING FOR e.g. Hangul!

            for ord_ in range(from_, to+1):
                if flag == BLOCK_CHANGE:
                    block = self.char_data.formatted('block', ord_)

                    if block != DState['last_block']:
                        # Change block, but only if changed as this code
                        # can be triggered if from_ equals None
                        #return_list.append(('block', block))
                        self.append_block(return_list, block, ord_)
                        DState['last_block'] = block

                sub_block = self.char_data.formatted('subblock heading', ord_)

                if sub_block != DState['last_sub_block']:
                    self.append_sub_block(return_list, sub_block, ord_)
                    DState['last_sub_block'] = sub_block

                if return_list[-1][0] != 'chars':
                    return_list.append(('chars', []))

                # TODO: Add range support!
                return_list[-1][1].append(ord_)

    def append_sub_block(self, return_list, sub_block, ord_):
        """
        Append, including:
        * subblock technical notice
        * subblock see also
        if that information is available, along with the subblock
        """
        tech_notice = self.char_data.formatted('subblock technical notice', ord_)
        see_also = self.char_data.raw_data('subblock see also', ord_)

        if tech_notice:
            tech_notice = '. '.join(i.strip('.') for i in tech_notice)

        if see_also:
            # [[734, "modifier letter rhotic hook"], ...]
            see_also = 'See also %s' % see_also # FIXME: WHY IS THIS A UNICODE TYPE???? ===========================================================
            #print see_also, see_also[0], type(see_also)
            #see_also = 'See also %s' % (
            #    '; '.join(
            #        '%s %s' % (i_ord, desc) for i_ord, desc in see_also
            #    )
            #)

        comment = ''
        if tech_notice and see_also:
            comment = '%s. %s' % (tech_notice, see_also)
        elif tech_notice:
            comment = tech_notice
        elif see_also:
            comment = see_also

        if comment:
            return_list.append(
                ('sub_block', ['. '.join(sub_block), comment])
            )
        else:
            return_list.append(
                ('sub_block', ['. '.join(sub_block), None])
            )


if __name__ == '__main__':
    from char_data.CharData import CharData
    from char_data.CharIndexes import CharIndexes

    char_data = CharData()
    char_indexes = CharIndexes(char_data=char_data)

    from pprint import pprint
    pprint(list(char_indexes.keys()))
    pprint(list(char_data.keys()))

    block_headings = BlockHeadings(char_data=char_data)
    pprint(BlockHeadings(
        char_data,
        char_indexes.search('unicodedata.script', 'Arabic')
    ))
