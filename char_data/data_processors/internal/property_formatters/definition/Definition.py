import unicodedata

#from Dicts.Misc.TextOut import w_readings
#from Data.Languages import Langs
from char_data.data_processors.internal.data_types.read import SentenceData


class Definition(SentenceData):
    def raw_data(self, ord_):
        if self.key == 'name' and ord_ >= 0xAC00 and ord_ <= 0xD7AF:
            # HACK: Use the unicodedata module for Hangul
            try:
                r = unicodedata.name(chr(ord_))
                return (r,) if r else None
            except: 
                return None
        
        # Add UnicodeData Name
        return SentenceData.raw_data(self, ord_)

    def _format_data(self, ord_, data):
        if data:
            # prevent ALL CAPS!
            L = []

            for i in data:
                if self.key == 'comments' and i and i[0] == '*':
                    if i.count('*') == 1:
                        i = i.strip('*')
                        if i:
                            L.append(i)
                    else:
                        L.extend([
                            j.strip() for j in
                            i.replace('\n', ' ').split('*')
                            if j.strip()
                        ])

                elif i.isupper():
                    i = i.lower()
                    if i:
                        L.append(i)

            data = tuple(L) if L else None

        # Provide better formatting for "Comment" fields like e.g.
        #  * intended to surround a diacritic above
        # parsing asterisks, etc as needed


        return data # HACK! =====================================================

    def add_sounds(self, s, iso, script):
        LRtn = []
        if type(s) == tuple: 
            s = s[0] # HACK!
        elif s is None:
            return None # HACK!
        
        DLangs = Langs.DLangs
        
        for reading in s.split(' '): # CHECK ME!
            profile = DLangs[iso][0]
            DFrom = {'iso': iso, 
                     'DLang': DLangs[iso][1][profile], 
                     'LTrans': [script, script, None]} # HACK!
            sound = w_readings(DFrom, reading, script=script, 
                               pron_popup=True, show_snd=True)
            
            if sound: 
                reading = sound
            
            LRtn.append(reading)
        
        return (' '.join(LRtn),)
