
class CharIndexValueInfo:
    def __init__(self, value, display_value, description=None):
        """
        value -> the internal value, with no spaces, and normalised etc
        display_name -> the value for display in the web interface etc to the user
        description -> information about this value (optional)
        """
        self.value = value
        self.display_value = display_value
        self.description = description

    @staticmethod
    def from_tuple(value, display_value, description):
        return CharIndexValueInfo(
            value, display_value, description
        )

    def to_tuple(self):
        return (
            self.value,
            self.display_value,
            self.description
        )

    def __str__(self):
        return "CharIndexValueInfo(value=%s, display_value=%s, description=%s)" % (
            self.value, self.display_value, self.description
        )
