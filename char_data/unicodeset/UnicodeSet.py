# -*- coding: utf-8 -*-
from char_data.unicodeset.tokenizer.UnicodeSetParse import get_unicode_set_ranges
from char_data.unicodeset.classes.Ranges import Ranges
from char_data.unicodeset.classes.String import String
from char_data.unicodeset.consts import RANGES, STRING


"""
This file contains an implementation of UnicodeSet in ICU.

There are likely gaps in its implementation. It was intended 
to be used for a parser for ICU's transliteration system,
but is currently mainly used for parsing the alphabet 
information in Unicode CLDR data in a different module. 
"""


def UnicodeSet(char_data, s):
    """
    Return a new unicode set object, using a string.

    :param s: the string containing the unicode set ranges
    :param char_data: a CharData instance
    :return: a unicode set object (one of `Ranges` or `String`)
    """
    token = get_unicode_set_ranges(char_data, s)
    return unicode_set_from_token(char_data=char_data, i=token)


DTypes = {
    RANGES: Ranges,
    STRING: String
}


def unicode_set_from_token(char_data, i):
    """
    Create a unicode set from one of the tokens,
    as defined in DTypes (RANGES or STRING)
    Mainly meant to be used internally.

    :param i: the token
    :param char_data: a CharData instance
    :return: a unicode set object (one of `Ranges` or `String`)
    """
    typ = i[0]
    return DTypes[typ](char_data, *i[1:])


if __name__ == '__main__':
    r = UnicodeSet(
        char_data,
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
