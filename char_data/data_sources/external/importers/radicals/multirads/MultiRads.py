from toolkit.encodings.surrogates import w_ord
from char_data.importer.Write import WriteBase, add
from .RadKFile import rad_k_file


class MultiRads(WriteBase):
    def __init__(self):
        WriteBase.__init__(self, 'Chars/Data/MultiRads/MultiRads.pyini')
        self.open_radkfile()
        
    @add
    def open_radkfile(self):
        DRads = rad_k_file.DRads  # ???? What about indexing????
        DKanji = rad_k_file.DKanji
        
        for kanji, LRads in list(DKanji.items()):
            yield 'multi_radicals', w_ord(kanji), [w_ord(i) for i in LRads]


def run():
    MultiRads().write('Chars/Data/MultiRads/MultiRads')


if __name__ == '__main__':
    run()
