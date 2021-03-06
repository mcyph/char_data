***********************
LangLynx Character Data
***********************

LangLynx Character Data is a module which allows accessing character information
about Unicode characters, made for the language dictionary/learning software software
LangLynx. It allows querying from various different sources.

Different sources of data
#########################

"Internal" data sources:
************************

"Internal" data sources use custom memory-mapped array-backed datatypes,
optimised for storage space.

* ccdict:
    * **Name:** CCDict dictionary. For Cantonese, Hakka and other Chinese Hanzi definitions and readings.
    * **Updated:** 2006
    * **URL:** http://www.chineselanguage.org
    * **License:** A Creative Commons Attribution 2.5 License.
* kanjidic:
    * **Name:** KANJIDIC. For Japanese Kanji information.
    * **Updated:** ???
    * **URL:** http://www.edrdg.org/wiki/index.php/KANJIDIC_Project
    * **License:** A Creative Commons Attribution-ShareAlike Licence (V3.0).
* unicodedata:
    * **Name:** Unicode character database
    * **Updated:** ???
    * **URL:** https://unicode.org/ucd/
    * **License:** The Unicode data files and software license: https://www.unicode.org/license.html
* unihan:
    * **Name:** Unihan. For all Hanzi/Kanji/Korean Hanja with large amounts of information. However, definitions are most targed towards Chinese Hanzi.
    * **Updated:** ???
    * **URL:** https://unicode.org/charts/unihan.html
    * **License:** The Unicode data files and software license: https://www.unicode.org/license.html

"External" data sources:
************************

"External" data sources allow accessing external data, such as python's
standard encoding mappings. They may not allow searching or other
functionality that "internal" ones do.

* reformatted
* standard_encodings
* cldralphabets:
* hanzi_variants:

Character Data Searching
########################

# aaa

