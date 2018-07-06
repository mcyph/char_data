import codecs
from toolkit.encodings.DIPA import DIPA
from toolkit.list_operations.rem_dupes import rem_dupes


def get_D_sup_scripts(DScripts, DBlockSubNames):
    # First of all, get a mapping from {Script: {SubScript: {}}}
    # This sounds like a chicken-and-egg problem!
    
    # Get a mapping from {Script: {Char: None}}
    DScriptChars = {}
    for Range in DScripts:
        ScriptName = DScripts[Range].strip()
        #if ScriptName not in ('Common', 'Inherited'): continue # HACK!
        print 'SCRIPT:', ScriptName
        
        if type(Range) in (list, tuple):
            FromRange, ToRange = Range
        else:
            FromRange, ToRange = Range, Range

        if ToRange-FromRange > 1000:
            continue # HACK!
        
        for i in xrange(FromRange, ToRange+1):
            if not ScriptName in DScriptChars:
                DScriptChars[ScriptName] = {}
            DScriptChars[ScriptName][i] = None
    
    # Get a mapping from {BlockName: {Char: None}}
    DBlockChars = {}
    for BlockRange in DBlockSubNames:
        BlockName = DBlockSubNames[BlockRange].strip()
        if type(BlockRange) in (list, tuple):
            FromRange, ToRange = BlockRange
        else:
            FromRange, ToRange = BlockRange, BlockRange

        if ToRange-FromRange > 1000:
            continue # HACK!
        
        for i in xrange(FromRange, ToRange+1):
            if not BlockName in DBlockChars:
                DBlockChars[BlockName] = {}
            DBlockChars[BlockName][i] = None
    
    # Get a mapping from {Script: {Block: [Char, ...]}}
    DMap = {}
    for ScriptName in DScriptChars:
        for BlockName in DBlockChars:
            for Char in DBlockChars[BlockName]:
                if Char in DScriptChars[ScriptName]:
                    if not ScriptName in DMap:
                        DMap[ScriptName] = {}
                    D = DMap[ScriptName]

                    if not BlockName in D:
                        D[BlockName] = []
                    D[BlockName].append(Char)
    
    # TODO: Convert chars to compressed ranges!
    #nDMap = {}
    
    # Add extra symbol mappings from Common, Inherited, 
    # combining ranges and manual codepoints/ranges and
    # adding the phonetic characters from mscIPA
    # TODO: SORT ME!
    DRtn = {}
    cScript = None
    import os
    os.chdir(r'E:\Dev\Flazzle') # HACK! ---------------------------------------------------------
    print os.getcwdu()
    File = codecs.open('Chars/Import/SupScripts.txt', 'rb', 'utf-8')

    for Line in File:
        if not Line.strip():
            continue
        else:
            From, To = Line.split('\t')

        From, To = From.strip(), To.strip()
        if not To: 
            # Script name specified, e.g. "Common" or "Basic Latin"
            cScript = From
            continue
        
        print 'FROM:', From, 'TO:', To, 'cSCRIPT:', cScript
        if cScript in ('Common', 'Inherited'):
            # Iterate through the script mappings in 
            # DSubBlocks and use alternative mappings
            print DMap[cScript].keys()

            BlockSubName = From
            if BlockSubName[0] == '*':
                continue

            for iRange in DMap[cScript][BlockSubName]:
                if not To in DRtn:
                    DRtn[To] = []
                DRtn[To].append(iRange)
        else:
            # Add custom mappings
            iRange = From
            if '-' in iRange: 
                iRange = int(iRange.split('-')[0].replace('U+', ''), 16), \
                         int(iRange.split('-')[1].replace('U+', ''), 16)
            else:
                iRange = int(iRange.replace('U+', ''), 16)
            
            if not To in DRtn:
                DRtn[To] = []
            DRtn[To].append(iRange)
    
    # Add phonetic IPA mappings
    DRtn['IPA Alphabet'] = []

    for k in DIPA:
        DRtn['IPA Alphabet'].extend([ord(i) for i in DIPA[k] if i.strip()])

    for c in 'abcdefghijklmnopqrstuvwxyz':
        DRtn['IPA Alphabet'].append(ord(c))

    DRtn['IPA Alphabet'] = rem_dupes(DRtn['IPA Alphabet'])
    return DRtn
