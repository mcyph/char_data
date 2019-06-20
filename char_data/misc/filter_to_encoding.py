def filter_to_encoding(Encoding, LChars):
    #print LChars
    LRtn = []
    for i in LChars:
        try:
            if ord(chr(i).encode(Encoding, 'ignore').decode(Encoding, 'ignore')) == i:
                LRtn.append(i)
        except:
            pass
            #print 'filterToEnc ERROR:', i
    return LRtn
