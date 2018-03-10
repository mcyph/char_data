# -*- coding: utf-8 -*-
# HACK FILE!

import unicodedata
#import fastdist
from title_idx.language_support.Stem import get_L_stemmed
from toolkit.rem_dupes import rem_dupes
from toolkit.white_space import WHITESPACE, tWHITESPACE
from toolkit.surrogates import w_ord
#from Translit.TranslitEngine import get_engine
#CTones2PinYin = get_engine('Chinese Pinyin Accents-PinYin')

DAlt = {u'け': u'か',
        u'せ': u'',
        u'せ': u'せさ', # sense-/dasai (dasse-) HACK!
        u'て': u'た',
        #u'げ': u'が',
        u'げ': u'ご', # suge- (sugoi) HACK!
        u'ぜ': u'ざ',
        u'へ': u'は',
        u'べ': u'ば',
        u'ぺ': u'ぱ',
        u'め': u'ま',
        u'れ': u'ら',
        u'ね': u'な',
        u'え': u'わ', # koe- (kowai)
        u'で': u'ど', # hide- (hidoi)
        }

#================================================================#
#                      Filter Accents/Tones                      #
#================================================================#

DNums = {'0': None, '1': None, '2': None, '3': None, 
         '4': None, '5': None, '6': None, '7': None, '8': None, '9': None, '10': None}
def remove_tones(Word):
    Word = Word.replace(' ', '')
    Word = ''.join([i for i in Word if i not in DNums])
    return Word

bAccents = u'̣̉̀̃́'
aAccents = u'̛̣́̀̃̂̆̉'
DbAccents = {}
for i in bAccents: DbAccents[i] = None
DaAccents = {}
for i in aAccents: DaAccents[i] = None

#def filter_vie_accents(Word, AllAccents):
#    # TODO: WTF does this code DO?
#    Word = Word.replace(' ', '')
#    Word = ''.join([i for i in Word if i not in DNums])
#    return Word

tAccents = u'ก่ก้ก๊ก๋ก็ก์'.replace(u'ก', '')
DtAccents = {}
for i in tAccents: DtAccents[i] = None
def filter_thai_accents(Word):
    Word = Word.replace(' ', '')
    Word = ''.join([i for i in Word if i not in DtAccents])
    return Word

DIgnore = {'Lm': 'Letter, Modifier',
           'Mn': 'Letter, Nonspacing',
           'Mc': 'Mark, Spacing Combining',
           'Me': 'Mark, Combining',
           'Sk': 'Symbol, Modifier',
           'Cc': 'Other, Control',
           'Cf': 'Other, Format'}

def get_cat(S):
    # TODO: Should there be better error handling?
    try: return unicodedata.category(S)
    except: return None

def filter_accents(Word):
    # Remove accents for e.g. French
    # FIXME: convert e.g. LATIN LETTER L WITH HOOK to LATIN LETTER L!
    Word = unicode(Word)
    Word = Word.replace(' ', '')
    Word = ''.join([i for i in Word if not get_cat(i) in DIgnore])
    return Word

def is_hanzi(S):
    Ord = w_ord(S)
    if Ord >= 0x4E00 and Ord <= 0x9FFF: return 1
    elif Ord >= 0x3400 and Ord <= 0x4DBF: return 1
    return 0

