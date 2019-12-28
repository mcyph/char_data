import sys, os
import md5
import time
#from JSON import dumps, loads, load, dump
from pickle import dump, load, loads
#from marshal import dump, load, loads
#for k in sys.modules:
#    print k

USE_CACHE = True
if not USE_CACHE:
    import warnings
    warnings.warn("TURN ON CACHE IN cache_funct!")


def get_hash_key(s):
    s = md5.new(str(s).encode('utf-8', 'replace')).hexdigest()
    return s


DHASH = {}


def cache_funct(id, Funct):
    if not USE_CACHE: return Funct
    
    # cache a function to pickle to save loading time
    def cache(*args, **kwargs):
        hash = get_hash_key((args, kwargs))
        if (id, hash) in DHASH: 
            return DHASH[(id, hash)]
        
        path = 'cache/%s_%s.cache' % (id, hash)
        if os.path.exists(path): # and os.path.getsize(path):
            print(('Opening %s -' % id), end=' ')
            t_from = time.time()
            f = open(path, 'rb')
            rtn = load(f)
            f.close()
            print('%ssec OK' % (time.time()-t_from))
        else:
            f = open(path, 'wb')
            rtn = Funct(*args, **kwargs)
            dump(rtn, f)
            f.close()
        #DHASH[(id, hash)] = rtn
        return rtn
    return cache


def test(): 
    return 'OK!'


assert cache_funct('test', test)() == 'OK!'
assert cache_funct('test', test)() == 'OK!'


def set_cache(id, value):
    path = 'cache/%s.cache' % id
    f = open(path, 'wb')
    dump(value, f)
    f.close()


DCACHE = {}


def get_from_cache(id, default_):
    if not USE_CACHE:
        return default_
    
    if id in DCACHE: 
        return DCACHE[id]
    
    path = 'cache/%s.cache' % id
    if os.path.exists(path) and os.path.getsize(path):
        print(('Opening %s -' % id), end=' ')
        t_from = time.time()
        f = open(path, 'rb')
        rtn = load(f)
        f.close()
        print('%ssec OK' % (time.time()-t_from))
    else: 
        rtn = default_
    
    #DCACHE[id] = rtn
    return rtn
