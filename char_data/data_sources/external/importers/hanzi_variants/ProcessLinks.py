# -*- coding: utf-8 -*-
import codecs
from json import dumps
from collections import defaultdict
from toolkit.list_operations.rem_dupes import rem_dupes

from dicts.chinese.cedict import OpenEdict

from get_L_cedict_hanzi import get_L_cedict_hanzi, ZhWord


DReverseAlias = {
    #'DLessCommonVariants': 'DMoreCommonVariants',
    'DMoreCommonVariants': 'DLessCommonVariants',

    #'DOldVariants': 'DNewVariants',
    'DNewVariants': 'DOldVariants',

    #'DAbbr': 'DLongForm',
    'DLongForm': 'DAbbr',

    ##'DVariants': 'DVariants',
    #'DSameAs': 'DSameAs',
    #'DSeeAlso': 'DSeeAlso',
}


DStartsWith = {
    # Note: The keys are based on what the
    # *character* is in relation to the *variant*

    # e.g. 戦 is the Japanese variant of 站,
    # so will be put in DJapaneseVariants

    #===========================================================#
    #                         Variants                          #
    #===========================================================#
    
    'popular variant of': 'DLessCommonVariants',
    'less common variant of': 'DMoreCommonVariants',
    'more commonly called': 'DMoreCommonVariants',

    'obscure variant of': 'DObscureVariants',
    'obscure character': 'DObscureVariants',

    'archaic variant of': 'DArchaicVariants',
    'trad variant of': 'DTradVariants', # TODO: REMOVE ME?
    'korean variant of': 'DKoreanVariants',
    'unicode compatibility': 'DCompatVariants',
    
    # Japanese Variant (therefore "combinations" won't 
    # be allowed and all characters converted)
    # -> 1? All converted (single chars only?)
    'japanese variant of': 'DJapaneseVariants',

    'prc equivalent:': 'DNonPRCVariants', # REVERSE!
    'Taiwan variant of': 'DTaiwanVariants',
    'Taiwanese variant of': 'DTaiwanVariants',
    'Taiwanese term for': 'DTaiwanVariants',
    
    # A variant, usually one character, but sometimes more 
    # and sometimes more than one variant
    # POSSIBLY will be done in every combination?
    # -> 1+ All combinations converted
    'variant': 'DVariants',
    'also variant of': 'DVariants',
    'graphic variant of': 'DVariants',
    'etymological variant of': 'DVariants',
    
    # Erhua Variant Of (adding an "er" to the end)
    # 'erhua' refers to the r-coloring or addition of the "ér"(儿) sound 
    # (transcribed in IPA as /ɚ/) to syllables in spoken Mandarin Chinese
    # -> 1+ Not converted - only "er" is 
    #    added, but "reversed" might be useful
    'erhua variant of': 'DErhua',
    
    #===========================================================#
    #                      Synonyms/Links                       #
    #===========================================================#
    
    # -> 1+, Converted, possibly reversed as well?
    'same as': 'DSameAs', # Same As
    'also written': 'DSameAs', # Also Written
    'also termed': 'DSameAs',
    'also called': 'DSameAs',
    'also known as': 'DSameAs',
    'also ': 'DSameAs',
    'another name for': 'DSameAs', # Another Name For
    'see ': 'DSeeAlso', # See (X)
    'cf ': 'DSeeAlso',
    
    # See http://en.wikipedia.org/wiki/Chinese_measure_word
    'cl:': 'DClassifier', 
    
    # (1+, All converted, with warnings?)
    'erroneous variant of': 'DErrors', # Mistakes
    'used erroneously for': 'DErrors',
    
    # (1+, All converted, with warnings?)
    'old name of': 'DOldVariants', # Old Names (of places etc)
    'old variant of': 'DOldVariants',
    'old spelling of': 'DOldVariants',
    'now ': 'DNewVariants',
    'archaic translation of': 'DOldVariants',
    'ancient translation of': 'DOldVariants',
    'ancient variant of': 'DOldVariants',
    'classical variant of': 'DOldVariants',
    
    #===========================================================#
    #                      Abbreviations                        #
    #===========================================================#
    
    # Opposite of Abbrevation (1+ short form)
    'abbr. as': 'DLongForm',
    'also abbr. to': 'DLongForm',
    'abbr. to': 'DLongForm',
    'abbr.': 'DLongForm', # CHECK ME!
    
    # Abbreviation (1+ The "long" forms of)
    'short name for': 'DAbbr',
    'contraction of': 'DAbbr',
    'abbr. for': 'DAbbr',
    'abbr. of': 'DAbbr',

    'opposite': 'DAntonyms',
}


