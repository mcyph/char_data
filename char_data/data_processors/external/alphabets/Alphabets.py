from char_data.data_processors.external.alphabets.AlphabetFormatter import AlphabetFormatter
from char_data.data_processors.external.ExternalSourceBase import ExternalSourceBase


class Alphabets(ExternalSourceBase):
    """
    TODO: Use the data from Unicode CLDR!!
    """
    def __init__(self):
        ExternalSourceBase.__init__(self, 'cldr_alphabets')
        self.alphabets = AlphabetFormatter(self)
