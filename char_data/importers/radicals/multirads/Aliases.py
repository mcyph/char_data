# -*- coding: utf-8 -*-

"""
DStrokeCounts gives the number of strokes for Katakana 
etc which don't have a unihan.TotalStrokes entry
"""
DStrokeCounts = {
    u'ノ': 1,
    u'ハ': 2,
    u'マ': 2,
    u'ユ': 2,
    u'ヨ': 3,
    u'｜': 1
}

DRadAliases =   {
    u'言': u'讠訁',
    u'食': u'饣飠',
    u'糸': u'纟糹',
    u'金': u'钅釒',
    u'｜': u'丨丨'
}

"""
This provides a "break-down" of more complicated radicals 
into simpler ones so that beginners can find characters 
more easily, even if sometimes this isn't technically correct
"""
DAlternate =    {
    u'化': u'亻',
    u'刈': u'刂',
    u'扎': u'扌',
    u'邦': u'阝',

    # HACK: This uses the above radical on the left but I've
    # assigned it to be the same as above for usability
    u'阡': u'阝',

    u'艾': u'艹',
    u'杰': u'灬',
    u'買': u'罒',
    u'込': u'辶',
    u'汁': u'氵',
    u'犯': u'犭',
    #u'麦': u'?',
    u'礼': u'礻',
    u'忙': u'忄'
}

"""
Sometimes big multirads can be divided themselves into 
smaller 'parts' to make things easier to find
e.g. 里 has "Paddy" and "Earth
but it makes sense to leave the existing mapping
TODO: Should 气 be mapped to something?

A LOT of these are strictly speaking incorrect, but as
e.g. "土" looks like "士" in a small font, I'd argue they won't 
find the result, so it's better to show them as aliases, 
even though they have very different different meanings
"""

DRadAppend = {
    u'里': u'土田',
    u'麦': u'主',
    u'魚': u'勹',
    u'食': u'白个',
    u'比': u'匕',
    u'牙': u'口',
    u'赤': u'ハ',
    u'角': u'田',
    u'彳': u'亻', # CONTROVERSIAL :-)
    u'欠': u'人',
    u'无': u'ハ',
    u'曰': u'日',

    #u'子': u'一',
    #u'五': u'一',
    #u'犬': u'一',
    u'戸': u'一尸',
    #u'尤': u'一',
    u'元': u'一',
    #u'手': u'一',
    #u'王': u'一',
    #u'文': u'一',
    u'犬': u'大丶',

    u'青': u'月主',
    u'土': u'士', # Earth -> Scholar
    u'士': u'土', # Scholar -> Earth
    u'儿': u'ハ',
    u'ハ': u'儿',
    u'戶': u'尸',
    u'个': u'人',
    u'人': u'个',
    u'歯': u'齒止囗米人一',
    u'齒': u'歯止囗米人一',
    u'足': u'止囗',
    u'禾': u'人二木大'
}
