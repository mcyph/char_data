from char_data.data_paths import data_path

from char_data.data_processors.internal.data_sources.kanjidic.Kanjidic2 import open_kanjidic_2
from char_data.data_processors.internal.data_sources.WriteBase import WriteBase, add


class ImportKanjidic(WriteBase):
    def __init__(self):
        from char_data.data_processors.internal.data_sources.kanjidic.Kanjidic import Kanjidic
        WriteBase.__init__(self, Kanjidic())
        self.open_kanjidic(data_path('chardata', 'kanjidic/source/kanjidic2.xml'))
        
    @add
    def open_kanjidic(self, path):
        for D in open_kanjidic_2(path):
            ord_ = D['codepoint']
            
            for key, value in list(D.items()):
                if key == 'codepoint':
                    continue
                
                yield key, ord_, value


def run():
    ImportKanjidic().write(data_path('chardata', 'kanjidic/output/kanjidic'))


if __name__ == '__main__':
    run()
