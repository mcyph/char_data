#from Chars.TranslitMap import get_translit_map

from char_data.data_processors.external.property_formatters import ExternalFormatterBase
from char_data.data_processors.consts import HEADER_LANGUAGE_USAGE


class TranslitFormatter(ExternalFormatterBase):
    def __init__(self, parent, from_script, to_script):
        ExternalFormatterBase.__init__(
            self, parent, HEADER_LANGUAGE_USAGE, original_name=typ,
            short_desc=DDesc[typ], LISOs=FIXME
        )

