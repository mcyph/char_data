from abc import ABC, abstractmethod
from char_data.toolkit.html_tools.escape import E


class PropertyFormatterBase(ABC):
    def __init__(self,
                 parent,
                 header_const,
                 original_name: str,
                 short_desc: str,
                 long_desc=None,
                 LISOs=None,
                 index=None):
        """
        The base class for both internal and external data sources.
        (data_sources/internal/data/read/InternalBaseClass and
         data_sources/external/property_formatters/ExternalBaseClass)

        This really should be in data_sources/, but for now it's here
        to prevent recursive import issues
        """

        self.parent = parent
        self.header_const = header_const
        self.original_name = original_name

        from char_data.data_processors.get_key_name import get_key_name

        self.key = get_key_name(original_name)
        self.short_desc = short_desc
        self.long_desc = long_desc
        self.LISOs = LISOs or []
        self.index = index

    @abstractmethod
    def raw_data(self, ord_):
        pass

    def formatted(self, ord_):
        data = self.raw_data(ord_)
        return self._format_data(ord_, data)

    @abstractmethod
    def _format_data(self, ord_, data):
        pass

    def html_formatted(self, ord_):
        value = self.formatted(ord_)
        if value is None:
            return None
        else:
            return self._process_property_value(value)

    def _process_property_value(self, value):
        """
        Get a pretty-printed HTML output version of the value
        """
        from char_data.data_processors.internal.property_formatters.enum.DEnum import DEnum

        if not isinstance(value, (list, tuple)):
            # TODO: add specific handling for Booleans??
            #print("VALUE:", value)

            if self.key in DEnum:
                value = DEnum[self.key].get(
                    str(value), value
                ).replace('_', ' ')

            #else:
            #    print(repr(value))

            return E(str(value).strip()).replace('\n', '<br>')

        else:
            if len(value) > 1:
                return '<ul>%s</ul>' % ''.join([
                    '<li>%s</li>' % self._process_property_value(i) for i in value
                ])
            else:
                return self._process_property_value(value[0])