.. code-block:: python

    >>> from char_data import char_data

    >>> char_data.get_key_info('standard_encodings.cp869')
    <char_data.CharData.CharDataKeyInfo instance at 0x7f65c3202b90>

    >>> unicode(char_data.get_key_info('standard_encodings.cp869'))
    u'CharDataKeyInfo(key=standard_encodings.cp869, original_key=cp869, header_const=Encoding, char_index_key_info=None)'

    >> char_data.raw_data(key='name', ord_=55)
    (u'DIGIT SEVEN',)

    >> char_data.formatted(key='name', ord_=55)
    (u'digit seven',)

    >> char_data.html_formatted(key='name', ord_=55)
    u'digit seven'

    >>> char_data.keys()
    ['ccdict.big5', 'ccdict.cangjie', 'ccdict.cantonese', 'ccdict.cns11643',
    'ccdict.english', 'ccdict.fourcorner', 'ccdict.gb', 'ccdict.hakka',
    'ccdict.mandarin', 'ccdict.r_s', 'ccdict.totalstrokes', 'ccdict.utf8',
    'cldr_alphabets.alphabets', 'hanzi_variants.abbreviated_form',
    'hanzi_variants.antonym', 'hanzi_variants.archaic_form',
    'hanzi_variants.archaic_variant', 'hanzi_variants.chinese_classifier',
    'hanzi_variants.chinese_traditional', 'hanzi_variants.correct_form',
    'hanzi_variants.erhua_variant', 'hanzi_variants.erroneous_form',
    'hanzi_variants.japanese_simplified', 'hanzi_variants.japanese_variant',
    'hanzi_variants.less_common_variant', 'hanzi_variants.modern_form',
    'hanzi_variants.modern_variant', 'hanzi_variants.more_common_variant',
    'hanzi_variants.non_erhua_variant', 'hanzi_variants.non_japanese_variant',
    'hanzi_variants.non_prc_variant', 'hanzi_variants.obscure_variant',
    'hanzi_variants.other_variant', 'hanzi_variants.popular_variant',
    'hanzi_variants.prc_variant', 'hanzi_variants.same_as', 'hanzi_variants.see_also',
    'hanzi_variants.unabbreviated_form', 'hanzi_variants.variant_of',
    'hanzi_variants.words_which_can_use_classifier', 'kanjidic.crossref_deroo',
    'kanjidic.crossref_jis208', 'kanjidic.crossref_jis212', 'kanjidic.crossref_jis213',
    'kanjidic.crossref_nelson_c', 'kanjidic.crossref_njecd', 'kanjidic.crossref_oneill',
    'kanjidic.crossref_s_h', 'kanjidic.crossref_ucs', 'kanjidic.dicref_busy_people',
    'kanjidic.dicref_crowley', 'kanjidic.dicref_gakken', 'kanjidic.dicref_halpern_kkld',
    'kanjidic.dicref_halpern_njecd', 'kanjidic.dicref_heisig', 'kanjidic.dicref_henshall',
    'kanjidic.dicref_henshall3', 'kanjidic.dicref_jf_cards',
    'kanjidic.dicref_kanji_in_context', 'kanjidic.dicref_kodansha_compact',
    'kanjidic.dicref_maniette', 'kanjidic.dicref_moro', 'kanjidic.dicref_nelson_c',
    'kanjidic.dicref_nelson_n', 'kanjidic.dicref_oneill_kk',
    'kanjidic.dicref_oneill_names', 'kanjidic.dicref_sakade', 'kanjidic.dicref_sh_kk',
    'kanjidic.dicref_tutt_cards', 'kanjidic.freq', 'kanjidic.grade',
    'kanjidic.jlpt', 'kanjidic.meaning', 'kanjidic.meaning_es', 'kanjidic.meaning_fr',
    'kanjidic.meaning_pt', 'kanjidic.querycode_deroo', 'kanjidic.querycode_four_corner',
    'kanjidic.querycode_sh_desc', 'kanjidic.rad_classical', 'kanjidic.rad_name',
    'kanjidic.rad_nelson_c', 'kanjidic.reading_ja_kun', 'kanjidic.reading_ja_on',
    'kanjidic.reading_korean_h', 'kanjidic.reading_korean_r', 'kanjidic.reading_nanori',
    'kanjidic.reading_pinyin', 'kanjidic.stroke_count',
    'reformatted.emoji_and_other_symbols', 'reformatted.inherited',
    'standard_encodings.ascii', 'standard_encodings.big5', 'standard_encodings.big5hkscs',
    'standard_encodings.cp037', 'standard_encodings.cp1006', 'standard_encodings.cp1026',
    'standard_encodings.cp1140', 'standard_encodings.cp1250', 'standard_encodings.cp1251',
    'standard_encodings.cp1252', 'standard_encodings.cp1253', 'standard_encodings.cp1254',
    'standard_encodings.cp1255', 'standard_encodings.cp1256', 'standard_encodings.cp1257',
    'standard_encodings.cp1258', 'standard_encodings.cp424', 'standard_encodings.cp437',
    'standard_encodings.cp500', 'standard_encodings.cp737', 'standard_encodings.cp775',
    'standard_encodings.cp850', 'standard_encodings.cp852', 'standard_encodings.cp855',
    'standard_encodings.cp856', 'standard_encodings.cp857', 'standard_encodings.cp860',
    'standard_encodings.cp861', 'standard_encodings.cp862', 'standard_encodings.cp863',
    'standard_encodings.cp864', 'standard_encodings.cp865', 'standard_encodings.cp866',
    'standard_encodings.cp869', 'standard_encodings.cp874', 'standard_encodings.cp875',
    'standard_encodings.cp932', 'standard_encodings.cp949', 'standard_encodings.cp950',
    'standard_encodings.euc_jis_2004', 'standard_encodings.euc_jisx0213',
    'standard_encodings.euc_jp', 'standard_encodings.euc_kr',
    'standard_encodings.gb18030', 'standard_encodings.gb2312', 'standard_encodings.gbk',
    'standard_encodings.hz', 'standard_encodings.iso2022_jp',
    'standard_encodings.iso2022_jp_1', 'standard_encodings.iso2022_jp_2',
    'standard_encodings.iso2022_jp_2004', 'standard_encodings.iso2022_jp_3',
    'standard_encodings.iso2022_jp_ext', 'standard_encodings.iso2022_kr',
    'standard_encodings.iso8859_10', 'standard_encodings.iso8859_13',
    'standard_encodings.iso8859_14', 'standard_encodings.iso8859_15',
    'standard_encodings.iso8859_2', 'standard_encodings.iso8859_3',
    'standard_encodings.iso8859_4', 'standard_encodings.iso8859_5',
    'standard_encodings.iso8859_6', 'standard_encodings.iso8859_7',
    'standard_encodings.iso8859_8', 'standard_encodings.iso8859_9',
    'standard_encodings.johab', 'standard_encodings.koi8_r', 'standard_encodings.koi8_u',
    'standard_encodings.latin_1', 'standard_encodings.mac_cyrillic',
    'standard_encodings.mac_greek', 'standard_encodings.mac_iceland',
    'standard_encodings.mac_latin2', 'standard_encodings.mac_roman',
    'standard_encodings.mac_turkish', 'standard_encodings.ptcp154',
    'standard_encodings.shift_jis', 'standard_encodings.shift_jis_2004',
    'standard_encodings.shift_jisx0213', 'standard_encodings.utf_16',
    'standard_encodings.utf_16_be', 'standard_encodings.utf_16_le',
    'standard_encodings.utf_7', 'standard_encodings.utf_8', 'unicodedata.age',
    'unicodedata.also_called', 'unicodedata.arabic_shaping_group',
    'unicodedata.arabic_shaping_type', 'unicodedata.bidi_mirroring',
    'unicodedata.bidirectional_category', 'unicodedata.block',
    'unicodedata.block_description', 'unicodedata.block_name',
    'unicodedata.canonical_combining_classes', 'unicodedata.case_folding',
    'unicodedata.case_folding_status', 'unicodedata.changes_when_nfkc_casefolded',
    'unicodedata.comments', 'unicodedata.compatibility_mapping',
    'unicodedata.composition_exclusions', 'unicodedata.conscript_blocks',
    'unicodedata.conscript_name', 'unicodedata.core_properties',
    'unicodedata.decimal_digit_value', 'unicodedata.decomposed_form',
    'unicodedata.digit_value', 'unicodedata.east_asian_width',
    'unicodedata.expands_on_nfc', 'unicodedata.expands_on_nfd',
    'unicodedata.expands_on_nfkc', 'unicodedata.expands_on_nfkd',
    'unicodedata.fc_nfkc_closure', 'unicodedata.formally_also_called',
    'unicodedata.full_composition_exclusion', 'unicodedata.general_category',
    'unicodedata.grapheme_break', 'unicodedata.joining_type', 'unicodedata.line_break',
    'unicodedata.lowercase', 'unicodedata.mirrored', 'unicodedata.name',
    'unicodedata.named_aliases', 'unicodedata.nfc_quick_check',
    'unicodedata.nfd_quick_check', 'unicodedata.nfkc_casefold',
    'unicodedata.nfkc_quick_check', 'unicodedata.nfkd_quick_check',
    'unicodedata.normalization_corrections_corrected',
    'unicodedata.normalization_corrections_errors', 'unicodedata.numeric_value',
    'unicodedata.property_list', 'unicodedata.script', 'unicodedata.see_also',
    'unicodedata.sentence_break', 'unicodedata.special_casing_condition_list',
    'unicodedata.special_casing_lower', 'unicodedata.special_casing_title',
    'unicodedata.special_casing_upper', 'unicodedata.subblock_heading',
    'unicodedata.subblock_see_also', 'unicodedata.subblock_technical_notice',
    'unicodedata.technical_notice', 'unicodedata.titlecase',
    'unicodedata.unicode_1_0_name', 'unicodedata.uppercase',
    'unicodedata.word_break', 'unihan.accountingnumeric', 'unihan.bigfive',
    'unihan.cangjie', 'unihan.cantonese', 'unihan.cccii', 'unihan.cheungbauer',
    'unihan.cheungbauerindex', 'unihan.cihait', 'unihan.cns1986', 'unihan.cns1992',
    'unihan.compatibilityvariant', 'unihan.cowles', 'unihan.daejaweon',
    'unihan.definition', 'unihan.eacc', 'unihan.fenn', 'unihan.fennindex',
    'unihan.fourcornercode', 'unihan.frequency', 'unihan.gb0', 'unihan.gb1',
    'unihan.gb3', 'unihan.gb5', 'unihan.gb7', 'unihan.gb8', 'unihan.gradelevel',
    'unihan.gsr', 'unihan.hangul', 'unihan.hanyu', 'unihan.hanyupinlu',
    'unihan.hanyupinyin', 'unihan.hdzradbreak', 'unihan.hkglyph', 'unihan.hkscs',
    'unihan.ibmjapan', 'unihan.iicore', 'unihan.irg_gsource', 'unihan.irg_hsource',
    'unihan.irg_jsource', 'unihan.irg_kpsource', 'unihan.irg_ksource',
    'unihan.irg_msource', 'unihan.irg_tsource', 'unihan.irg_usource',
    'unihan.irg_vsource', 'unihan.irgdaejaweon', 'unihan.irgdaikanwaziten',
    'unihan.irghanyudazidian', 'unihan.irgkangxi', 'unihan.japanesekun',
    'unihan.japaneseon', 'unihan.jis0', 'unihan.jis0213', 'unihan.jis1',
    'unihan.kangxi', 'unihan.karlgren', 'unihan.korean', 'unihan.kps0',
    'unihan.kps1', 'unihan.ksc0', 'unihan.ksc1', 'unihan.lau',
    'unihan.mainlandtelegraph', 'unihan.mandarin', 'unihan.matthews',
    'unihan.meyerwempe', 'unihan.morohashi', 'unihan.nelson', 'unihan.othernumeric',
    'unihan.phonetic', 'unihan.primarynumeric', 'unihan.pseudogb1',
    'unihan.rsadobe_japan1_6', 'unihan.rsjapanese', 'unihan.rskangxi',
    'unihan.rskanwa', 'unihan.rskorean', 'unihan.rsunicode', 'unihan.sbgy',
    'unihan.semanticvariant', 'unihan.simplifiedvariant',
    'unihan.specializedsemanticvariant', 'unihan.taiwantelegraph', 'unihan.tang',
    'unihan.totalstrokes', 'unihan.traditionalvariant', 'unihan.vietnamese',
    'unihan.xerox', 'unihan.xhc1983', 'unihan.zvariant']


Character Index Searching
#########################

.. code-block:: python

    from char_data import char_indexes

    >>> char_indexes.keys()

    >>> char_indexes.values(key=FIXME)

    >>> char_indexes.search(key=FIXME, value=FIXME)

    >>> key_info = char_indexes.get_key_info(key)
    ...

    >>> char_indexes.get_value_info(key, value)

