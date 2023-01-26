from iso_tools.cldr.CLDR import CLDR
from char_data.abstract_base_classes.formatters.ExternalFormatterBase import ExternalFormatterBase
from char_data.data_processors.consts import HEADER_LANGUAGE_USAGE  # HACK!!!!
from .AlphabetIndex import AlphabetIndex


# TODO: Write me!
class AlphabetFormatter(ExternalFormatterBase):
    def __init__(self, parent):
        self.lang_data = CLDR('en')  # DEFAULT TO ENGLISH HACK!!!
        index = AlphabetIndex(self.lang_data, 'alphabets')

        ExternalFormatterBase.__init__(
            self, parent, HEADER_LANGUAGE_USAGE, original_name='alphabets',
            short_desc='Alphabets', index=index, #LISOs=FIXME
        )
    
    def raw_data(self, ord_):
        return None  # TODO: Allow getting which languages a character is used in!!
    
    def _format_data(self, ord_, data):
        if data:
            return self.lang_data.prettify_lang(data)
        return None
