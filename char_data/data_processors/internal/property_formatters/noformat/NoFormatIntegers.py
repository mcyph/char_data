from char_data.data_processors.internal.data_types.read import IntegerList


class NoFormatIntegers(IntegerList):
    def _format_data(self, ord_, data):
        return data
