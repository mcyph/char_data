from codecs import open
from collections import defaultdict
from char_data.data_paths import data_path


def get_trad_ja_maps():
    """
    Returns dicts which convert traditional chinese to Japanese
    characters, and Japanese to traditional, respectively

    Has keys of single Hanzi/Kanji, and values as multi-character
    Unicode strings
    """
    DTradToJa = defaultdict(str)
    DJaToTrad = defaultdict(str)

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
