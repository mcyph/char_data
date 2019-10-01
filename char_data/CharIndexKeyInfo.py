

class CharIndexKeyInfo:
    def __init__(self, key, display_key, key_type):
        self.key = key
        self.display_key = display_key
        self.key_type = key_type

    @staticmethod
    def from_tuple(key, display_key, key_type):
        return CharIndexKeyInfo(
            key, display_key, key_type
        )

    def to_tuple(self):
        return (
            self.key,
            self.display_key,
            self.key_type
        )

    def __str__(self):
        return "CharIndexKeyInfo(key=%s, display_key=%s, key_type=%s)" % (
            self.key, self.display_key, self.key_type
        )