SAllowMulti = set(
    i.strip() for i in u'''
        CL:尊[zun1], 張|张[zhang1]
        abbr. for Beijing 北京[Bei1 jing1], Shanghai 上海[Shang4 hai3]
        CL:條|条[tiao2], 套[tao4], 個|个[ge4]
        CL:棵[ke1], 個|个[ge4]
        abbr. for Tianjin 天津 also 津沽
        also transcribed variously as 馬里奧|马里奥[Ma3 li3 ao4], 馬力歐|马力欧[Ma3 li4 ou1] etc
        BWH, abbr. for a woman's three measurements, namely: bust 胸圍|胸围[xiong1 wei2], waist 腰圍|腰围[yao1 wei2]
        abbr. for Marx 馬克思|马克思[Ma3 ke4 si1], Engels 恩格斯[En1 ge2 si1], Lenin 列寧|列宁[Lie4 ning2]
        CL:個|个[ge4],隻|只[zhi1]
        variant of 三個臭皮匠，賽過一個諸葛亮|三个臭皮匠，赛过一个诸葛亮[san1 ge4 chou4 pi2 jiang5 , sai4 guo4 yi1 ge4 Zhu1 ge3 Liang4]
        abbr. for Beijing 北京[Bei1 jing1], Shanghai 上海[Shang4 hai3] or Guangzhou 廣州|广州[Guang3 zhou1]
        see 又要馬兒跑，又要馬兒不吃草|又要马儿跑，又要马儿不吃草[you4 yao4 ma3 r5 pao3 , you4 yao4 ma3 r5 bu4 chi1 cao3]
        abbr. for mathematics 數學|数学[shu4 xue2], physics 物理[wu4 li3]
        also written 伏侍, see also 服事[fu2 shi4]
        abbr. for 毛澤東思想|毛泽东思想[Mao2 Ze2 dong1 Si1 xiang3], 鄧小平理論|邓小平理论[Deng4 Xiao3 ping2 Li3 lun4]
        see 可汗[ke4 han2], 汗國|汗国[han2 guo2]
        abbr. for Shanghai 上海[Shang4 hai3], Shenzhen 深圳[Shen1 zhen4]
        see 肉豆蔻 nutmeg, 豆蔻 cardamon
    '''.split('\n') if i.strip()
)


USE_SIMPTRAD = False


