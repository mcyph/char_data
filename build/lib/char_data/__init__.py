def dep_fn(s):
    """
    HACK: Make sure the char modules which depend
    on the char modules don't end with recursive
    import problems
    """
    def fn(*args, **kwargs):
        print s, args, kwargs
        return eval(s)(*args, **kwargs)
    return fn

keys = dep_fn('keys')
raw_data = dep_fn('raw_data')
formatted = dep_fn('formatted')

idx_search = dep_fn('idx_search')
idx_keys = dep_fn('idx_keys')
idx_values = dep_fn('idx_values')

from ClassByProperty import ClassByProperty
from CharInfo import * # HACK!
