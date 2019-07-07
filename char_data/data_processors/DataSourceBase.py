from json import loads
from toolkit.escape import E
from toolkit.encodings.hex_padding import get_uni_point


class DataSourceBase:
    def __init__(self, parent, header_const, original_name, short_desc,
                 long_desc=None, LISOs=None, index=None):
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

    def raw_data(self, ord_):
        raise NotImplementedError

    def formatted(self, ord_):
        data = self.raw_data(ord_)
        return self._format_data(ord_, data)

    def _format_data(self, ord_, data):
        raise NotImplementedError

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

            elif isinstance(value, str) and value.startswith('[') and value.endswith(']'):

                # HACK: The fact this is a JSON-parsable value means
                # this should be handled in the formatters at a higher
                # level - this logic should be moved (when I have time!) =================================================================
                value = loads(value)

                LOut = []

                def add_list_item(s):
                    if len(value) == 1:
                        LOut.append(s)
                    else:
                        LOut.append(f'<li>{ s }</li>')

                for i_tuple in value:
                    assert isinstance(i_tuple, (list, tuple))

                    if len(i_tuple) == 2:
                        # See also, e.g. [96, "grave accent"]
                        # for combining grave accents
                        add_list_item(
                            f'{ get_uni_point(i_tuple[0]) } '
                            f'&#{ int(i_tuple[0]) }; '
                            f'{ E(i_tuple[1]) }'
                        )

                    elif len(i_tuple) == 3:
                        if isinstance(i_tuple[0], (list, tuple)):
                            # e.g. [[[65, 769], null, null]] as in combining char decompositions
                            codepoints = ''
                            uni_chars = ''

                            for codepoint in i_tuple[0]:
                                codepoints += f"{ get_uni_point(codepoint) } "
                                uni_chars += f"&#{ int(codepoint) };"

                            add_list_item(
                                f'{ codepoints.strip() } { uni_chars } ' 
                                f'{ E(str(i_tuple[1])) if i_tuple[1] else "" } ' 
                                f'{ E(str(i_tuple[2])) if i_tuple[2] else "" }'
                            )
                        else:
                            # ???
                            add_list_item(
                                f'{ get_uni_point(i_tuple[0]) } '
                                f'&#{ int(i_tuple[0]) }; '
                                f'{ E(str(i_tuple[1:])) }'
                            )

                if LOut:
                    return '<ul>' + "\n".join(LOut) + '</ul>'
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
