#from Chars.TranslitMap import get_translit_map

from char_data.data_sources.external.property_formatters import ExternalBaseClass
from char_data.data_sources.consts import HEADER_LANGUAGE_USAGE


class Transliteration(ExternalBaseClass):
    def __init__(self, parent, from_script, to_script):
        ExternalBaseClass.__init__(
            self, parent, HEADER_LANGUAGE_USAGE, original_name=typ,
            short_desc=DDesc[typ], LISOs=FIXME
        )

