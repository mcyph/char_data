from char_data.data_sources.external.property_formatters import ExternalBaseClass

from ReformatIndex import ReformatIndex


class ReformatData(ExternalBaseClass):
    def __init__(self, parent, header_const, original_name, short_desc, get_L_data):
        self.get_L_data = get_L_data

        ExternalBaseClass.__init__(self,
            parent, header_const, original_name, short_desc
        )
        self.index = ReformatIndex(original_name, get_L_data)

    def raw_data(self, ord_):
        # As based on other data (like the "Common" characters script)
        # we'll just return `None` here
        return None

    def _format_data(self, ord_, data):
        if data is not None:
            return data.partition('.')[-1]  # HACK!
        return None