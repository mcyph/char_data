class String:
    def __init__(self, char_indexes, s):
        self.char_indexes = char_indexes
        self.s = s

    def contains(self, c):
        return c == self.s

    def __iter__(self):
        yield self.s
