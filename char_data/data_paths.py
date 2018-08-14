import os
from toolkit.data_paths import DataPaths

dir_path = os.path.dirname(os.path.realpath(__file__))

data_paths = DataPaths(dir_path, {
    "chardata": "char_data/data",

    "chinese_variants": "char_data/data/chinese_variants",
    "j_simplified": "char_data/data/j_simplified"
})
data_path = data_paths.data_path

