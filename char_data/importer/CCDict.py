from char_data.data_paths import data_path

from char_data.importer.parsers.Unihan import open_unihan
from char_data.importer.Write import WriteBase, add


class ImportCCDict(WriteBase):
    def __init__(self):
        WriteBase.__init__(self, 'ccdict/ccdict.pyini')
        self.open_ccdict()
    
    @add
    def open_ccdict(self):
        #=======================================================#
        #                      CCDict Data                      #
        #=======================================================#
        
        for D in open_unihan([data_path('chardata', 'ccdict/src/ccdict.txt')]):
            ord_ = D['codepoint']
            
            for key, value in D.items():
                if key == 'codepoint':
                    continue
                elif key.startswith('f'):
                    key = key[1:]
                
                #print key, ord_, value
                yield key, ord_, value


def run():
    ImportCCDict().write(data_path('chardata', 'ccdict/ccdict'))


if __name__ == '__main__':
    run()
