from char_data.toolkit.json_tools import load
from char_data.data_paths import data_path
from char_data.toolkit.py_ini.read import read_D_pyini
from char_data.formatters import property_formatters


LData = [
    ('unicodedata', 'unidata'),
    ('unihan', 'unihan'),
    ('ccdict', 'ccdict'),
    ('kanjidic', 'kanjidic'),
    ('nameslist', 'nameslist')
]


def get_D_data():
    """
    Load the basic data instances
    """
    for key, path in LData:
        print()
        print()
        print(('FOR:: %s' % key))

        open_data(
            data_path('chardata', '%s/output/%s' % (path, path))
        )

    #D = self.D['hanzi_variants'] = {}

    #D['japanesesimplified'] = (
    #    property_formatters.JaSimplified('japanesesimplified')
    #)
    #D['chinesetraditional'] = (
    #    property_formatters.JaSimplified('chinesetraditional')
    #)

    #for key in property_formatters.LHanziVariantKeys:
    #    D[key.lower().replace(' ', '_')] = property_formatters.CEDictVariants(key)


def open_data(path):
    LRtn = []

    DKeys = load(path + '.json')
    DINI = read_D_pyini(path.replace('/output/', '/') + '.pyini')
    # print(DINI)

    with open('%s.bin' % path, 'r+b') as f:
        for key, DJSON in list(DKeys.items()):
            i_DINI = DINI[key]

            LRtn.append(
                instance_from_D_ini(key, i_DINI)
            )

    LRtn.sort()
    print(('\n'.join(i[-1] for i in LRtn)))
    return LRtn


format = '''
self.%(variable_name)s = %(class_name)s(
    self, %(category_constant)s, '%(original_name)s', '%(short_description)s',
    LISOs=%(LISOs)s, index=%(index)s
)'''.strip()


SFormatters = {
    'RadicalStrokes',
    'Definition',
    'Indices',
    'NoFormatIntegers',
    'Definition',
    'NoFormatStrings',
    'Encoding',
    'IRG',
    'UnicodeHex',
    'Frequency',
    'StringEnum',
    'BooleanEnum',
    'MappingLink',
    'Hex',
    'Readings'
}

HEADER_DEFINITION = 0
HEADER_NAMED_ALIASES = 1
HEADER_READINGS = 2
HEADER_SEE_ALSO = 3
HEADER_BLOCK_INFO = 4
HEADER_SUBBLOCK_INFO = 5
HEADER_SCRIPTS_BLOCKS = 6
HEADER_UNICODE_GENERAL = 7
HEADER_CASING = 8
HEADER_NORMALISATION = 9
HEADER_NUMERIC = 10
HEADER_LANGUAGE_USAGE = 11
HEADER_VARIANTS = 12
HEADER_GRADES_FREQUENCIES = 13
HEADER_TOTAL_STROKES = 14
HEADER_RADICAL_STROKES = 15
HEADER_INPUT = 16
HEADER_ENCODING = 17
HEADER_UNICODE_LAYOUT = 18
HEADER_INDICES = 19
HEADER_PHONETIC_INDICES = 20
HEADER_ADOBE = 21
HEADER_FIXME = None  # TODO!!!










DHeaders = {
    'Definition': 'HEADER_DEFINITION',
    'Numeric': 'HEADER_NUMERIC',
    'Readings': 'HEADER_READINGS',
    'Language Usage': 'HEADER_LANGUAGE_USAGE',
    'Variants': 'HEADER_VARIANTS',
    'Grades/Frequencies': 'HEADER_GRADES_FREQUENCIES',
    'Total Strokes': 'HEADER_TOTAL_STROKES',
    'Radical/Additional Strokes': 'HEADER_RADICAL_STROKES',
    'Input': 'HEADER_INPUT',
    'Encoding': 'HEADER_ENCODING',
    'Indices': 'HEADER_INDICES',
    'Phonetic Indices': 'HEADER_PHONETIC_INDICES',
    'Adobe': 'HEADER_ADOBE',
    None: 'HEADER_FIXME',

    'definition': 'HEADER_DEFINITION',
    'Unicode general': 'HEADER_UNICODE_GENERAL',
    'layout': 'HEADER_UNICODE_LAYOUT',
    'scripts/blocks': 'HEADER_SCRIPTS_BLOCKS',
    'normalization': 'HEADER_NORMALISATION',
    'casing': 'HEADER_CASING',
    'numeric': 'HEADER_NUMERIC',
    'named aliases': 'HEADER_NAMED_ALIASES'
}


def instance_from_D_ini(key, DINI):
    assert DINI['formatter'] in SFormatters, DINI['formatter']

    D = {}
    D['variable_name'] = key.replace('/', '_').replace(' ', '_').replace('-', '_').replace('.', '_').lower()
    D['class_name'] = DINI['formatter']
    D['category_constant'] = DHeaders.get(DINI['header'], DHeaders[None])
    D['original_name'] = key
    D['short_description'] = DINI.get('name', key.title()).replace("'", "\\'")
    D['LISOs'] = DINI.get('LLangs', None)
    D['index'] = DINI.get('index', None)

    s = format % D
    return (eval(D['category_constant']), D['variable_name']), s




if __name__ == '__main__':
    get_D_data()

