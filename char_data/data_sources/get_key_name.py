
def get_key_name(s):
    """
    Get the property key name for use as class variables etc
    (for program-level access)
    """
    for c in '.,-/ ':
        s = s.replace(c, '_')
    return s.lower()