def get_L_words(fISOCode, fVariant, Word, Deinflect=False):
    if fISOCode in ('cmn', 'yue'):
        # NOTE: Filtering Chinese accents is probably a bad idea 
        # as say "pin" could have multiple headers, so I think
        # it's best to filter the accents at e.g. a CEDict level 
        # and sort by character frequency :-P
        
        # Replace commonly confused PinYin
        # combinations by Westerners :-P
        # TODO: Should this be in "Deinflect" (or a separate mode?)
        if Deinflect or len(Word) > 5:
            # TODO: What about "similar" mode? ---------------------------------------------
            R = Word.replace('r', 'l')
            if R.endswith('dz'): R = R[:-2]+'zi' # Yale Handz (Hanzi) HACK!
            if R.endswith('z'): R = R[:-1]+'i'
            R = R.replace('e', 'a')
            R = R.replace('o', 'u')
            R = R.replace('d', 't')
            R = R.replace('y', 'i')
            # OPEN ISSUE: Should this be -> ts?
            R = R.replace('i', 'u') # CONTROVERSIAL - PinYin "i" often sounds like "u"!
            
            # replace "ch"-related sounds
            R = R.replace('ch', 'q')
            R = R.replace('j', 'q')
            R = R.replace('zh', 'q')
            R = R.replace('sh', 'q') # CONTROVERSIAL!
            R = R.replace('x', 'q') # OPEN ISSUE: Should this be "s" or "c"?
            
            # replace "ts"-related sounds
            #R = R.replace('c', 's') # CONTROVERSIAL!
            R = R.replace('z', 'c') # Sometimes sounds like "ts" as in "Hanzi"?
            R = R.replace('ts', 'c')
            
            R = R.replace('s', 'q')
            return (Word, R) #remove_tones(Word))
        else: return (Word,)
        
    #elif fISOCode == 'vie':
        #return (Word, filter_vie_accents(Word, False), filter_vie_accents(Word, True))
    elif fISOCode == 'tha':
        return (Word, filter_thai_accents(Word))
    elif fISOCode == 'jpn':
        # Add Katakana -> Hiragana in no accents mode
        iConv = Word # ''.join([Conv(i) for i in Word])
        # Use romaji for more accurate similar results
        #Latin = HiraToRomaji(KataToRomaji(iConv))
        # TODO: What if the Latin is WRONG?
        #Latin = '^%s^' % Latin # Make sure Latin titles aren't confused!
        
        # Spaces are replaced to fix startswith/endswith queries
        NoSpaces = iConv.replace('_', '')
        LRtn = (Word, 
               NoSpaces, 
               #Latin.lower().replace('_', '')
               )
        
        oNoSpaces = NoSpaces
        if not Deinflect and NoSpaces:
            # Masculine Japanese HACK - 
            # Converts "uzee" into "uzai" etc
            #print 'NoSpaces:', NoSpaces.encode('utf-8')
            
            NoSpaces = unicodedata.normalize('NFC', unicode(NoSpaces)) # HACK!
            Override = NoSpaces[-1] in u'ーぇ' or u'しぇ' in NoSpaces
            
            # Fix shenshei (sensei) as used in Lucky Star (if I recall correctly) :-P
            NoSpaces = NoSpaces.replace(u'しぇ', u'せ')
            
            NoSpaces = NoSpaces.replace(u'ー', u'え')
            NoSpaces = NoSpaces.replace(u'ぇ', u'え')
            # Koeeee (Kowai) HACK!
            while NoSpaces[-3:] == u'えええ':
                NoSpaces = NoSpaces[:-1]
            # Fix Sugeee (Sugoi) etc
            while NoSpaces[-2:] == u'ええ' and NoSpaces[1] != u'え':
                NoSpaces = NoSpaces[:-1]
            
            if len(NoSpaces) > 1 and ((NoSpaces[-1] == u'え' and NoSpaces[-2] in DAlt) or Override):
                if NoSpaces[-2] in DAlt:
                    LAltChars = DAlt[NoSpaces[-2]]
                else: LAltChars = NoSpaces[-2]
                
                for AltChar in LAltChars:
                    Masculine = u'%s%s' % (NoSpaces[:-2], AltChar)
                    Masculine = unicodedata.normalize('NFD', Masculine) # HACK!
                    Masculine = Masculine.replace(u'っ', '') # Get rid of 'dekke-' (dekai) etc :-P
                    
                    if is_hanzi(Masculine[0]):
                        # Fix [Ko]wai -> [Kowa]i when first character Kanji
                        KanjiForm = Masculine[0]+Masculine[2:]
                        LRtn += (u'%sい' % Masculine, 
                                 u'%sい' % KanjiForm)
                    else: 
                        LRtn += (u'%sい' % Masculine,)
        
        if Deinflect and NoSpaces: 
            # In deinflect mode, look up possible stems in the character data
            from mscSentenceJpn import IsKana # HACK!
            if is_hanzi(oNoSpaces[0]) and IsKana(oNoSpaces[1:]):
                from char_data.CharData import CharData # HACK!
                LKun = CharData.raw_data('Japanese Kun', 
                                                    w_ord(oNoSpaces[0]))
                if LKun:
                    LKun = unicodedata.normalize('NFD', LKun[0]).replace('-', '').split(' ')
                    LExtend = ['%s%s' % (oNoSpaces[0], i.split('.')[1]) for i in LKun if '.' in i]
                    LExtend = [(fastdist.distance(oNoSpaces, i), i) for i in LExtend]
                    LExtend.sort(key=lambda x: -x[0])
                    LRtn += tuple([i[1] for i in LExtend])
        
        print ';'.join(LRtn).encode('utf-8')
        return LRtn
    else:
        Rtn = (Word, filter_accents(Word))
        #print 'get_L_words RTN:', Rtn
        return Rtn

#================================================================#
#                      Get Processed Words                       #
#================================================================#

