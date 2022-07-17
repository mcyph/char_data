from char_data.CharData import CharData


class _ShortCharDefinitions:
    def __init__(self, char_data, key='unicodedata.name'):
        self.key = key

        self.cur_block = None
        self.cur_subblock = None

        self.SCurSubblockTokens = set()
        self.SCurBlockTokens = set()

        self.char_data = char_data

    def get_short_char_definitions(self, LChars):
        LOut = []

        for key, item in LChars:
            if key == 'block':
                self.cur_block = item[0]
                self.SCurBlockTokens = set(self._get_L_tokens(self.cur_block))
                LOut.append((key, item))

            elif key == 'sub_block':
                self.cur_subblock = item[0]
                self.SCurSubblockTokens = set(self._get_L_tokens(self.cur_subblock))
                LOut.append((key, item))

            elif key == 'chars':
                LNewChars = []

                for chars in item:
                    if isinstance(chars, int):
                        # A single codepoint
                        LNewChars.append(self._codepoint_processed(chars))
                    else:
                        # A range
                        LNewChars.extend(self._range_processed(*chars))

                LOut.append(('chars', LNewChars))

            elif key == 'compound_char':
                LOut.append((key, item))

            else:
                raise Exception("Unknown chardata key: %s" % key)

        return LOut

    def _range_processed(self, from_ord, to_ord):
        return_list = []
        for ord_ in range(from_ord, to_ord):
            return_list.append(self._codepoint_processed(ord_))
        return return_list

    def _codepoint_processed(self, ord_):
        # TODO: add su
        value = self.char_data.formatted(self.key, ord_)

        if value:
            value = ' '.join(
                i for i in value[0].split() if not (  # CHECK if there's other values here!!!!! =============================
                    self._stemmed(i.lower()) in self.SCurBlockTokens or
                    self._stemmed(i.lower()) in self.SCurSubblockTokens
                )
            )
            return [ord_, [value]]
        else:
            return ord_

    def _get_L_tokens(self, s):
        if s is None:
            return []  # CHECK ME!!

        s = s.lower()
        LTokens = [
            self._stemmed(i.strip()) for i in s.split()
        ]
        return LTokens

    def _stemmed(self, s):
        if len(s) > 1 and s[-2] != 's' and s[-1] == 's':
            # plural hack: it may (or may not) be better
            # to use a proper stemmer/lemmatizer here,
            #
            # depending on whether the headings will
            # contain other kinds of lexeme variants
            return s[:-1]
        else:
            return s


def get_short_char_definitions(LChars, char_data):
    inst = _ShortCharDefinitions(char_data=char_data)
    return inst.get_short_char_definitions(LChars)

