from char_data.datatypes.read import StringData

class IRG(StringData): # ??? ==========================================================
    def __init__(self, key, f, DJSON):
        StringData.__init__(self, key, f, DJSON)
    
    def formatted(self, ord_):
        # TODO: Provide specific info on the IRG fields, provide info 
        # whether the character is encoded in that geographic region 
        # and the rough frequency based on the encoding points
        # TODO: Should Hong Kong have a special formatter?
        data = self.raw_data(ord_)
        
        if not data: 
            return None
        return data
