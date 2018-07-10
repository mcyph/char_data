from char_data.data_sources.external.property_formatters import ExternalBaseClass
from char_data.data_sources.consts import HEADER_READINGS


class ReadingsCombine(ExternalBaseClass):
    def __init__(self, parent, LKeys):
        ExternalBaseClass.__init__(
            self, parent, HEADER_READINGS, original_name='similar_hanzi',
            short_desc='Similar Hanzi', LISOs=FIXME
        )
    
    def raw_data(self, ord_):
        """
        TODO: Combine readings from multiple sources,
        e.g. for Mandarin, get from Unihan, Kanjidic and CCDict,
        sorting by the frequencies (if they exist as in Hanlu Pinlu) 
        position and number of times the readings occur between sources
        """
        pass
    
    def formatted(self, ord_):
        pass
