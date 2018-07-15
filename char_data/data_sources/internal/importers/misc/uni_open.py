import codecs
from char_data.data_paths import data_path

UNICODE_PATH = data_path('chardata', 'unidata/source/%s')


def uni_open(file_name):
    path = UNICODE_PATH % file_name
    f = codecs.open(path, 'rb', 'utf-8', 'replace')
    return f
