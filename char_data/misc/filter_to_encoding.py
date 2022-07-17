def filter_to_encoding(Encoding, LChars):
    #print LChars
    return_list = []
    for i in LChars:
        try:
            if ord(chr(i).encode(Encoding, 'ignore').decode(Encoding, 'ignore')) == i:
                return_list.append(i)
        except:
            pass
            #print 'filterToEnc ERROR:', i
    return return_list
