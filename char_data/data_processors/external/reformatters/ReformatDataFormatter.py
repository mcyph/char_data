from char_data.abstract_base_classes.formatters.ExternalFormatterBase import ExternalFormatterBase

from .ReformatIndex import ReformatIndex


class ReformatDataFormatter(ExternalFormatterBase):
    def __init__(self, parent, header_const, original_name, short_desc, get_L_data,
                 alternative_mapping_key=None):
        """
        This is just a placeholder, as getting raw value information for derived
        info by codepoints doesn't make much sense (that I can see)

        See also ReformatIndex.py for what this is here for.
        """
        self.get_L_data = get_L_data

        ExternalFormatterBase.__init__(self,
                                       parent, header_const, original_name, short_desc
                                       )
        self.index = ReformatIndex(
            original_name, get_L_data,
            alternative_mapping_key=alternative_mapping_key
        )

    def raw_data(self, ord_):
        # As based on other data (like the "Common" characters script)
        # we'll just return `None` here
        return None

    def _format_data(self, ord_, data):
        if data is not None:
            return data  # HACK!
        return None
