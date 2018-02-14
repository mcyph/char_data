from char_data.CharData import CharData
from char_data.ranges.IterRanges import iter_ranges

def get_D_scripts():
    DScripts = {}
    
    for line in script_types.split('\n'): # from Data/ScriptTypes.txt
        line = line.strip()
        if not line: 
            continue
        
        try: 
            script, mapping = line.replace('    ', '\t').split('\t')
        except: 
            print "ERROR ON LINE:", line.encode('utf-8')
            raise
        
        if not mapping in DScripts:
            DScripts[mapping] = []
        DScripts[mapping].append(script)
    
    return DScripts
DScripts = get_D_scripts()

def get_script_subranges(typ):
    # 
    range = CharData.search('General Scripts', typ)
    del_font_script, LRanges = iter_ranges(range)
    
    LRtn = []
    for i_type, value in LRanges:
        if i_type == 'Block':
            LRtn.append(value)
    
    if typ=='Common' or typ=='Inherited': 
        LRtn.sort()
    return (typ, LRtn)

def get_L_scripts():
    # Add by script region, e.g. "Middle East"
    #LScripts = sorted(DScripts.keys())
    SUsedScripts = set()
    
    LRtn = []
    for region in LScriptOrder: # from ScriptOrder.txt
        if not region in DScripts: 
            continue
        
        DScripts[region].sort()
        
        LSubRanges = []
        for script in DScripts[region]:
            LSubRanges.append(get_script_subranges(script))
            SUsedScripts.add(script)
        
        #print 'LAPPEND:', LAppend
        LRtn.append((region, LSubRanges))
    
    LScripts = CharData.MultiIndex.property_keys('General Scripts')
    print 'SCRIPTS:', LScripts
    
    for script in LScripts:
        if not script in SUsedScripts: 
            print 'SCRIPT UNUSED WARNING:', script.encode('utf-8')
    return LScripts
