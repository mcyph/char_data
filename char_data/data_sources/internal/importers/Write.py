import warnings
from json import dumps

from toolkit.io.file_tools import file_write

from char_data.data_paths import data_path
from char_data.data_sources.internal.indexes import DIndexWriters
from char_data.DataSourceBase import DataSourceBase
from char_data.data_sources.get_key_name import get_key_name


def add(old_fn):
    def new_fn(self, *args, **kw):
        # use iterator `old_fn` and add character information
        for key, ord_, value in old_fn(self, *args, **kw):
            #print(self.DKeys)
            D = self.DKeys[get_key_name(key)]  # PERFORMANCE WARNING!!! =============================================

            if ord_ in D:
                warnings.warn(
                    "ordinal %s key %s already exists" % (ord_, key)
                )
            D[ord_] = value
    return new_fn


class WriteBase:
    def __init__(self, internal_data_source):
        self.DKeys = {}
        self.DCls = {}
        self.read_data(internal_data_source)
    
    def read_data(self, internal_data_source):
        for key in dir(internal_data_source):
            inst = getattr(internal_data_source, key)
            print(inst)
            if not isinstance(inst, DataSourceBase):
                continue

            print((key, inst))
            self.DKeys[key] = {}
            
            if inst.index_type and inst.index_type not in (None, 'FIXME'): # HACK!
                indexer = DIndexWriters[inst.index_type]
            else:
                indexer = None
            
            self.DCls[key] = (inst, indexer)
    
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
        
        for key, DOrds in list(self.DKeys.items()):
            formatter_class, index_fn = self.DCls[key]
            print(('writing:', key, formatter_class))#, DOrds
            
            fn = formatter_class.writer
            DJSON[key] = fn(f_data, key, DOrds)
            
            if index_fn:
                DData = self.DKeys[key]
                # NOTE: DItem (i.e. the dict from the .pyini file) was passed here, but
                DIdxJSON[key] = index_fn(f_idx, key, DData)
        
        file_write('%s.json' % path, dumps(DJSON, indent=4))
        file_write('%s-idx.json' % path, dumps(DIdxJSON, indent=4))


if __name__ == '__main__':
    from char_data.data_sources.internal.importers import Unihan, Kanjidic, CCDict, Unicode
    CCDict.run()
    Kanjidic.run()
    #MultiRads.run()
    Unicode.run()
    Unihan.run()
