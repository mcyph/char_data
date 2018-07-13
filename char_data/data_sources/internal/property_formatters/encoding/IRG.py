from char_data.data_sources.internal.data.read import StringData


class IRG(StringData): # ??? ==========================================================
    def _format_data(self, ord_, data):
        # TODO: Provide specific info on the IRG fields, provide info 
        # whether the character is encoded in that geographic region 
        # and the rough frequency based on the encoding points
        # TODO: Should Hong Kong have a special formatter?
        if not data: 
            return None
        return data
