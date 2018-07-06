# -*- coding: utf-8 -*-
from collections import namedtuple
import re
from re import compile, IGNORECASE, I
import zhon.hanzi, zhon.pinyin


cn = (
    zhon.hanzi.characters +
    zhon.hanzi.radicals +
    u'、。；，・'

).replace(
    '[', ''
).replace(
    ']', ''
).replace(
    '|', ''
)

cedict_re = compile(
    '((?:\\b[^\\s])*[%s]+(?:\\b[^\\s])*)(\|(?:\\b[^\\s])*[%s]+(?:\\b[^\\s])*)?(\[(?:%s|(?:\s|:))+\])?' % (
        cn, cn, zhon.pinyin.numbered_word
    ),
    IGNORECASE
)
ZhWord = namedtuple('ZhWord', ['trad', 'simp', 'pinyin'])


def get_L_cedict_hanzi(s):
    """
    Get the Hanzi from string "s"
    """

    LRtn = []

    def fn(m):
        trad, simp, pinyin = m.groups()

        simp = simp[1:] if simp else trad
        pinyin = pinyin[1:-1] if pinyin else None

        LRtn.append(
            ZhWord(trad.strip(':'), simp.strip(':'), pinyin)
        )
        return ''

    cedict_re.sub(fn, s)
    return LRtn


if __name__ == '__main__':
    print get_L_cedict_hanzi(u'靈渠|灵渠[Ling2 qu2]')
    print get_L_cedict_hanzi(u'靈渠[Ling2 qu2]')
    print get_L_cedict_hanzi(u'靈渠|灵渠[Ling2 qu2]')
    print get_L_cedict_hanzi(u'靈渠|灵渠[nu:]')
    print get_L_cedict_hanzi(u'靈渠|灵渠')
    print get_L_cedict_hanzi(u'靈渠')

    print get_L_cedict_hanzi(u'a b靈渠')
