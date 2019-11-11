from char_data.unicodeset.classes.Difference import Difference
from char_data.unicodeset.classes.Intersect import Intersect
from char_data.unicodeset.consts import OPERATOR


class Ranges:
    def __init__(self, char_indexes, neg, L):
        from char_data.unicodeset.UnicodeSet import unicode_set_from_token
        self.char_indexes = char_indexes

        LOut = []

        x = -1
        while 1:
            x += 1
            try:
                i = L[x]
            except IndexError:
                break

            if isinstance(i, (tuple, list)):
                if isinstance(i[0], int):
                    # A subitem
                    if i[0] == OPERATOR:
                        prev_item = LOut.pop()
                        cur_item = unicode_set_from_token(
                            i[1][1], char_indexes=self.char_indexes
                        )

                        if i[1][0] == '-':
                            LOut.append(Difference(prev_item, cur_item))
                        elif i[1][0] == '&':
                            LOut.append(Intersect(prev_item, cur_item))
                        else:
                            raise Exception(i)

                    else:
                        LOut.append(
                            unicode_set_from_token(
                                i, char_indexes=self.char_indexes
                            )
                        )
                else:
                    LOut.append(i)
            else:
                # Probably an instance/string
                LOut.append(i)

        self.neg = neg
        self.L = LOut

    def contains(self, c):
        r = False
        for i in self.L:
            if isinstance(i, (list, tuple)):
                # A range
                from_, to = i
                if (c >= from_) and (c <= to):
                    r = True
                    break

            elif isinstance(i, str):
                # A string (this can be more than a single char)
                if i == c:
                    r = True
                    break

            else:
                # An instance, so forward
                if i.contains(c):
                    r = True
                    break

        if self.neg:
            r = not r
        return r

    def __iter__(self):
        if self.neg:
            # TODO: Implement me!
            raise NotImplementedError

        for i in self.L:
            if isinstance(i, (list, tuple)):
                # A range
                from_, to = i
                from_ = ord(from_)
                to = ord(to)

                for x in range(from_, to+1): # CHECK ME!
                    yield chr(x)

            elif isinstance(i, str):
                # A string
                yield i

            else:
                # An instance
                for x in i:
                    yield x

