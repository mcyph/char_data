from string import ascii_letters
from toolkit.encodings.surrogates import w_unichr

from .UnicodeSetUtils import (
    get_D_default_props, get_D_prop_aliases, get_D_values, get_D_props
)
from char_data.CharIndexes import char_indexes
# Get various property/value aliases etc
from .ProcessRangeBase import ProcessRangeBase

DProps = get_D_props()
DDefaultProps = get_D_default_props()
DPropAliases = get_D_prop_aliases()
DValues = get_D_values()

# Match types
#
# NOTE: OPERATOR works on all the items to the 
# left of the operator in the current group, 
# and only subtracts/intersects the *one* group 
# to the right of the operator.
#
# See: http://userguide.icu-project.org/strings/unicodeset
OPERATOR = 0 # (operator, (from, to))
RANGES = 1 # [(from, to), ...]
STRING = 2 # pattern

# Operator types
INTERSECT = 0 # A & B
DIFFERENCE = 1 # A - B
DOperators = {
    '-': DIFFERENCE,
    '&': INTERSECT
}

# TODO: 
# * SUPPORT [{abc}] FORMAT! ========================================================
# * SUPPORT '' AND ' blah ' FORMAT! ================================================
# * SUPPORT VARIABLES! =============================================================


def get_unicode_set_ranges(s, DVars=None):
    """
    Get the ICU UnicodeSet range tokens
    """
    return UnicodeSetParse(s, DVars).ranges


