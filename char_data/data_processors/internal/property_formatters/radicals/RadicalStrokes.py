# -*- coding: utf-8 -*-
from char_data.data_processors.internal.data_types.read import StringData
from char_data.abstract_base_classes.formatters.InternalFormatterBase import InternalFormatterBase


class RadicalStrokes(StringData):
    def __init__(self, parent, header_const, original_name, short_desc,
                 long_desc=None, LISOs=None, index_type=None):

        InternalFormatterBase.__init__(
            self, parent, header_const, original_name, short_desc,
            long_desc=long_desc, LISOs=LISOs, index_type=index_type
        )

        # TODO: PLEASE REWRITE DRadTypes to use the ISO codes or new keys!

        '''LRadInfo = DRadTypes[self.key]
        traditional = LRadInfo[0]

        if traditional == True:
            kind = KANGXI_TRADITIONAL
        elif traditional == False:
            kind = KANGXI_SIMPLIFIED
        elif traditional == 'Both':
            kind = KANGXI_BOTH
        else:
            raise Exception("Unknown kind: %s" % traditional)

        self.DRads = kangxi_data.get_D_indexed_by_key('numeric_id', kind)
        '''

    def _format_data(self, ord_, data):
        # TODO: Split into (radical, Additional Strokes) and display as
        # the actual radical using radical.py:
        # %(radical)s (%(Additional Strokes)s Additional Strokes)
        # TODO: Should there be an Adobe/CheungBauer parser?
        if not data:
            return None

        L = []
        for x in data.strip().split(' '):
            radical, extra_strokes = x.split('.')
            if not radical:
                # CCDict "㽍" etc HACK!
                continue
            
            # CCDict multiple values HACK!
            extra_strokes = int(extra_strokes.rstrip(';'))

            new_radical = radical # HACK!
            #new_radical = ''
            #for rad_inst in self.DRads[radical]:
            #    new_radical += rad_inst.kangxi
            
            radical = new_radical
            L.append('%s with %s extra strokes' % (radical, extra_strokes))

        data = '/'.join(L)
        return data or None
