from char_data.storage.data.read import StringData
from DCangjie import DCangjie


class NoFormatStrings(StringData):  # WARNING! ============================================================
    def _format_data(self, ord_, data):
        # As the name suggests, don't do any processing, just return
        if self.key == 'cangjie' and data:
            # CANGJIE HACK!
            # TODO: Move to a separate type :-P
            LRtn = []
            for c in data:
                if c in DCangjie:
                    LRtn.append(DCangjie[c][0])
                else:
                    LRtn.append('?')
            return '%s (%s)' % (data, ''.join(LRtn))
        return data

