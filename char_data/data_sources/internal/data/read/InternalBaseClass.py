from char_data.DataSourceBase import DataSourceBase


class NO_DATA: pass


class InternalBaseClass(DataSourceBase):
    def __init__(self, parent, header_const, original_name, short_desc,
                 long_desc=None, LISOs=None, index_type=None):
        """
        The base class for internal datatype readers
        (e.g. Boolean/IntegerList etc)

        raw_data needs to be implemented in subclasses of this base class,
        returning unformatted (raw) data

        format_data needs to be implemented by subclasses in property_formatter
        (which are derived from subclasses of this base class)
        """
        self.data_loaded = False
        self.index_type = index_type if index_type != 'FIXME' else None  # HACK HACK HACK!!!!!

        DataSourceBase.__init__(
            self, parent=parent, header_const=header_const,
            original_name=original_name, short_desc=short_desc,
            long_desc=long_desc, LISOs=LISOs, index=self.index_type
        )

        self._ensure_data_loaded()

    def _ensure_data_loaded(self):
        from char_data.data_sources.internal.indexes import DIndexReaders

        try:
            # Load the base data
            D = self.parent.DBaseJSON[self.key]
            self._load_data(self.key, self.parent.f_base_data, D)
        except:
            from traceback import print_exc
            print_exc()

        # Load the index data
        if self.index:
            try:
                D = self.parent.DIndexJSON[self.key]
                self.index = (
                    DIndexReaders[self.index](self.parent.f_index_data, D)
                )
            except:
                #from traceback import print_exc
                print(("ERROR LOADING INDEX: %s with index type %s" % (self.key, self.index_type)))
                #print_exc()
                self.index = None

    def _load_data(self, key, f, DJSON):
        # Needs to be implemented in subclasses of this base class,
        # instantiating any data arrays
        raise NotImplementedError

    def get_range_data(self, ord_):
        for from_, to, value in self.LRanges:
            if from_ > ord_:
                # Stop searching if no greater values
                break
            
            elif ord_ >= from_ and ord_ <= to:
                return value
        
        return NO_DATA
