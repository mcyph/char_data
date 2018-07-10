
from char_data.data_sources.external.property_formatters import ExternalBaseClass

#from Data.Languages.Langs import DLangs


# TODO: Write me!
class Alphabets(ExternalBaseClass):
    def __init__(self, parent):
        ExternalBaseClass.__init__(
            self, parent, HEADER_FIXME, original_name='',
            short_desc='Alphabets', LISOs=FIXME
        )
    
    def get_data(self, ord_):
        pass
    
    def formatted(self, ord_):
        pass
