from char_data.storage.indexes import DIndexReaders
from char_data.storage.get_key_name import get_key_name

class NO_DATA: pass


class BaseClass:
    def __init__(self, parent, header_const, original_name, short_desc,
                 long_desc=None, LISOs=None, index=None):
        self.data_loaded = False

        self.parent = parent
        self.header_const = header_const
        self.original_name = original_name
        self.key = get_key_name(original_name)
        self.short_desc = short_desc
        self.long_desc = long_desc
        self.LISOs = LISOs or []
        self.index = index if index != 'FIXME' else None  # HACK HACK HACK!!!!!

        try:
            self._ensure_data_loaded()
        except:
            from traceback import print_exc
            print_exc()

    def _ensure_data_loaded(self):
        # Load the base data
        D = self.parent.DBaseJSON[self.key]
        self._load_data(self.key, self.parent.f_base_data, D)

        # Load the index data
        if self.index:
            D = self.parent.DIndexJSON[self.key]
            self.index = (
                DIndexReaders[self.index](self.parent.f_index_data, D)
            )

    def _load_data(self, key, f, DJSON):
        # Needs to be implemented in subclasses of this base class,
        # instantiating any data arrays
        raise NotImplementedError

    def raw_data(self, ord_):
        # Needs to be implemented in subclasses of this base class,
        # returning unformatted (raw) data
        raise NotImplementedError

    def formatted(self, ord_):
        data = self.raw_data(ord_)
        return self._format_data(ord_, data)

    def _format_data(self, ord_, data):
        # Needs to be implemented by subclasses in property_formatter
        # (which are derived from subclasses of this base class)
        raise NotImplementedError

    def get_range_data(self, ord_):
        for from_, to, value in self.LRanges:
            if from_ > ord_:
                # Stop searching if no greater values
                break
            
            elif ord_ >= from_ and ord_ <= to:
                return value
        
        return NO_DATA
