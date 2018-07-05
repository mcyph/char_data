from json import dumps

from toolkit.file_tools import file_write
from toolkit.py_ini import read_D_pyini
from char_data.data_paths import data_path
from char_data.indexes import DIndexWriters
from char_data import formatters

def add(old_fn):
    def new_fn(self, *args, **kw):
        # use iterator `old_fn` and add character information
        for key, ord_, value in old_fn(self, *args, **kw):
            D = self.DKeys[key]
            
            if False: 
                assert not ord_ in D, "ordinal %s key %s already exists" % (ord_, key)
            
            D[ord_] = value
    return new_fn

class WriteBase:
    def __init__(self, path):
        self.DKeys = {}
        self.DCls = {}
        self.read_data(data_path('chardata', path))
    
    def read_data(self, path):
        D = read_D_pyini(path)
        
        for key, DItem in D.items():
            print key, DItem
            self.DKeys[key] = {}
            
            if 'index' in DItem and DItem['index'] not in (None, 'FIXME'): # HACK!
                indexer = DIndexWriters[DItem['index']]
            else:
                indexer = None
            
            self.DCls[key] = (getattr(formatters, DItem['formatter']),
                              indexer,
                              DItem)
    
    def write(self, path):
        """
        Write the values to a binary file and the JSON data 
        which specifies the seek position, amount, array type 
        (e.g. short/integer etc) and architecture (byte order/
        wide+narrow Unicode build to disk)
        """
        DJSON = {}
        DIdxJSON = {}
        
        f_data = open('%s.bin' % path, 'wb')
        f_idx = open('%s-idx.bin' % path, 'wb')
        
        for key, DOrds in self.DKeys.items():
            formatter_class, index_fn, DItem = self.DCls[key]
            print 'writing:', key, formatter_class#, DOrds
            
            fn = formatter_class.writer
            DJSON[key] = fn(f_data, key, DOrds)
            
            if index_fn:
                DData = self.DKeys[key]
                DIdxJSON[key] = index_fn(f_idx, key, DData, DItem)
        
        file_write('%s.json' % path, dumps(DJSON, indent=4))
        file_write('%s-idx.json' % path, dumps(DIdxJSON, indent=4))

if __name__ == '__main__':
    from char_data.importer import Unihan, Kanjidic, CCDict, Unicode
    CCDict.run()
    Kanjidic.run()
    #MultiRads.run()
    Unicode.run()
    Unihan.run()
