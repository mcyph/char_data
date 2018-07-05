from toolkit.encodings.surrogates import w_ord
from char_data.importer.Write import WriteBase, add
from char_data.importer.parsers.multirads.RadKFile import get_D_rads, get_D_kanji, combine_radkfile_2

class MultiRads(WriteBase):
    def __init__(self):
        WriteBase.__init__(self, 'Chars/Data/MultiRads/MultiRads.pyini')
        self.open_radkfile()
        
    @add
    def open_radkfile(self):
        DRads = combine_radkfile_2(get_D_rads('Chars/Data/MultiRads/radkfile'),
                                   get_D_rads('Chars/Data/MultiRads/radkfile2'))
        DKanji = get_D_kanji(DRads)
        
        for kanji, LRads in DKanji.items():
            yield 'Multi Radicals', w_ord(kanji), [w_ord(i) for i in LRads]

def run():
    MultiRads().write('Chars/Data/MultiRads/MultiRads')

if __name__ == '__main__':
    run()
