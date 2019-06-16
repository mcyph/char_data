import gzip
from toolkit.escape import E, esc_word_disp
from lxml.etree import iterparse
from toolkit.encodings.surrogates import w_ord


SIgnored = set()
for i in (
    'misc',
    'query_code',
    'radical',
    'reading_meaning',
    'rmgroup',
    'header',
    'kanjidic2',
    'character',
    'codepoint',
    'dic_number'
):
    SIgnored.add(i)


def open_kanjidic_2(path):
    ext = path.split('.')[-1].lower()
    
    if ext == 'gz': 
        f = gzip.open(path)
    else: 
        f = file(path, 'rb')
    
    # get an iterable
    iter_ = iterparse(f, events=("end",))
    D = {}
    for event, elem in iter_:
        tag = elem.tag
        if tag == 'literal':
            # Yield the existing character and change it
            if elem.text:
                if D: yield D
                D = {'codepoint': w_ord(elem.text.strip())}
        
        elif tag in SIgnored:
            # Only children useful - ignored
            # But make sure it actually IS blank!
            if elem.keys() or (elem.text and elem.text.strip()):
                print('tag Ignore Warning:', tag, elem.keys(), elem.text)
        
        elif tag == 'database_version':
            # The Kanjidic database version
            # May as well print it
            print('Kanjidic2 DB Version:', elem.text)
            
        elif tag == 'date_of_creation':
            # Likewise
            print('Kanjidic2 Date of Creation:', elem.text)
            
        elif tag == 'file_version':
            # Likewise
            print('f Version:', elem.text)
        
        elif tag == 'cp_value':
            # Codepoint values can be easily grabbed by str.encode('utf-8') 
            # or str.encode('shift-jis') so I won't bother including them
            pass
            
        elif tag == 'dic_ref':
            # e.g. Morohashi references
            dic_ref_type = 'dicref_%s' % elem.get('dr_type')
            if not elem.text or not elem.text.strip():
                continue
            
            if not dic_ref_type in D:
                D[dic_ref_type] = []
            
            value = elem.text.strip()
            if dic_ref_type == 'dicref_moro':
                # HACK: Convert to a string - see also `dicref_moro` 
                # in the `Indicies` variable in `IndiceBuilder`
                value = '%s.%s.%s' % (value, 
                                      elem.get('m_vol', '0'), 
                                      elem.get('m_page', '0')) # HACK! ================================
            
            if dic_ref_type == 'dicref_busy_people':
                if value.endswith('.A'):
                    value = '%s.0' % (value[:-2]) # HACK! =============================================
            
            D[dic_ref_type].append(value)
        
        elif tag == 'freq':
            # Record the Japanese frequency
            if elem.text:
                if not 'freq' in D:
                    D['freq'] = []
                D['freq'].append(elem.text.strip())
                
        elif tag == 'grade':
            # Record the Japanese grade
            if elem.text:
                if not 'grade' in D:
                    D['grade'] = []
                D['grade'].append(elem.text.strip())
        
        elif tag == 'meaning':
            # WARNING: Specific meanings might be grouped with specific readings with rmgroup! ===========
            # I don't think Kanjidic differentiates between them *yet* though
            
            # Record the Japanese meaning
            if 'm_lang' in elem.keys():
                # In English
                key = 'meaning_%s' % elem.get('m_lang')
                
                if not key in D:
                    D[key] = []
                
                if elem.text:
                    D[key].append(elem.text.strip())
            else: 
                # In another language
                if not 'meaning' in D:
                    D['meaning'] = []
                
                if elem.text:
                    D['meaning'].append(elem.text.strip())
        
        elif tag == 'nanori':
            # Record the Japanese
            if not 'reading_nanori' in D:
                D['reading_nanori'] = []
            
            if elem.text:
                D['reading_nanori'].append(elem.text.strip())
            
        elif tag == 'q_code':
            # Input codes, e.g. SKIP and Four Corners
            # I've removed SKIP for now for licensing reasons
            query_code_type = elem.get('qc_type')
            
            if query_code_type == 'skip': 
                continue
            query_code_type = 'querycode_%s' % query_code_type
            
            if not query_code_type in D:
                D[query_code_type] = []
            
            if elem.text:
                D[query_code_type].append(elem.text.strip())
        
        elif tag == 'rad_name':
            # Record the radical's name (if the character used 
            # as a radical) in Japanese
            # TODO: This should be a StringData!
            if not 'rad_name' in D:
                D['rad_name'] = []
            
            if elem.text:
                D['rad_name'].append(elem.text)
        
        elif tag == 'rad_value':
            radical_type = elem.get('rad_type')
            key = 'rad_%s' % radical_type
            
            if not key in D:
                D[key] = []
            
            if elem.text:
                D[key].append(elem.text.strip())
        
        elif tag == 'reading':
            # The reading, e.g. pinyin/ja_on etc
            reading_type = 'reading_%s' % elem.get('r_type')
            
            if not reading_type in D:
                D[reading_type] = []
            
            if elem.text:
                D[reading_type].append(elem.text.strip())
        
        elif tag == 'stroke_count':
            # The total Japanese stroke count
            if elem.text:
                if not 'stroke_count' in D:
                    D['stroke_count'] = []
                D['stroke_count'].append(elem.text.strip())
            
        elif tag == 'variant':
            # Variant forms of this character
            key = 'crossref_%s' % elem.get('var_type')
            if elem.text:
                if not key in D:
                    D[key] = []
                D[key].append(elem.text.strip())

        elif tag == 'jlpt':
            # JLPT level
            if not 'jlpt' in D:
                D['jlpt'] = []

            D['jlpt'].append(int(elem.text.strip()))

        else:
            print('WARNING:', tag, elem)
    f.close()


if __name__ == '__main__':
    DKeys = {}
    len = 0
    for D in open_kanjidic_2(r'E:\Dev\Dictionaries\Asian\Japanese\Commercial\Kanjidic2\kanjidic2.xml'):
        print(D)
        for k in D:
            DKeys[k] = None
        len += 1
    
    LKeys = sorted(DKeys.keys())
    for key in LKeys:
        print(key)
    print()
    print('LEN:', len)
    