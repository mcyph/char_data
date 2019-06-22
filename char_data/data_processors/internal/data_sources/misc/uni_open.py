from char_data.data_paths import data_path

UNICODE_PATH = data_path('chardata', 'unidata/source/%s')


def uni_open(file_name):
    path = UNICODE_PATH % file_name
    f = open(path, 'r', encoding='utf-8', errors='replace')
    return f
