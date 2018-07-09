from char_data.storage.data.read import IntegerList


class NoFormatIntegers(IntegerList):
    def _format_data(self, ord_, data):
        return data
