from char_data.data_sources.internal.data.read import IntegerList


class NoFormatIntegers(IntegerList):
    def _format_data(self, ord_, data):
        return data
