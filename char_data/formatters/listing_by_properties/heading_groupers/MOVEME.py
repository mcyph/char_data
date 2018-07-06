def too_many_chars(L):
    Total = 0
    for i in L:
        if type(i) == tuple:
            From, To = i
            Total += To-From
        else:
            Total += 1
        
        if Total > 15000:
            return True
    return False


def filter_to_enc(Encoding, LChars):
    #print LChars
    LRtn = []
    for i in LChars:
        try: 
            if ord(unichr(i).encode(Encoding, 'ignore').decode(Encoding, 'ignore')) == i:
                LRtn.append(i)
        except: 
            pass
            #print 'filterToEnc ERROR:', i
    return LRtn
