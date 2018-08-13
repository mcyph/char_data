
def get_key_name(s):
    """
    Get the property key name for use as class variables etc
    (for program-level access)
    """
    for c in '.,-/ ':
        s = s.replace(c, '_')

    while '__' in s:
        s = s.replace('__', '_')
    return s.lower()
