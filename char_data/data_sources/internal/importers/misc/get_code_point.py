def get_code_point(Hex):
    if '..' in Hex:
        # Two hex values - return an int range
        FromHex, ToHex = Hex.split('..')
        return int(FromHex, 16), int(ToHex, 16)
    else:
        # Return a single int
        try:
            return int(Hex, 16)
        except:
            print("ERROR:", Hex)
            raise

