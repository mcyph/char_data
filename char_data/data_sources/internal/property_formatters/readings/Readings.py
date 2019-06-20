from char_data.data_sources.internal.data.read import SentenceData
from char_data.data_sources.internal.property_formatters.hex import conv_hex

SNums = set(str(i) for i in range(10))


def _is_upper(S):
    return all(i.isupper() for i in S if i.strip() and i not in SNums)


class Readings(SentenceData):
    def _format_data(self, ord_, data):
        """
        The definitions are already in English, so just make sure 
        they aren't in a SHOUTING format and return them
        """
        if not data:
            return None
        
        elif type(data) in (tuple, list):
            LRtn = []
            for readings in data:
                if self.key in ('Japanese On', 'Japanese Kun', 'Japanese Nanori'):
                    readings = self.format_japanese(readings)
                
                elif self.key == 'Hanyu Pinyin':
                    # HACK: Remove the indices (??? assuming that's what they are)
                    readings = ' '.join([i.split(':')[-1] for i in readings.split()])
                    readings = readings.replace(',', ' ')
                
                elif self.key == 'Xiandai Hanyu Pinlu':
                    readings = readings.replace('(', ' (') # ' (freq ')
                    
                if _is_upper(data):
                    LRtn.append(conv_hex(self.key, readings.lower()))
                else: 
                    LRtn.append(conv_hex(self.key, readings))
            
            return tuple(LRtn)
        
        elif _is_upper(data):
            return conv_hex(self.key, data.title())
        
        else: 
            return conv_hex(self.key, data)

    def format_japanese(self, readings):
        LNew = []
        for reading in readings.split():
            '''
            Make Japanese On/Kun from format "Root.Stem" to "Root(Stem)"
            OPEN ISSUE: Should fullwidth brackets be used here?
            '''
            
            if '.' in reading:
                LSplit = reading.split('.')
                LNew.append('%s(%s)' % (LSplit[0], '.'.join(LSplit[1:])))
            else: 
                LNew.append(reading)
        
        return ' '.join(LNew)
