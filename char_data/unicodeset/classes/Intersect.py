class Intersect:
    def __init__(self, o1, o2):
        self.o1 = o1
        self.o2 = o2

    def contains(self, c):
        return (
            c in self.o1 and
            c in self.o2
        )

    def __iter__(self):
        for c in self.o1:
            if c in self.o2:
                yield c
