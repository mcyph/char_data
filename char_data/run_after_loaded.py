LFns = []

def register(fn):
    LFns.append(fn)


def run_all():
    for fn in LFns:
        fn()
