from char_data.toolkit.arrays import get_uni_array, get_int_array
from char_data.misc import get_char_gaps, iter_ranges
from char_data.toolkit.arrays import write_array, write_json
from char_data.data_processors.internal.data_types.write.range_gen_tools import compress_ord_ranges


def write_sentence_data(f, key, DOrds):
    """
    Names [UnicodeData (single), NamesList (multiple)]
      LWordLinks separated by 1 to allow multiple names,
      Ended by a 0 [LWordLinks+=2 to compensate]
    References each word by a unsigned short (65535 max dictionary words)
    Variables: LSeek[+1; 0 means "no link/value for this codepoint"] -> 
               LWordLinks[+2] -> 
               LWords[\v terminated]
    """
    LSeek = get_int_array() # [+1]
    LAmount = get_int_array()
    LWordLinks = get_int_array() # [+2]
    LWords = get_uni_array()
    
    LRanges, DOrds = compress_ord_ranges(DOrds) # MASSIVE SPACE WASTAGE WARNING! ==================================
    LIgnoreRanges = get_char_gaps(DOrds)
    
    DWords = {}
    def get_word_seek(word):
        if not word in DWords:
            # Add the word and seek info 
            # if the word not in DWords
            seek = len(LWords)
            amount = LWords.extend(word)

            DWords[word] = (seek, amount)
        return DWords[word]
    
    DWordLinks = {}
    def get_wordlinks_seek(value):
        # This requires a list type to allow multiple 
        # definitions, so if it isn't convert it to one
        if not type(value) in (list, tuple):
            value = [value]
        value = tuple(value)
        
        if value in DWordLinks:
            return DWordLinks[value]
        
        # Process each definition seperately
        i_LWords = [i.split() for i in value]
        wordlinks_seek = len(LWordLinks)
        
        i = 1
        for LSentence in i_LWords:
            for word in LSentence:
                # Append to LWordLinks[+2]
                seek, amount = get_word_seek(word)
                LWordLinks.append(seek+2)
                LAmount.append(amount)
                
            if i != len(i_LWords):
                # 1 signifies multiple names
                # Only happens if not the last item
                LWordLinks.append(1)
                LAmount.append(0)
            i += 1
        
        # 0 signifies the end of sequence
        LWordLinks.append(0)
        LAmount.append(0)
        
        # Store for next time
        DWordLinks[value] = wordlinks_seek
        return wordlinks_seek
    
    if DOrds:
        for ord_ in iter_ranges(LIgnoreRanges, max(DOrds)):
            if ord_ in DOrds:
                #print 'CODEPOINT FOUND:', ord_
                seek = get_wordlinks_seek(DOrds[ord_])
                LSeek.append(seek+1)
            else:
                LSeek.append(0)
    
    # Make the values in the LRanges to point 
    # to seek positions as well to save space
    LRanges = [(from_, to, get_wordlinks_seek(value)) for from_, to, value in LRanges]
    
    # Write to disk
    DRtn = {}
    DRtn['LSeek'] = write_array(f, LSeek)
    DRtn['LWordLinks'] = write_array(f, LWordLinks)
    DRtn['LAmount'] = write_array(f, LAmount)
    DRtn['LWords'] = write_array(f, LWords)
    DRtn['LIgnoreRanges'] = write_json(f, LIgnoreRanges)
    DRtn['LRanges'] = write_json(f, LRanges)
    return DRtn
    