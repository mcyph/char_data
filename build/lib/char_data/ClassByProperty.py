#=========================================================#
#                 Get Class by Property                   #
#=========================================================#


class ClassByProperty:
    def __init__(self, D):
        self.D = D
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
            return self.D[data_source][key]
        else:
            # e.g. 'Name' (try in all of the sources)
            for data_source in (
                'unicodedata',
                'unihan',
                'ccdict',
                'kanjidic',
                'others',
                'hanzi variants'
            ):
                key = s
                if data_source in self.D and key in self.D[data_source]:
                    return self.D[data_source][key]
        
        raise KeyError("invalid character property name: %s" % s)

