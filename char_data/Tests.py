# -*- coding: utf-8 -*-
import os
from pprint import pprint
from char_data.formatters.radicals import SimilarHanzi

from char_data.CharInfo import formatted, char_data.raw_data, keys, idx_keys, idx_values, char_indexes.search

#pprint(keys())
#pprint(idx_keys())
#print idx_values('general category')
#print char_indexes.search('general category', 'Ps')
#print

#raise

#print formatted('japanesesimplified', u'轉')
#print formatted('chinesetraditional', u'転')
#print formatted('Japanese variant', u'轉')
#print formatted('name', 'a')
#print char_data.raw_data('name', 'z')

def test(chars):
    for ord_ in chars:
        if isinstance(ord_, basestring):
            ord_ = ord(ord_)

        print ord_
        #print keys()
        
        for key in sorted(keys()):


            try:
                raw_ = char_data.raw_data(key, ord_)
                if raw_:
                    print key, char_data.raw_data(key, ord_), formatted(key, ord_)
            except:
                import traceback
                traceback.print_exc()
                
                print 'ERROR:', key, unichr(ord_), ord_, hex(ord_)
        
        if ord_ % 1000 == 0: 
            print ord_
        #print

from cProfile import run
#test(u'㐀㐅厝意')
#run('test(xrange(300000))')
#print test(u'abc')
print test(u'～〜~')

#i = SimilarHanzi(None, None)
#for ord_ in u'藤意総思心認感必応急優態想念':
#    print ord_, i.formatted(ord(ord_))[:50]
#    print

'''
Traceback (most recent call last):
  File "F:\Dev\Flazzle-NewJS\Chars\Tests.py", line 19, in test
ERROR: ('unihan', 'rsunicode') 卤 21348 0x5364
    key, char_data.raw_data(key, ord_), formatted(key, ord_)
  File "F:\Dev\Flazzle-NewJS\Chars\CharData.py", line 82, in formatted
    return inst.formatted(ord_)
  File "F:\Dev\Flazzle-NewJS\Chars\Formatters\Radicals\RadicalStrokes.py", line 41, in formatted
    for i_strokes, i_radical, i_eng_name in DRads[radical]:
KeyError: "197'"

Traceback (most recent call last):
  File "F:\Dev\Flazzle-NewJS\Chars\Tests.py", line 19, in test
ERROR: ('unihan', 'rsunicode') 辶 36790 0x8fb6
    key, char_data.raw_data(key, ord_), formatted(key, ord_)
  File "F:\Dev\Flazzle-NewJS\Chars\CharData.py", line 82, in formatted
    return inst.formatted(ord_)
  File "F:\Dev\Flazzle-NewJS\Chars\Formatters\Radicals\RadicalStrokes.py", line 41, in formatted
    for i_strokes, i_radical, i_eng_name in DRads[radical]:
KeyError: "162'"

Traceback (most recent call last):
  File "F:\Dev\Flazzle-NewJS\Chars\Tests.py", line 19, in test
ERROR: ('unihan', 'rsunicode') 鹾 40574 0x9e7e
    key, char_data.raw_data(key, ord_), formatted(key, ord_)
  File "F:\Dev\Flazzle-NewJS\Chars\CharData.py", line 82, in formatted
    return inst.formatted(ord_)
  File "F:\Dev\Flazzle-NewJS\Chars\Formatters\Radicals\RadicalStrokes.py", line 41, in formatted
    for i_strokes, i_radical, i_eng_name in DRads[radical]:
KeyError: "197'"

Traceback (most recent call last):
  File "F:\Dev\Flazzle-NewJS\Chars\Tests.py", line 19, in test
    key, char_data.raw_data(key, ord_), formatted(key, ord_)
  File "F:\Dev\Flazzle-NewJS\Chars\CharData.py", line 82, in formatted
    return inst.formatted(ord_)
  File "F:\Dev\Flazzle-NewJS\Chars\Formatters\Radicals\RadicalStrokes.py", line 41, in formatted
    for i_strokes, i_radical, i_eng_name in DRads[radical]:
KeyError: "201'"
ERROR: ('unihan', 'rsunicode') 黄 40644 0x9ec4
'''
