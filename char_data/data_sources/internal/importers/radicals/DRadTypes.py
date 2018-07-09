# Chinese Frequency
# Hong Kong Grade
# IICore
# Japanese Frequency
# Japanese Grade

# NOTE: RSUnicode is essentially the same as RSKangXi so I've excluded it
DRadTypes = {
    'Chinese Unified Radicals': (
        'Both', 'Unicode RS', ('unihan.frequency',
                               'unihan.gradelevel',
                               'kanjidic.freq')
    ),
    'Chinese Simplified Radicals': (
        False, 'Unicode RS', ('unihan.frequency',
                               'unihan.gradelevel',
                               'kanjidic.freq')
    ),
    'Chinese Traditional Radicals': (
        True, 'Unicode RS', ('unihan.frequency',
                             'unihan.gradelevel',
                             'kanjidic.freq')
    ),
    'Japanese Radicals': (
        True, ('Japanese', 'Unicode RS'), ('kanjidic.grade',
                                           'kanjidic.freq')
    ),
    'Korean Radicals': (
        True, ('Korean RS', 'Unicode RS'), ('unihan.frequency',
                                            'unihan.gradelevel',
                                            'kanjidic.freq')
    ),  # FIXME!
    'Tang Radicals': (
        True, 'Unicode RS', ('unihan.frequency',
                             'unihan.gradelevel',
                             'kanjidic.freq')
    ),  # FIXME!
    'Vietnamese Radicals': (
        True, 'Unicode RS', ('unihan.frequency',
                             'Hong Kong Grade',
                             'kanjidic.freq')
    )
}  # FIXME!

