from char_data.data_processors.consts import DHeaders


class CharDataKeyInfo:
    def __init__(self, key, original_key, short_desc,
                 header_const, source, char_index_key_info=None):
        self.key = key
        self.original_key = original_key
        self.short_desc = short_desc
        self.header_const = header_const
        self.source = source
        self.char_index_key_info = char_index_key_info

    @staticmethod
    def from_tuple(t):
        return CharDataKeyInfo(*t)

    def to_tuple(self):
        return (
            self.key,
            self.original_key,
            self.short_desc,
            self.header_const,
            self.source,
            (
                self.char_index_key_info.to_tuple()
                if self.char_index_key_info
                else None
            )
        )

    def __str__(self):
        return "CharDataKeyInfo(key=%s, original_key=%s, header_const=%s, char_index_key_info=%s)" % (
            self.key, self.original_key,
            DHeaders[self.header_const],
            str(self.char_index_key_info)
        )
