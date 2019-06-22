# -*- coding: utf-8 -*-
#from Chars.Radicals.MultiRad import DBothChars
from toolkit.encodings.surrogates import w_unichr

from char_data.data_processors.external.property_formatters import ExternalBaseClass
from char_data.data_processors.consts import HEADER_RADICAL_STROKES


class MultiRadicals(ExternalBaseClass):
    def __init__(self, parent):
        ExternalBaseClass.__init__(
            self, parent, HEADER_RADICAL_STROKES, original_name='multi_radicals',
            short_desc='multi_radicals', LISOs=None
        )

    def raw_data(self, ord_):
        char = w_unichr(ord_)
        
        if char in DBothChars:
            return ' '.join(tuple([i for i in DBothChars[char] if i != '�']))
        else:
            return None

    def _format_data(self, ord_, data):
        # Add multi-radical mappings
        return data # TODO: Make me more pretty! ==============================
