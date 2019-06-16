from uni_open import uni_open
from get_code_point import get_code_point


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
        # print('open_scsv line:', LLine)

        # Output the codepoint as either a
        # tuple range or a single codepoint
        LLine[0] = get_code_point(LLine[0])

        yield LLine
    f.close()
