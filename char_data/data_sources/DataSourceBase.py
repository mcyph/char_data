from char_data.data_sources.internal.property_formatters.enum.DEnum import DEnum


class DataSourceBase:
    def __init__(self, parent, header_const, original_name, short_desc,
                 long_desc=None, LISOs=None, index=None):
        """
        The base class for both internal and external data sources.
        """

        self.parent = parent
        self.header_const = header_const
        self.original_name = original_name

        from char_data.data_sources.get_key_name import get_key_name

        self.key = get_key_name(original_name)
        self.short_desc = short_desc
        self.long_desc = long_desc
        self.LISOs = LISOs or []
        self.index = index

    def raw_data(self, ord_):
        raise NotImplementedError

    def formatted(self, ord_):
        data = self.raw_data(ord_)
        return self._format_data(ord_, data)

    def _format_data(self, ord_, data):
        raise NotImplementedError

    def html_formatted(self, ord_):
        value = self.formatted(ord_)
        return self._process_property_value(value)

    def _process_property_value(self, value):
        """
        Get a pretty-printed HTML output version of the value
        """
        from types import BooleanType

        if not isinstance(value, (list, tuple)):
            # TODO: add specific handling for Booleans??
            if self.key in DEnum:
                value = DEnum[self.key].get(
                    unicode(value), value
                ).replace('_', ' ')

            return E(unicode(value).strip()).replace('\n', '<br>')

        else:
            if len(value) > 1:
                return '<ul>%s</ul>' % ''.join([
                    '<li>%s</li>' % self._process_property_value(i) for i in value
                ])
            else:
                return self._process_property_value(value[0])