class UnicodeSetParse(ProcessRangeBase):
    def __init__(self, s, DVars=None):
        self.s = s
        self.DVars = DVars
        assert (s[0], s[-1]) == ('[', ']')
        self.ranges = self.get_ranges(s[1:-1])
        
    def get_ranges(self, s):
        x = 0
        LRtn = []
        
        backslash_mode = False
        cur_operator = None
        neg = False
        
        while 1:
            # Get the current char
            try: c = s[x]
            except: break
            #print 'GET_RANGES:', c
            
            if backslash_mode:
                if c in 'pP':
                    # perl-syntax!
                    x, neg, LRanges = self.process_perl(x, s)
                    LRtn.append((RANGES, neg, LRanges))
                    
                elif c == 'u':
                    # Unicode backslash
                    LRtn.append((STRING, w_unichr(int(s[x+1:x+5], 16))))
                    x += 4
                
                elif c == '\\':
                    # a literal backslash
                    LRtn.append((STRING, '\\'))
                
                backslash_mode = False
                
            elif c == '\\':
                # Activate backslash mode
                backslash_mode = True
            
            elif c == '{':
                # Extract a string
                x, str_ = self.process_curly_braces(x, s)
                LRtn.append((STRING, str_))
            
            elif s[x:x+2] == '[:':
                # A POSIX range
                x, neg, LRanges = self.process_posix(x, s)
                LRtn.append((RANGES, neg, LRanges))
            
            elif c == '[':
                # Embedded ranges
                # TODO: Fix PERL BACKSLASHES! =======================================
                x, range_text = self.process_range(x, s)
                assert (range_text[0], range_text[-1]) == ('[', ']')
                LRtn.append(self.get_ranges(range_text[1:-1]))
                
            elif c == ']':
                # Should never be a closing bracket here!
                raise Exception("']' without '['!")
            
            elif c in '-&':
                # Operators
                # - is difference
                # & is intersect
                cur_operator = c
                x += 1
                continue
            
            elif not x and c=='^':
                # Negative mode
                neg = True
            
            elif c=='$' and (x==len(s)-1):
                pass
                #FIXME # FIXME! ================================================
                
            elif c=='$' and self.DVars!=None:
                # Process `$variableName`
                y, name = self.process_variable(x, s)
                
                value = self.DVars[name]
                if isinstance(value, (tuple, list)):
                    value = ''.join(_[-1] for _ in value) # TYPE WARNING! ==========
                
                # Insert the variable, and reprocess
                #print 'BEFORE:', s, value
                s = s[:x]+value+s[y:]
                #print s, s[x]
                x -= 1
            
            elif c.strip():
                # Non-whitespace - add a single character as a string
                # OPEN ISSUE: Ignore whitespace??? ================================
                LRtn.append((STRING, c))
            
            else:
                # Whitespace - ignore it
                x += 1
                continue
            
            
            if not backslash_mode and cur_operator and len(LRtn)<2:
                # Allow initial "-" and "&" characters
                LRtn.append((STRING, cur_operator))
                cur_operator = None
                
            elif not backslash_mode and cur_operator:
                
                if LRtn[-1][0] in (RANGES, OPERATOR):
                    # A range difference etc, e.g. "[[a-e]-[c]]"
                    assert LRtn[-2][0] in (RANGES, OPERATOR)
                    LRtn.append((OPERATOR, (cur_operator, LRtn.pop())))
                else:
                    # an ordinary range, e.g. "[a-e]"
                    item2, item1 = LRtn.pop(), LRtn.pop()
                    
                    assert cur_operator == '-'
                    assert (item1[0], item2[0]) == (STRING, STRING), (item1, item2, self.s)
                    assert (len(item1[1]), len(item2[1])) == (1, 1)
                    
                    # Note the "FALSE!"
                    LRtn.append((RANGES, False, ((item1[1], item2[1]),)))
                
                cur_operator = None
            
            x += 1
        return (RANGES, neg, tuple(LRtn))
    
    #===============================================================#
    #                      Process Literals                         #
    #===============================================================#
    
    def process_quotes(self, x, s):
        """
        According to
        http://userguide.icu-project.org/strings/unicodeset,
        single quotes should escape, but I don't think that's was 
        the case when I was playing around with UnicodeSet in PyICU...
        """
        FIXME
    
    def process_curly_braces(self, x, s):
        """
        Characters inside curly braces/
        brackets ({...}) make a string
        """
        L = []
        backslash_mode = False
        x += 1
        
        while 1:
            # Get the current char
            try: c = s[x]
            except: break
            
            if backslash_mode and c == 'u':
                # A Unicode backslash
                L.append(
                    w_unichr(int(s[x+1:x+5], 16))
                )
                backslash_mode = False
                x += 4

            elif backslash_mode:
                L.append(c)
                backslash_mode = False
            
            elif c.strip():
                if c == '}':
                    break
                elif c == '\\':
                    backslash_mode = True
                else:
                    L.append(c)
            x += 1
        
        return x, ''.join(L)
    
    #===============================================================#
    #                      Process Variables                        #
    #===============================================================#
    
    def process_variable(self, x, s):
        """
        Get the `$variable_name`
        """
        SAllowed = set(ascii_letters+'_0123456789')
        
        L = []
        x += 1 # Skip the $
        while 1:
            # Get the current char
            try: c = s[x]
            except: break
            
            if c in SAllowed:
                L.append(c)
            else: 
                break
            x += 1
        return x, ''.join(L)
    
    #===============================================================#
    #                   Process Property-Values                     #
    #===============================================================#
    
    def process_posix(self, x, s):
        """
        Process posix-style:
        
        [:value:] (for Unicode General Category)
        
        Positive: [:type=value:]
        Negative: [:^type=value:]
        """
        LType = []
        LValue = []
        
        first_char = True
        neg = False
        value_found = False
        
        assert s[x:x+2] == '[:' # bloody well hope so!
        x += 2 # ignore the '[:'
        
        while 1:
            # Get the current char
            try: c = s[x]
            except: break
            
            if first_char and c=='^':
                neg = True
                
            elif not value_found:
                if c == '=':
                    value_found = True
                elif s[x:x+2] == ':]':
                    value = ''.join(LType).lower()
                    return x+1, neg, self.get_L_ranges(DDefaultProps[value])
                else:
                    LType.append(c)
            
            else:
                if s[x:x+2] == ':]':
                    break
                LValue.append(c)
            
            first_char = False
            x += 1
        
        typ = self.convert_type(''.join(LType))
        value = self.convert_value(typ, ''.join(LValue))
        LRanges = self.get_L_ranges([(typ, value)])
        return x+1, neg, LRanges
    
    def process_perl(self, x, s):
        """
        Process perl-style:
        
        \p{value} (for Unicode General Category)
        
        Positive: \p{type=value}
        Negative: \P{type=value}
        """
        LType = []
        LValue = []
        
        value_found = False
        first_char = True
        
        while 1:
            # Get the current char
            try: c = s[x]
            except: break
            
            if first_char:
                # p -> positive/P -> negative
                neg = {'p': False, 'P': True}[c]
                first_char = False
                
                # Skip the initial {
                assert s[x+1]=='{'
                x += 1
                
            elif not value_found:
                if c == '=':
                    value_found = True
                elif c == '}':
                    value = ''.join(LType).lower()
                    return x, neg, self.get_L_ranges(DDefaultProps[value])
                else:
                    LType.append(c)
                
            else:
                if c == '}':
                    break
                else:
                    LValue.append(c)
            
            x += 1
        
        # OPEN ISSUE: Convert the type
        typ = self.convert_type(''.join(LType))
        value = self.convert_value(typ, ''.join(LValue))
        LRanges = self.get_L_ranges([(typ, value)])
        return x, neg, LRanges
        
    def get_L_ranges(self, L):
        """
        """
        LRtn = []
        for typ, value in L:
            # FIXME: Don't allow searches by 
            # fulltext unless it's a direct match for 
            # name/conscript name/definitions etc! ===============================
            # (readings should allow partial matches I think)
            #print typ, value
            for i in char_indexes.search(typ, value):
                if isinstance(i, (list, tuple)):
                    from_, to = i
                    LRtn.append((w_unichr(from_), w_unichr(to)))
                else:
                    LRtn.append(w_unichr(i))
        return tuple(LRtn)
        
    def convert_type(self, typ):
        """
        Convert aliases to the original name and return 
        the associated Flazzle name (without underscores)
        """
        typ = typ.replace(' ', '_')
        typ = DPropAliases.get(typ.lower(), typ)
        typ = DProps[typ.lower()]
        return typ.replace('_', ' ')
    
    def convert_value(self, typ, value):
        if not typ in DValues:
            return value # WARNING! ==============================================
        return DValues[typ].get(str(value), value)


if __name__ == '__main__':
    for i in [
        '[^a-z]',
        '[abc123]',
        '[\p{Letter}]',
        '[[:latin:] \p{script=Latin}]',
        '[[a-c]-[b]]',
        r'[\u0300-\u0345]',
        '[{my\\ very\\ own\\ {s tring\\}}]'
    ]:
        print(i)
        from pprint import pprint
        pprint(get_unicode_set_ranges(i))
