class String:
    def __init__(self, char_data, s):
        self.char_data = char_data
        self.s = s

    def contains(self, c):
        return c == self.s

    def __iter__(self):
        yield self.s