# TODO: It does make sense to cache the result of process_word, 
# but disk access causes more penalty than it's worth!
# Therefore it should use the LRU cache once it's been written :-)
def get_deinflect_word(Word, fISOCode, fVariant, StripWhite=True):
    # RETURNS A LIST!
    # This forces the index and the search words to have 
    # the same properties, e.g. fullwidth spaces are treated 
    # like every other space and Hiragana/Katakana are converted 
    # to Latin to improve accuracy in similar searches
    if StripWhite:
        Word = Word.strip(tWHITESPACE).lower()
        
        # convert whitespace to underscores
        DWhitespace = WHITESPACE # Make sure global lookup doesn't affect performance
        nWord = []
        for c in Word:
            if c in DWhitespace:
                # Make sure all spaces are alike, so that e.g. 
                # fullwidth spaces or tabs don't mess up searches
                nWord.append('_')
            else: nWord.append(c)
        Word = ''.join(nWord)
    else: Word = Word.lower()
    
    #assert type(fISOCode) in (str, unicode)
    #assert type(fVariant) in (str, unicode)
    #print fISOCode, fVariant
    
    if fISOCode == 'cmn' or fISOCode == 'yue':
        # PinYin? Remove spaces and make it in the format 
        # "pin1yin3" internally
        Word = Word.replace('_', '')
        Word = CTones2PinYin.convert(Word)
    elif fISOCode == 'jpn':
        # Return using the grammar parser to deinflect words
        # TODO: AUTO-CONVERT from Kanji -> Kana???
        LWords = []
        for D in JDeinflect(Word.replace('_', ' ')):
            if 'origform' in D:
                #print 'OrigForm:', D['origform'].encode('utf-8')
                LWords.append(D['origform'].replace('_', '~'))
            else: LWords.append(D['word'].replace('_', '~'))
        Word = '_'.join(LWords)
        #Word = Word.replace('__', '_')
    
    # convert to combining characters
    # This allows more accurate Latin-language, e.g. Vietnamese 
    # as the accent is separate to the other letters in similar searching
    Word = unicodedata.normalize('NFD', unicode(Word))
    #print 'Word:', Word.encode('utf-8'), fISOCode, fVariant
    
    # convert to the dictionary form of the word
    # THIS IS EXTREMELY CONTROVERSIAL! IF THIS IS DISABLED, 
    # REMEMBER TO TURN DEINFLECT BACK ON IN dbsResultSearch!!!
    # It definitely has exceptions where it doesn't 
    # work, so I remain open to changes :-)
    LWords = get_L_stemmed(Word.lower().replace('_', ' '), fISOCode, fVariant)
    # Just choose the first deinflected form if multiple available
    if LWords and LWords[0]: 
        Word = LWords[0].replace(' ', '_').lower()
    if StripWhite: 
        return [i for i in rem_dupes(get_L_words(fISOCode, fVariant, Word, True)) if i.strip()]
    else: return Word

def get_sub_word_internal(Word, fISOCode, fVariant, StripWhite=True):
    # RETURNS A LIST!
    # When using GetWordEntry() above, it gets the *dictionary* 
    # form, e.g. 'running' gets 'run'. When individual entries in 
    # a dictionary are in Katakana or not in the base dictionary form,
    # this can disambiguate. If the dictionary entry is 'run'
    # it will show the inflected form, e.g. running, runner, ran etc
    
    # if the individual word matches the dictionary entry, it just uses a 
    # dot point. This is used for internal purposes, so the combining form 
    # is used with underscores as spaces. If Chinese/Vietnamese, it returns 
    # with and without tones
    
    #assert type(fISOCode) in (str, unicode)
    #assert type(fVariant) in (str, unicode)
    
    # convert whitespace to an underscore
    if StripWhite:
        DWhitespace = WHITESPACE
        Word = Word.strip(tWHITESPACE).lower()
        nWord = []
        for c in Word:
            if c in DWhitespace:
                # Make sure all spaces are alike, so that e.g. 
                # fullwidth spaces or tabs don't mess up searches
                nWord.append('_')
            else: nWord.append(c)
        Word = ''.join(nWord)
    else: Word = Word.lower()
    
    if fISOCode == 'cmn' or fISOCode == 'yue':
        # PinYin? Remove spaces and make it in the format 
        # "pin1yin3" internally
        Word = Word.replace('_', '')
        Word = CTones2PinYin.convert(Word)
    elif fISOCode == 'jpn':
        # Return using the grammar parser to break up the words
        # TODO: AUTO-CONVERT from Kanji -> Kana???
        LWords = [D['word'].replace('_', '~') for D in JDeinflect(Word.replace('_', ' '))]
        Word = '_'.join(LWords)
        #Word = Word.replace('__', '_')
    #print 'Word:', Word.encode('utf-8'), fISOCode, fVariant
    
    # convert to combining characters
    # This makes sure searches are processed correctly
    Word = unicodedata.normalize('NFD', unicode(Word))
    if StripWhite:
        return [i for i in rem_dupes(get_L_words(fISOCode, fVariant, Word, False)) if i.strip()]
    else: return Word

def get_sub_word_disp(Word, fISOCode, fVariant):
    # Same as above, except converts the internal form
    # from combining to noncombining and underscores to 
    # a single space for onscreen display
    
    # convert whitespace to spaces
    DWhitespace = WHITESPACE
    Word = Word.strip(tWHITESPACE).lower()
    nWord = []
    for c in Word:
        if c in DWhitespace or c == '_':
            # Make sure all spaces are alike, so that e.g. 
            # fullwidth spaces or tabs don't mess up searches
            nWord.append(' ')
        else: nWord.append(c)
    Word = ''.join(nWord)
    
    # convert to noncombining characters
    # This makes sure people can view the word with most fonts
    Word = unicodedata.normalize('NFC', unicode(Word))
    return Word
