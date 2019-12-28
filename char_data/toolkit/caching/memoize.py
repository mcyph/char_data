from marshal import dumps
cache = {}


def memoize(f):
    """
    Memoize any function.
    """
    def decorated(*args):
        key = (f, dumps(args))
        if key in cache:
            return cache[key]

        cache[key] = f(*args)
        return cache[key]

    return decorated


def memoize_cls_method(f):
    """
    Memoize any class function.
    """
    def decorated(self, *args):
        key = (f, dumps(args))
        if key in cache:
            return cache[key]

        cache[key] = f(self, *args)
        return cache[key]

    return decorated
