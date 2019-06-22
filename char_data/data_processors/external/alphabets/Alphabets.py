from char_data.data_processors.external.alphabets.AlphabetFormatter import AlphabetFormatter
from char_data.data_processors.external.ExternalSourceBase import ExternalBase


class Alphabets(ExternalBase):
    """
    TODO: Use the data from Unicode CLDR!!
    """
    def __init__(self):
        ExternalBase.__init__(self, 'cldr_alphabets')
        self.alphabets = AlphabetFormatter(self)
