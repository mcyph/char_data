from .DataSourceBase import DataSourceBase
from char_data.data_processors.get_key_name import get_key_name

#=========================================================#
#                 Get Class by Property                   #
#=========================================================#


class DataBase:
    def __init__(self, o):
        """
        This is fed the data from get_D_indexes and get_D_data
        in DataReader, to allow finding properties of characters
        """
        self.o = o
        self.SPossible = set(i[0] for i in self.o.LData)
        self.DCache = {}

    def get_class_by_property(self, s):
        if isinstance(s, list):
            s = tuple(s)
        
        if not s in self.DCache:
            self.DCache[s] = self._get_class_by_property(s)
        return self.DCache[s]

    def _get_class_by_property(self, s):
        """
        Returns the class instance of the formatter
        
        Format: [data source].[property key]
        Example: "unihan.rsjapanese"
        
        NOTE: property keys are case insensitive
        """
        if isinstance(s, (list, tuple)):
            # Convert (data source, key) 
            # tuples/lists to "[data source].[key]"
            s = '%s.%s' % s
        s = s.lower()
        
        if '.' in s:
            # e.g. Unihan.RSJapanese etc
            # NOTE: "unicode 1.0 name" needs to be 
            # referenced as "unicodedata.unicode 1.0 name"
            
            data_source, _, key = s.partition('.')
            key = get_key_name(key)
            if not data_source in self.SPossible:
                raise KeyError("invalid data source: %s" % data_source)

            o = getattr(getattr(self.o, data_source), key)
            assert isinstance(o, DataSourceBase)
            return o
        else:
            # e.g. 'Name' (try in all of the sources)
            for data_source in (
                'unicodedata',
                'unihan',
                'ccdict',
                'kanjidic',
                'others',
                'hanzi_variants'
            ):
                key = get_key_name(s)

                if data_source in self.SPossible:
                    o = getattr(self.o, data_source)
                    if hasattr(o, key) and isinstance(getattr(o, key), DataSourceBase):
                        return getattr(getattr(self.o, data_source), key)
                else:
                    raise KeyError("invalid data source: %s" % data_source)
        
        raise KeyError("invalid character property name: %s" % s)