class ProcessLinks:
    def __init__(self, dict_path, out_path):
        self.DFwd = defaultdict(
            lambda: defaultdict(list)
        )
        self.DRev = defaultdict(
            lambda: defaultdict(list)
        )
        
        # simp/trad Variants
        self.DSimp = {}      # The trad->simp forms
        self.DTrad = {}      # The simp->trad forms
        
        # Process CEDict
        self.process(dict_path)
        self.write(out_path)


    def process(self, path):
        for D in OpenEdict(path, 'utf-8'):
            for result in D['LMeanings']:
                # First go through each meaning to provide "reverse links" to
                # abbreviations etc to display in "See Also" headers etc

                # Append variants etc into a dict
                # NOTE: This can also be used later for JMNedict (Japanese) ->
                # Chinese conversion etc and for HK/TW etc variants

                self.append(
                    ZhWord(
                        D['trad'], D['simp'], D['pinyin']
                    ),
                    result
                )


    def write(self, out_path):
        # write the dicts to disk

        
        if not USE_SIMPTRAD:
            del self.DSimp
            del self.DTrad
        
        D = {}
        for var in dir(self):
            if not var.startswith('D'):
                continue
            
            D[var] = getattr(self, var)
            
            for key in D[var]:
                # HACK: Remove duplicates
                for sub_key in D[var][key]:
                    D[var][key][sub_key] = rem_dupes([tuple(i) for i 
                                                      in D[var][key][sub_key]])

        with codecs.open(out_path, 'wb', 'utf-8') as f:
            f.write(dumps(D, ensure_ascii=False, indent=2))


    def append_unified(self, simp, trad):
        # add trad-simp Variant
        L = self.DSimp.setdefault(trad, [])
        L.append(simp)
        
        # add simp-trad Variant
        L = self.DTrad.setdefault(simp, [])
        L.append(trad)


    def append(self, zh_word, s):
        # TODO: MAKE SURE trad/simp VARIANTS REPRESENTED!
        s = s.replace(u'成语 saw', '') # HACK!
        s = s.replace('(', ' ')
        s = s.replace(')', ' ')
        s = s.strip()

        while '  ' in s:
            s = s.replace('  ', ' ')

        LKeys = sorted(
            DStartsWith,
            key=lambda x: -len(x)
        )

        added = False
        for key in LKeys:
            if s.lower().startswith(key):
                # TODO: REMOVE FALSE POSITIVES HERE (!)
                self.add(DStartsWith[key], zh_word, s)
                added = True
                break


        if not added:
            if ' abbr. for ' in s.lower():
                self.add('DAbbr', zh_word, s)
                added = True

            elif ' variant of ' in s.lower():
                print 'OTHER VARIANT WARNING:', s
                self.add('DVariants', zh_word, s)
                added = True


        if not added and ('variant' in s or '|' in s) and not any(i in s for i in ('county', 'township', 'district', 'town')):
            print 'VARIANT WARNING:', s.encode('utf-8')


    def add(self, key, LWord, definition):
        #print key
        # Process "VARIANT or VARIANT" multiple variant syntax
        LDefinitions = []
        definition = definition.replace(' and ', ' or ')
        definition = definition.replace(u'鴕鳥 鸵鸟', u'鴕鳥|鸵鸟')


        if ' or ' in definition:
            # Multiple variants!
            print 'MULTIPLE VARIANTS:', definition
            definition = definition.replace(' or of ', ' or ')
            LDefinitions = definition.split(' or ')
        else:
            LDefinitions.append(definition)


        LDefinitionHanzi = []

        for i in LDefinitions:
            LExtend = get_L_cedict_hanzi(i)
            if len(LExtend) > 1 and not i in SAllowMulti and not definition.startswith('CL:'):
                LExtend = [LExtend[0]]
                print 'MULTIPLE HANZI WARNING:', i

            LDefinitionHanzi.extend(LExtend)


        for zh_word in LDefinitionHanzi:
            if not zh_word.simp or not zh_word.trad:
                continue # HACK!
            
            # Only use the "simplified"
            #LTradOnly = ('DJVariants', 'DKorVariants', 
            #             'DArchVariants', 'DTradVariants')
            #if key in LTradOnly: simp = trad

            if key in DReverseAlias:
                self._assign(DReverseAlias[key], zh_word, LWord)
            else:
                self._assign(key, LWord, zh_word)


    def _assign(self, key, LWord, zh_word):
        """
        Assign the variants
        """
        DFwd = self.DFwd[key]
        DRev = self.DRev[key]

        DFwd[LWord.simp].append([LWord.pinyin, zh_word])
        DFwd[LWord.trad].append([LWord.pinyin, zh_word])

        DRev[zh_word.simp].append([zh_word.pinyin, LWord])
        DRev[zh_word.trad].append([zh_word.pinyin, LWord])


if __name__ == '__main__':
    from dicts.data_paths import data_path

    ProcessLinks(
        data_path('dicts-cn', 'Mandarin/English/cedict_mdbg/cedict_ts.u8'),
        data_path('chardata', 'cedict/variants.json')
    )
