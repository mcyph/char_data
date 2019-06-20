# -*- coding: utf-8 -*-
from .tokenizer.UnicodeSetParse import RANGES, STRING, OPERATOR
from .tokenizer.UnicodeSetParse import get_unicode_set_ranges

"""
This file contains an implementation of UnicodeSet in ICU.

There are likely gaps in its implementation. It was intended 
to be used for a parser for ICU's transliteration system.
"""


class Difference:
    def __init__(self, o1, o2):
        self.o1 = o1
        self.o2 = o2

    def contains(self, c):
        return (
            c in self.o1 and
            not c in self.o2
        )

    def __iter__(self):
        for c in self.o1:
            if not c in self.o2:
                yield c


class Intersect:
    def __init__(self, o1, o2):
        self.o1 = o1
        self.o2 = o2

    def contains(self, c):
        return (
            c in self.o1 and
            c in self.o2
        )

    def __iter__(self):
        for c in self.o1:
            if c in self.o2:
                yield c


class Ranges:
    def __init__(self, neg, L):
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
                        cur_item = unicodeset_from_token(i[1][1])

                        if i[1][0] == '-':
                            LOut.append(Difference(prev_item, cur_item))
                        elif i[1][0] == '&':
                            LOut.append(Intersect(prev_item, cur_item))
                        else:
                            raise Exception(i)

                    else:
                        LOut.append(
                            unicodeset_from_token(i)
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


class String:
    def __init__(self, s):
        self.s = s

    def contains(self, c):
        return c == self.s

    def __iter__(self):
        yield self.s


DTypes = {
    RANGES: Ranges,
    STRING: String
}

def unicodeset_from_token(i):
    typ = i[0]
    return DTypes[typ](*i[1:])

def unicodeset_from_range(s):
    token = get_unicode_set_ranges(s)
    #print token
    return unicodeset_from_token(token)


if __name__ == '__main__':
    r = unicodeset_from_range(
        #"[a b c d e f g h i j k l m n o p q r s t u v w x y z]"
        #u"[a ä b c d e f g h i j k l m n o ö p q r s ß t u ü v w x y z]"
        #u"[一 丁 七 丈-不]"
        #u"[[a-c]-[b]]"
        #u"[[a-c]&[bc]]"
        "[a-vx-zá é í ó ú ý ñ ã ẽ ĩ õ ũ ỹ {g\\u0303}]"
    )
    for i in r:
        print(i)

    for c in 'a^':
        print((r.contains(c)))
