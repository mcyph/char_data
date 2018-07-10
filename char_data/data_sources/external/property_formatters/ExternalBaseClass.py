class ExternalBaseClass:
    def __init__(self, parent, header_const, original_name, short_desc,
                 long_desc=None, LISOs=None, index=None):
        """
        A class similar to BaseClass in storage/data/read/BaseClass.py,
        but used for data held in external databases/retrieved or
        generated programmatically etc

        All subclasses need:

        * raw_data(ordinal)
        * _format_data(ordinal, data)

        methods implemented.
        """

        self.parent = parent
        self.header_const = header_const
        self.original_name = original_name

        from char_data.data_sources.get_key_name import get_key_name

        self.key = get_key_name(original_name)
        self.short_desc = short_desc
        self.long_desc = long_desc
        self.LISOs = LISOs or []

        # NOTE: Indexes need to be actual "faux" index instances,
        #       with `keys()` and `search(s)` methods
        self.index = index

    def raw_data(self, ord_):
        raise NotImplementedError

    def formatted(self, ord_):
        data = self.raw_data(ord_)
        return self._format_data(ord_, data)

    def _format_data(self, ord_, data):
        raise NotImplementedError
