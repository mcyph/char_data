from char_data.DataSourceBase import DataSourceBase


class ExternalBaseClass(DataSourceBase):
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

        NOTE: Indexes need to be actual "faux" index instances,
              with `keys()` and `search(s)` methods
        """

        DataSourceBase.__init__(
            self, parent=parent, header_const=header_const,
            original_name=original_name, short_desc=short_desc,
            long_desc=long_desc, LISOs=LISOs, index=index
        )
