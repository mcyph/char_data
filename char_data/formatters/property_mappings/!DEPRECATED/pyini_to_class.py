from toolkit.json_tools import load
from char_data.data_paths import data_path
from toolkit.py_ini.read import read_D_pyini
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
        print
        print
        print 'FOR:: %s' % key

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
    # print DINI

    with open('%s.bin' % path, 'r+b') as f:
        for key, DJSON in DKeys.items():
            i_DINI = DINI[key]

            LRtn.append(
                instance_from_D_ini(key, i_DINI)
            )

    LRtn.sort()
    print '\n'.join(i[-1] for i in LRtn)
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
HEADER_NUMERIC = 1
HEADER_READINGS = 2
HEADER_LANGUAGE_USAGE = 3
HEADER_VARIANTS = 4
HEADER_GRADES_FREQUENCIES = 5
HEADER_TOTAL_STROKES = 6
HEADER_RADICAL_STROKES = 7
HEADER_INPUT = 8
HEADER_ENCODING = 9
HEADER_INDICES = 10
HEADER_PHONETIC_INDICES = 11
HEADER_ADOBE = 12
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
    None: 'HEADER_FIXME'
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

