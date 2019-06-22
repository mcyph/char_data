from lang_data import LangData, get_L_possible_isos
from char_data.data_processors.external.property_formatters import ExternalBaseClass
from char_data.data_processors.consts import HEADER_LANGUAGE_USAGE  # HACK!!!!
from .AlphabetIndex import AlphabetIndex


# TODO: Write me!
class AlphabetData(ExternalBaseClass):
    def __init__(self, parent):
        self.ld = LangData('en')  # DEFAULT TO ENGLISH HACK!!!
        index = AlphabetIndex(self.ld, 'alphabets')

        ExternalBaseClass.__init__(
            self, parent, HEADER_LANGUAGE_USAGE, original_name='alphabets',
            short_desc='Alphabets', index=index, #LISOs=FIXME
        )
    
    def raw_data(self, ord_):
        return None  # TODO: Allow getting which languages a character is used in!!
    
    def _format_data(self, ord_, data):
        if data:
            return self.ld.prettify_lang(data)
        return None
