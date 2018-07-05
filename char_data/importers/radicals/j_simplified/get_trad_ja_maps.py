from codecs import open
from collections import defaultdict
from char_data.data_paths import data_path


def get_trad_ja_maps():
    DTradToJa = defaultdict(unicode)
    DJaToTrad = defaultdict(unicode)

    for line in open(
        data_path('chardata', 'j_simplified/JSimplified.txt'),
        'rb', 'utf-8'
    ):
        line = line.strip()
        if not line:
            continue
        ja, trad = line.split()

        for i in trad:
            DTradToJa[i] += ja

        DJaToTrad[ja] += trad

    return DTradToJa, DJaToTrad
