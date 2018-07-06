import os
from uni_open import uni_open


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
            print "ERROR:", Hex
            raise


def open_scsv(Path):
    # Open a Unicode file, separated by semicolons
    #print Path, os.getcwdu()
    f = uni_open(Path)

    # File = codecs.open_scsv(Path, 'rb', 'utf-8')
    for line in f:
        line = line.split('#')[0].strip()
        if not line:
            continue

        LLine = [i.strip() for i in line.split(';')]
        # print 'open_scsv line:', LLine

        # Output the codepoint as either a
        # tuple range or a single codepoint
        LLine[0] = get_code_point(LLine[0])

        yield LLine
    f.close()
