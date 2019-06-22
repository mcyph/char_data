from char_data.data_processors.consts import HEADER_UNICODE_GENERAL  # HACK!!!!
from char_data.data_processors.external.property_formatters.alphabets.AlphabetData import AlphabetData
from .ExternalBase import ExternalBase


class Alphabets(ExternalBase):
    """
    TODO: Use the data from Unicode CLDR!!
    """
    def __init__(self):
        ExternalBase.__init__(self, 'cldr_alphabets')
        self.alphabets = AlphabetData(self)
