from toolkit.arrays.ArrayUtils import read_array, read_json
from char_data.datatypes.read import RangeClass

from char_data.importer.misc.char_utilities import get_adjusted_code_point
from char_data.datatypes.write import write_sentence_data
from char_data.datatypes.read.RangeClass import  NO_DATA


class SentenceData(RangeClass):
    writer = staticmethod(write_sentence_data)
    
    def __init__(self, key, f, DJSON):
        self.DJSON = DJSON
        self.key = key
        
        self.LRanges = read_json(f, DJSON['LRanges'])
        self.LIgnoreRanges = read_json(f, DJSON['LIgnoreRanges'])
        
        self.LSeek = read_array(f, DJSON['LSeek']) # [+1] # integer seek positions to LWordLinks
        self.LAmount = read_array(f, DJSON['LAmount'])
        self.LWordLinks = read_array(f, DJSON['LWordLinks']) # [+2] integer seek positions to LWords
        self.LWords = read_array(f, DJSON['LWords']) # [\v terminated] string/unicode array
        
        self.DWordLinkCache = {}
        
    def raw_data(self, ord_):
        seek = self.get_range_data(ord_)
        if seek != NO_DATA:
            return self.get_L_sentence(seek)
        
        ord_ = get_adjusted_code_point(ord_, self.LIgnoreRanges)
        if ord_ is None:
            # If the range cancelled, return None
            return None
        
        elif ord_ >= (len(self.LSeek)-1):
            # Prevent IndexErrors
            return None
        
        else:
            '''
            Returns a list of strings (e.g. definitions etc), one for 
            each definition associated with this codepoint. 
            
            Each word in each sentence stores seek positions individually 
            e.g. LWordLinks might be 
            [sentence 1 word 1 seek pos-2]
            [sentence 1 word 2 seek pos-2]
            [1 indicates next sentence]
            [sentence 2 word 1 seek pos-2]
            [0 indicates no more sentences]
            
            e.g. [tree][trees][1][forest][0]
            '''
            
            # If seek is 0 then there isn't a name for that character
            seek = self.LSeek[ord_]
            if seek == 0: 
                return None
            seek -= 1 # seek is [+1]
            return self.get_L_sentence(seek)
    
    def get_L_sentence(self, seek):
        # WordLinks has the indice of the word in LWords
        LRtn = [] # Contains all definitions
        LSentence = [] # The current sentence only
        
        while 1:
            word_link = self.LWordLinks[seek]
            if word_link == 0:
                # Ended by a 0 [LWordLinks+=2 to compensate]
                LRtn.append(' '.join(LSentence))
                break
            
            elif word_link == 1:
                # Separated by 1 to allow multiple names
                LRtn.append(' '.join(LSentence))
                LSentence = []
            
            else:
                # Otherwise, -2 and use it on LWords
                word_seek = word_link-2
                LSentence.append(self.get_word(word_seek, self.LAmount[seek]))
            seek += 1
            
        return tuple(LRtn)
    
    def get_word(self, seek, amount):
        return self.LWords[seek:seek+amount]
