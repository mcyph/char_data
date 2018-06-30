import re
import codecs
from char_data.importer.parsers import NamesListTokens as consts


class NamesList:
    MAIN_LOGIC = [
        (('TITLE',), 'TITLE_PAGE'),
        (('BLOCKHEADER',), 'BLOCK'),
        (('NAME_LINE', 'RESERVED_LINE'), 'CHAR_ENTRY')
    ]
    
    TITLE_PAGE = [
        'SUBTITLE',
        'SUBHEADER',
        'IGNORED_LINE',
        'EMPTY_LINE',
        'NOTICE_LINE',
        'COMMENT_LINE',
        'PAGE_BREAK',
        'FILE_COMMENT'
    ]

    BLOCK = [
        'INDEX_TAB',
            
        # NOTE: I replaced CHAR_ENTRY with NAME_LINE
        # and RESERVED_LINE so they'll be properly
        # processed separately
        #'CHAR_ENTRY',
        'NAME_LINE',
        'RESERVED_LINE', # (never used)

        'SUBHEADER',
        'NOTICE_LINE',
        'EMPTY_LINE',
        'IGNORED_LINE',
        'SIDEBAR_LINE',
        'PAGE_BREAK',
        'FILE_COMMENT',

        # ADDED to fix the references after "0250 IPA Extensions 02AF"
        # NOT STRICTLY TO THE SPEC!
        'CROSS_REF'
    ]

    CHAR_ENTRY = [
        'ALIAS_LINE',
        'FORMALALIAS_LINE',
        # <- COMMENT_LINE used to be here!
        'CROSS_REF',
        'DECOMPOSITION',
        'COMPAT_MAPPING', # [[[97, 702]]]
        'IGNORED_LINE',
        'EMPTY_LINE',

        'NOTICE_LINE',
        'FILE_COMMENT',

        'COMMENT_LINE',
    ]

    def __init__(self, path):
        self.f = codecs.open(path, 'rb', 'latin-1') # CHECK ME! ============================================
    
    def close(self):
        self.f.close()
    
    def __iter__(self):
        D = {}
        last_mode = None
        
        for mode, const, match, line in self.iter_lines():
            LData = [i for i in match.groups() if i != None]
            LData = convert_hex(LData)
            
            #print mode, const, line, 
            #print mode, const, LData
            
            if last_mode!=mode or const in ('NAME_LINE', 
                                            'RESERVED_LINE', 
                                            'BLOCKHEADER', 
                                            'TITLE'):
                for i in self.process_data(last_mode, D):
                    yield i
                
                D = {}
                last_mode = mode
            
            D.setdefault(const, []).append(LData)

        if D:
            for i in self.process_data(last_mode, D):
                yield i
    
    def iter_lines(self):
        mode = None
        
        for line in self.f:
            if mode == 'CHAR_ENTRY':
                # Both BLOCK and CHAR_ENTRY must be tried in CHAR_ENTRY mode
                LTryModes = ['CHAR_ENTRY', 'BLOCK']
            elif mode:
                # Otherwise try just the current mode
                LTryModes = [mode]
            else:
                LTryModes = []
            
            match = None
            
            for try_mode in LTryModes:
                L = getattr(self, try_mode)
                for const in L:
                    s = '^%s$' % getattr(consts, const)
                    #print const, s
                    match = re.match(s, line)
                    
                    if match:
                        if const in ('NAME_LINE', 'RESERVED_LINE'): # mode == 'BLOCK' and 
                            # NAME_LINE and RESERVED_LINE are synonymous 
                            # with CHAR_ENTRY, so activate CHAR_ENTRY mode
                            mode = 'CHAR_ENTRY'
                        else:
                            mode = try_mode
                        #print s
                        
                        yield mode, const, match, line
                        break
                
                if match:
                    break
            
            if match: 
                continue
            
            for LTry, new_mode in self.MAIN_LOGIC:
                for const in LTry:
                    s = '^%s$' % getattr(consts, const)
                    match = re.match(s, line)
                    
                    if match:
                        mode = new_mode
                        yield mode, const, match, line
                        break
                
                if match:
                    break
            
            if not match:
                print '*** WARNING ***:', mode, line
        self.close()
    
    def process_data(self, mode, D):
        # Convert the raw data into something more suitable
        
        if mode == 'TITLE_PAGE':
            nD = {}
            for k, L in D.items():
                if k in ('TITLE', 'SUBTITLE', 'NOTICE_LINE'):
                    assert len(L)==1 and len(L[0])==1
                    assert isinstance(L[0][0], basestring)
                
                
                if k == 'TITLE':
                    nD['standard'] = L[0][0]
                
                elif k == 'SUBTITLE':
                    # [[u'U60M100817.lst']]
                    nD['source file'] = L[0][0]
                    
                elif k == 'NOTICE_LINE':
                    # [[u'Copyright (c) 1991-2010 Unicode, Inc.']]
                    nD['copyright'] = L[0][0]
                
                elif k == 'COMMENT_LINE':
                    # [[u'Final Unicode 6.0 names list.'], ...]
                    assert all(len(i)==1 for i in L)
                    nD['information'] = '\n'.join([i[0] for i in L])
                    
                else:
                    print 'CHAR_ENTRY warning:', k, L
            
            yield 'information', nD
                
        elif mode == 'BLOCK':
            nD = {}
            DSubBlock = {} # For supplementary comments about subblocks inside blocks
            
            for k, L in D.items():
                if k == 'BLOCKHEADER':
                    assert len(L)==1 and len(L[0]) in (3, 4), L
                    assert len(L[0][0])==1 and len(L[0][-1])==1
                    assert (isinstance(L[0][0][0], int) and
                            isinstance(L[0][-1][0], int) and
                            isinstance(L[0][1], basestring))
                    
                    nD['from'] = L[0][0][0]
                    nD['to'] = L[0][-1][0]
                    
                    if len(L[0])==4:
                        assert isinstance(L[0][2], basestring)
                        nD['block description'] = L[0][1] # e.g. "C0 Controls and Basic Latin"
                        nD['block name'] = L[0][2] # e.g. "Basic Latin"
                    
                    elif len(L[0])==3:
                        nD['block name'] = L[0][1]
                
                elif k == 'INDEX_TAB':
                    # [[]], used as a separator
                    nD['has separator'] = True
                    
                elif k == 'SUBHEADER':
                    # [[u'Based on TIS 620-2533'], [u'Consonants']]
                    assert all(len(i)==1 and isinstance(i[0], basestring) for i in L)
                    DSubBlock['subblock heading'] = [i[0] for i in L]
                    
                elif k == 'NOTICE_LINE':
                    # [[u'For viram punctuation, use the generic Indic 0964 and 0965.']]
                    assert all(len(i)==1 and isinstance(i[0], basestring) for i in L)
                    DSubBlock['subblock technical notice'] = [i[0] for i in L]
            
                elif k == 'CROSS_REF':
                    # [[u'latin small letter ae', [230]], ...]
                    assert all(len(i)==2 and 
                           isinstance(i[0], basestring) and 
                           isinstance(i[1], list) and 
                           isinstance(i[1][0], int) for i in L), L
                    DSubBlock['subblock see also'] = [(i[1][0], i[0]) for i in L]
                
                else:
                    print 'BLOCK warning:', k, L
            
            if nD:
                yield 'block', nD
            
            if DSubBlock:
                yield 'subblock', DSubBlock
        
        elif mode == 'CHAR_ENTRY':
            nD = {}
            for k, L in D.items():
                if k == 'NAME_LINE':
                    # CHAR_ENTRY mode; [[[2305], u'DEVANAGARI SIGN CANDRABINDU']]
                    assert len(L)==1 and len(L[0])==2 and len(L[0][0])==1
                    assert isinstance(L[0][0][0], int), L
                    assert isinstance(L[0][1], basestring)
                    nD['codepoint'] = L[0][0][0]
                    nD['name'] = L[0][1]
                
                elif k == 'ALIAS_LINE':
                    # [[u'latin small letter script a (1.0)']]
                    assert all(len(i)==1 and isinstance(i[0], basestring) for i in L)
                    nD['also called'] = [i[0] for i in L]
                    
                elif k == 'FORMALALIAS_LINE':
                    # [[u'KANNADA LETTER LLLA']]
                    assert all(len(i)==1 and isinstance(i[0], basestring) for i in L)
                    nD['formally also called'] = [i[0] for i in L]
                    
                elif k == 'CROSS_REF':
                    # [[u'devanagari danda', [2404]]]
                    nL = []
                    for i in L:
                        if len(i) == 2:
                            assert isinstance(i[0], basestring)
                            assert isinstance(i[1], list) and len(i[1])==1 and isinstance(i[1][0], int)
                            nL.append((i[1][0], i[0]))
                        else:
                            assert isinstance(i[0], list) and len(i[0])==1 and isinstance(i[0][0], int)
                            
                            # No character information supplied for the link, so add some
                            #import unicodedata
                            #try: 
                            #    name = unicodedata.name(unichr(i[0][0]))
                            #except ValueError:
                            #    name = '(unknown)' # narrow python unicode WARNING!
                            name = None
                            
                            nL.append((i[0][0], name))
                            
                    nD['see also'] = nL
                
                elif k == 'DECOMPOSITION':
                    # [[[6919, 6965]]]
                    #assert len(L)==1 and len(L[0])==1 and isinstance(L[0][0][0], int), L
                    nD['decomposed form'] = self.get_mapping(L)
                
                elif k == 'COMPAT_MAPPING':
                    # [[u'super', [50]]] or [[[32, 769]]] or 
                    # [[u'03BC greek small letter mu']]
                    # or [[u'fraction', [51, 8260, 52]]] (from "\t# <fraction>...")
                    nD['compatibility mapping'] = self.get_mapping(L)
                    
                elif k == 'NOTICE_LINE':
                    # [[u'* from ISO 2047']]; "*" indicates a dotpoint
                    # usually indicates notes on ISO standards etc
                    assert all(len(i)==1 and isinstance(i[0], basestring) for i in L)
                    nD['technical notice'] = [i[0] for i in L]
                
                elif k == 'COMMENT_LINE':
                    # NOTE: Can have codepoint links anywhere in the text
                    # * indicates a dotpoint
                    # [[u'* archaic phonetic for palatalized alveolar or dental stop'], 
                    # [u'* recommended spelling 0074 02B2']]
                    assert all(len(i)==1 and isinstance(i[0], basestring) for i in L)
                    nD['comments'] = '\n'.join([i[0] for i in L])
                
                else:
                    print 'CHAR_ENTRY warning:', k, L
        
            yield 'character', nD
            
    def get_mapping(self, L):
        # Returns [[a list of integer codepoints (guaranteed),
        #           type of the variant form (e.g. <fraction>, <circle> 
        #           if a circled character is pointing to an 
        #           uncircled character) or `None`,
        #           the names of the characters or `None`
        
        nL = []
        for i in L:
            #print i
            assert len(i) in (1, 2)
            
            if len(i) == 2:
                typ, LOrd = i
                assert isinstance(typ, basestring)
                assert not ' ' in typ
                nL.append((LOrd, typ, None))
            
            elif len(i) == 1:
                x = i[0]
                if isinstance(x, basestring):
                    codepoint, sep, value = x.partition(' ')
                    codepoint = convert(codepoint)
                    assert isinstance(codepoint, int), codepoint
                    nL.append(([codepoint], None, value))
                    
                elif isinstance(x, list):
                    assert(all(isinstance(j, (int, long)) for j in x))
                    nL.append((x, None, None))
                    
        return nL


def longest(L):
    nL = []
    LRtn = []
    for i in L:
        if isinstance(i, basestring):
            nL.append(i)
        else:
            if nL:
                LRtn.append(' '.join(nL))
                nL = []
            LRtn.append(i)
    
    if nL:
        LRtn.append(' '.join(nL))
    return LRtn


def convert(i):
    try: 
        if (not i.isupper() and not i.isdigit()) or len(i) not in (4, 5, 6):
            raise Exception
        
        return int(i, 16)
    except: 
        return i


def convert_hex(L):
    nL = []
    for i in L:
        if ' ' in i or True:
            i_nL = [convert(j) for j in i.split(' ')]
            
            if all(isinstance(j, (int, long)) for j in i_nL):
                nL.append(i_nL)
            else:
                #nL.append(longest(i_nL))
                nL.append(i)
        else:
            nL.append(convert(i))
    return nL


if __name__ == '__main__':
    for mode, D in NamesList(r'D:\Documents\Uni_\Uni\6.0.0\NamesList.txt'):
        print mode, D
        