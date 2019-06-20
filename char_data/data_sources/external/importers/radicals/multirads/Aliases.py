# -*- coding: utf-8 -*-

"""
DStrokeCounts gives the number of strokes for Katakana 
etc which don't have a unihan.TotalStrokes entry
"""
DStrokeCounts = {
    'ノ': 1,
    'ハ': 2,
    'マ': 2,
    'ユ': 2,
    'ヨ': 3,
    '｜': 1
}

DRadAliases =   {
    '言': '讠訁',
    '食': '饣飠',
    '糸': '纟糹',
    '金': '钅釒',
    '｜': '丨丨'
}

"""
This provides a "break-down" of more complicated radicals 
into simpler ones so that beginners can find characters 
more easily, even if sometimes this isn't technically correct
"""
DAlternate =    {
    '化': '亻',
    '刈': '刂',
    '扎': '扌',
    '邦': '阝',

    # HACK: This uses the above radical on the left but I've
    # assigned it to be the same as above for usability
    '阡': '阝',

    '艾': '艹',
    '杰': '灬',
    '買': '罒',
    '込': '辶',
    '汁': '氵',
    '犯': '犭',
    #u'麦': u'?',
    '礼': '礻',
    '忙': '忄'
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
    '里': '土田',
    '麦': '主',
    '魚': '勹',
    '食': '白个',
    '比': '匕',
    '牙': '口',
    '赤': 'ハ',
    '角': '田',
    '彳': '亻', # CONTROVERSIAL :-)
    '欠': '人',
    '无': 'ハ',
    '曰': '日',

    #u'子': u'一',
    #u'五': u'一',
    #u'犬': u'一',
    '戸': '一尸',
    #u'尤': u'一',
    '元': '一',
    #u'手': u'一',
    #u'王': u'一',
    #u'文': u'一',
    '犬': '大丶',

    '青': '月主',
    '土': '士', # Earth -> Scholar
    '士': '土', # Scholar -> Earth
    '儿': 'ハ',
    'ハ': '儿',
    '戶': '尸',
    '个': '人',
    '人': '个',
    '歯': '齒止囗米人一',
    '齒': '歯止囗米人一',
    '足': '止囗',
    '禾': '人二木大'
}
