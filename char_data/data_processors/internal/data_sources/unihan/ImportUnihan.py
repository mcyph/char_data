import glob

from char_data.data_paths import data_path

from char_data.data_processors.internal.data_sources.unihan.open_unihan import open_unihan
from char_data.data_processors.internal.data_sources.WriteBase import WriteBase, add


class ImportUnihan(WriteBase):
    def __init__(self):
        from char_data.data_processors.internal.data_sources.unihan.Unihan import Unihan
        WriteBase.__init__(self, Unihan())
        self.open_unihan()
    
    @add
    def open_unihan(self):
        #=======================================================#
        #                      Unihan Data                      #
        #=======================================================#
        
        path = data_path('chardata', 'unihan/source/*.txt')
        LUni = glob.glob(path)
        assert LUni, path
        
        for D in open_unihan(LUni):
            # Get the codepoint, deleting the 'Word' key
            ord_ = D['codepoint']
            
            self.IICore(ord_, D)
            self.HDZRadBreak(ord_, D)
            self.Fenn(ord_, D)
            self.CheungBauer(ord_, D)
            
            for key, value in list(D.items()):
                if key == 'codepoint':
                    continue
                
                yield key, ord_, value
    
    def IICore(self, ord_, D):
        if 'IICore' in D:
            # HACK: Remap IICore to be a True/False value with alias info that
            # e.g. says "Yes, Commonly Used in East Asia" or possibly shorter
            # as "IICore" (Integrated Ideographs? Core) isn't very descriptive
            D['IICore'] = True
        else: 
            D['IICore'] = False
    
    def HDZRadBreak(self, ord_, D):
        if 'HDZRadBreak' in D:
            if True: 
                # HDZRadBreak has a radical and phonetic indice, both of which seem 
                # to be more useful deleted rather than keeping them
                del D['HDZRadBreak']
            else:
                # TODO: Split into Radical; Indices, possibly ignoring the radical
                pass
    
    def Fenn(self, ord_, D):
        if 'Fenn' in D:
            if True:
                # Fenn may be useful, so I may enable Fenn later if I have time
                del D['Fenn']
            else:
                # Split into Phonetic Indices; Grades/Frequencies
                Phonetic = D['Fenn'][0]
                Frequency = D['Fenn'][1]
                D['Fenn Phonetic'] = Phonetic
                D['Fenn Frequency'] = Frequency
                del D['Fenn']
    
    def CheungBauer(self, ord_, D):
        if 'CheungBauer' in D:
            if True:
                # As all three of the values are already in other 
                # properties, it's probably better to delete this property
                del D['CheungBauer']
            else:
                # Split into Radical/Additional Strokes; Cangjie; Readings
                RS, cangjie, jyutping = D['CheungBauer'].split(';')
                
                RS = RS.strip()
                cangjie = cangjie.strip()
                jyutping = jyutping.strip()
                
                D['CheungBauer RS'] = RS
                D['CheungBauer Cangjie'] = cangjie
                D['CheungBauer Jyutping'] = jyutping


def run():
    ImportUnihan().write(data_path('chardata', 'unihan/output/unihan'))


if __name__ == '__main__':
    run()
