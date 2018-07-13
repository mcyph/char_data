import re
from toolkit.py_ini import read_D_pyini

# NOTE: Kanjidic is listed before Unihan
# TODO: Fix busy people chapter "A"!
# TODO: Fix Morohashi in Kanjidic (Kanjidic2.py)! =====================================================


Indicies = '''dicref_henshall3    <page>
dicref_sakade    <page>
dicref_henshall    <page>
dicref_oneill_kk    <page>
dicref_gakken    <page>
dicref_busy_people    <volume>.<chapter>
dicref_jf_cards    <page>
dicref_oneill_names    <page><position:char:1:A?>
dicref_sh_kk    <page>
dicref_kanji_in_context    <page>
dicref_kodansha_compact    <page>
dicref_halpern_kkld    <page>
dicref_nelson_c    <page>
dicref_moro    <page><P:char:1:[P]?><X:char:1:[X]?>.<volume>.<volume page>
dicref_halpern_njecd    <page>
dicref_nelson_n    <page>
dicref_heisig    <page>
dicref_crowley    <page>
dicref_tutt_cards    <page>
dicref_maniette    <page>

CheungBauerIndex    <page:3>.<position:2>
CihaiT    <page>.<row:1><position:2>
Cowles    <page>
DaeJaweon    <page>.<character number:2><status:1>
FennIndex    <page>.<position>
GSR    <page:4><position:char:1:[A-z]?><offset:char:1:[']?>
HanYu    <volume number:1><page:4>.<character number:2><in dictionary:1>
HKGlyph    <page:4>
KangXi    <page>.<character number:2><status:1>
Karlgren    <page><interpolated:char:1:[\*A]?>
Lau    <page>
Matthews    <page>
MeyerWempe    <page><subsidiary:char:1:[A-z]?>
Morohashi    <page><simplified:char:1:[']?>
Nelson    <page>
SBGY    <page:3>.<position:2>'''


DIndicies = {}
for Line in Indicies.split('\n'):
    Line = Line.strip()
    if Line: 
        key, value = Line.split('    ')
        DIndicies[key] = value


def create_re_object(key):
    #print 'KEY:', key
    # Create the re_ object referenced by key
    o_key = key
    LRtn = []
    DTypes = {}
    
    format = DIndicies[key]
    LFormat = format.split('<')
    
    # Append and chop off the first item
    LRtn.append(LFormat[0].replace('.', '\\.'))
    LFormat = LFormat[1:]
    
    for i in LFormat:
        dict_format, extra = i.split('>')
        
        L = []
        colons = dict_format.count(':')
        
        if colons == 0:
            # Just the key as an integer
            L.append('(?P<%s>[0-9]+)' % dict_format.replace(' ', '_'))
            DTypes[dict_format] = 'integer'
        
        elif colons == 1:
            # key:len_ OR key:data_type
            key, len_ = dict_format.split(':')
            
            try: 
                len_ = int(len_)
                L.append('(?P<%s>.{%s})' % (key.replace(' ', '_'), len_))
                DTypes[key] = 'integer'
            except ValueError:
                L.append('(?P<%s>.+?)' % (key.replace(' ', '_')))
                DTypes[key] = len_
            
        elif colons == 2:
            # key:data_type:len_
            key, data_type, len_ = dict_format.split(':')
            len_ = int(len_)
            L.append('(?P<%s>.{%s})' % (key.replace(' ', '_'), len_))
            DTypes[key] = data_type
            
        elif colons == 3:
            # key:data_type:len_:range
            key, data_type, len_, range = dict_format.split(':')
            len_ = int(len_)
            
            if len_ == 1:
                L.append('(?P<%s>%s)' % (key.replace(' ', '_'), range))
            else: 
                L.append('(?P<%s>%s{%s})' % (key.replace(' ', '_'), range, len_))
            
            DTypes[key] = data_type
        
        LRtn.append(''.join(L))
        LRtn.append(extra.replace('.', '\\.'))
    
    re_ = ''.join(LRtn)
    re_ = '^%s$' % re_
    #print 'key:', o_key, 're_:', re_
    re_ = re.compile(re_, re.UNICODE)
    return DTypes, re_


DREs = {}
for key in DIndicies:
    DREs[key] = create_re_object(key)


def parse_indices(key, DOrds):
    # Split into multiple dictionaries as values
    D = {}
    LArrays = []
    DTypes, del_re = DREs[key]
    for i_key in DTypes:
        LArrays.append((i_key, DTypes[i_key]))
    
    for ord_ in DOrds:
        value = DOrds[ord_]
        #print key, ord_, value
        
        if isinstance(value, basestring):
            value = value.split() # Kanjidic multiple values - NOTE ME!
        
        assert isinstance(value, (list, tuple))
        
        D[ord_] = [convert(key, i) for i in value]
        #print 'key:', key, 'value:', value, 'D:', D[ord_]
    return LArrays, D


def convert(key, value):
    # Split value into a dictionary using that key's re_ object
    del_D_types, re_ = DREs[key]
    #try: print 'value:', value
    #except: print 'value:', value.encode('utf-8')
    
    # HACK: Chop the second onwards references
    o_val = value
    value = value.split()[0]
    if o_val != value: 
        print 'MultiVal warning:', key, o_val.encode('utf-8')
    
    match = re_.search(value)
    if not match: 
        print 'INDICE WARNING:', key, value.encode('utf-8')
        return {}
    else: 
        DRtn = {}
        D = match.groupdict(value)
        for k in D:
            DRtn[k.replace('_', ' ')] = D[k]
        return DRtn
