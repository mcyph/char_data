import unicodedata

#from Dicts.Misc.TextOut import w_readings
#from Data.Languages import Langs
from char_data.storage.data.read import SentenceData


class Definition(SentenceData):
    def raw_data(self, ord_):
        if self.key=='Name' and ord_>=0xAC00 and ord_<=0xD7AF:
            # HACK: Use the unicodedata module for Hangul
            try: 
                return unicodedata.name(unichr(ord_)).lower()
            except: 
                return None
        
        # Add UnicodeData Name
        return SentenceData.raw_data(self, ord_)

    def _format_data(self, ord_, data):
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
