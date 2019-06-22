"""
NOTE: This was based off Unicode 6.0.0
http://www.unicode.org/Public/6.0.0/ucd/NamesList.html

Please keep me up to date, and update with differences at 
http://www.unicode.org/Public/UNIDATA/NamesList.html
using a diff tool when the above file changes!
"""

def or_(*L):
    r = '(?:%s)' % '|'.join(['(?:%s)' % i for i in L])
    #print L, r
    return r

#===================================================================#
#                  1.4 NamesList File Primitives                    #
#===================================================================#

# Added for python/REs
LPARAN = r'\('
RPARAN = r'\)'
RESERVED_TYPE = '([^<>]+)' # HACK! ===================================
ASTERISK = r'\*'
PLUS = r'\+'

NAME = '([A-Z0-9 -]+)'
# <sequence of uppercase ASCII letters, digits, space and hyphen> 
LCNAME = '([a-z0-9B -]+)' # HACK: Note the added "B" to make "<noBreak>" work! ====================
# <sequence of lowercase ASCII letters, digits space and hyphen>
# LCNAME "-" CHAR              <- WHAT DOES THIS MEAN?

LCTAG = '([a-zB]+)' # HACK!
# <sequence of lowercase ASCII letters>
STRING = '(.+)' # WARNING - NOT STRICTLY CORRECT!
# <sequence of Latin-1 characters, except controls> 
LABEL = '([^()]+)' # WARNING!
# <sequence of Latin-1 characters, except controls, "(" or ")"> 
CHAR = r'([0-9A-F]{4,6})'
#          X X X X
#        | X X X X X 
#        | X X X X X X 
#X:          "0"|"1"|"2"|"3"|"4"|"5"|"6"|"7"|"8"|"9"|"A"|"B"|"C"|"D"|"E"|"F" 
ESC = "\\\\"
ESC_CHAR = ESC+CHAR    
            # Special semantics of backslash (\) are supported
            # only in EXPAND_LINE.
TAB = r'\t+'
# <sequence of one or more ASCII tab characters 0x09>    
SP = r' '
# <ASCII 20>
LF = r'(?:\r\n|\n|\r)'
# <any sequence of ASCII 0A and 0D>

LINE = STRING+LF
COMMENT_1 = LPARAN+LABEL+RPARAN
COMMENT_2 = LPARAN+LABEL+RPARAN+SP+ASTERISK
COMMENT_3 = ASTERISK
COMMENT = or_(COMMENT_1, COMMENT_2, COMMENT_3)

#===================================================================#
#                   1.3 NamesList File Elements                     #
#===================================================================#

# EXPAND_LINE
EXPAND_LINE = or_(ESC_CHAR, CHAR, STRING, ESC) + LF
            # Instances of CHAR (see Notes) are replaced by 
            # CHAR NBSP x NBSP where x is the single Unicode
            # character corresponding to CHAR.
            # If character is combining, it is replaced with
            # CHAR NBSP <circ> x NBSP where <circ> is the 
            # dotted circle

# NAME_LINE
NAME_LINE1 = CHAR+TAB+NAME+LF
            # The CHAR and the corresponding image are echoed, 
            # followed by the name as given in NAME
NAME_LINE_CONTROL = CHAR+TAB+"<"+LCNAME+">"+LF
            # Control and noncharacters use this form of                                    
            # lowercase, bracketed pseudo character name
NAME_LINE_COMMENT = CHAR+TAB+NAME+SP+COMMENT+LF
            # Names may have a comment, which is stripped off
            # unless the file is parsed for an ISO style list
NAME_LINE_CONTROL_COMMENT = CHAR+TAB+"<"+LCNAME+">"+SP+COMMENT+LF
            # Control and noncharacters may also have comments
NAME_LINE = or_(
    NAME_LINE1,
    NAME_LINE_CONTROL,
    NAME_LINE_COMMENT,
    NAME_LINE_CONTROL_COMMENT
)

# RESERVED_LINE
RESERVED_LINE = CHAR+TAB+"<"+RESERVED_TYPE+">"+LF
            # The CHAR is echoed followed by an icon for the
            # reserved character and a fixed string e.g. "<reserved>"

# COMMENT_LINE
COMMENT_LINE_1 = TAB+ASTERISK+SP+EXPAND_LINE # WILL ALWAYS BE IGNORED! ================================
            # * is replaced by BULLET, output line as comment
COMMENT_LINE_2 = TAB+EXPAND_LINE # NOTE ME! ==================================================
            # Output line as comment
COMMENT_LINE_3 = TAB+ASTERISK+SP+STRING+CHAR+LF # ADDED TO HANDLE COMMENT LINKS! ===========================
COMMENT_LINE = or_(
    #COMMENT_LINE_3,
    COMMENT_LINE_2,
    COMMENT_LINE_1
)
print(COMMENT_LINE)

# ALIAS_LINE
ALIAS_LINE = TAB+"="+SP+LINE    
            # Replace = by itself, output line as alias

# FORMALALIAS_LINE
FORMALALIAS_LINE = TAB+"%"+SP+NAME+LF    
            # Replace % by U+203B, output line as formal alias

# CROSS_REF
CROSS_REF_1 = TAB+"x"+SP+CHAR+SP+LCNAME+LF    
CROSS_REF_CONTROL = TAB+"x"+SP+CHAR+SP+"<"+LCNAME+">"+LF
            # x is replaced by a right arrow
CROSS_REF_PARANS = TAB+"x"+SP+LPARAN+LCNAME+SP+"-"+SP+CHAR+RPARAN+LF    
CROSS_REF_PARANS_CONTROL = TAB+"x"+SP+LPARAN+"<"+LCNAME+">"+SP+"-"+SP+CHAR+RPARAN+LF    
            # x is replaced by a right arrow;
            # (second type as used for control and noncharacters)

            # In the forms with parens the LPARAN,"-" and RPARAN are removed
            # and the order of CHAR and STRING is reversed;
            # i.e. all inputs result in the same order of output
CROSS_REF_IDEOGRAPHS = TAB+"x"+SP+CHAR+LF
            # x is replaced by a right arrow
            # (this type is the only one without LCNAME 
            # and is used for ideographs)
CROSS_REF = or_(
    CROSS_REF_1,
    CROSS_REF_CONTROL,
    CROSS_REF_PARANS,
    CROSS_REF_PARANS_CONTROL,
    CROSS_REF_IDEOGRAPHS
)

FILE_COMMENT = ";"+LINE 
EMPTY_LINE = LF            
            # Empty and ignored lines as well as 
            # file comments are ignored

IGNORED_LINE = TAB+";"+EXPAND_LINE
            # Skip ';' character, ignore text

SIDEBAR_LINE = ";;"+LINE
            # Skip ';;' characters, output line
            # as marginal note

DECOMPOSITION = TAB+":"+SP+EXPAND_LINE    
            # Replace ':' by EQUIV, expand line into 
            # decomposition 

# COMPAT_MAPPING
COMPAT_MAPPING_1 = TAB+"#"+SP+EXPAND_LINE    
COMPAT_MAPPING_2 = TAB+"#"+SP+"<"+LCTAG+">"+SP+EXPAND_LINE    
            # Replace '#' by APPROX, output line as mapping;
            # check the <tag> for balanced < >
COMPAT_MAPPING = or_(
    COMPAT_MAPPING_2,
    COMPAT_MAPPING_1
)

# NOTICE_LINE
NOTICE_LINE_1 = "@"+PLUS+TAB+LINE        
            # Skip '@+', output text as notice
NOTICE_LINE_BULLET = "@"+PLUS+TAB+ASTERISK+SP+LINE # WARNING: THIS WILL NEVER BE REACHED! =============
            # Skip '@', output text as notice
            # "*" expands to a bullet character
            # Notices following a character code apply to the
            # character and are indented. Notices not following
            # a character code apply to the page/block/column 
            # and are italicized, but not indented
NOTICE_LINE = or_(NOTICE_LINE_1, 
                  NOTICE_LINE_BULLET)

SUBTITLE = "@@@"+PLUS+TAB+LINE    
            # Skip "@@@+", output text as subtitle

SUBHEADER = "@"+TAB+LINE    
            # Skip '@', output line as text as column header

# BLOCKNAME
BLOCKNAME_1 = LABEL
BLOCKNAME_2 = LABEL+SP+LPARAN+LABEL+RPARAN            
            # If an alternate label is present it replaces 
            # the blockname when an ISO-style namelist is
            # laid out; it is ignored in the Unicode charts
BLOCKNAME = or_(
    BLOCKNAME_1,
    BLOCKNAME_2
)

BLOCKSTART = CHAR    # First character position in block
BLOCKEND = CHAR    # Last character position in block

BLOCKHEADER = "@@"+TAB+BLOCKSTART+TAB+BLOCKNAME+TAB+BLOCKEND+LF
            # Skip "@@", cause a page break and optional
            # blank page, then output one or more charts
            # followed by the list of character names. 
            # Use BLOCKSTART and BLOCKEND to define
            # what characters belong to a block.
            # Use blockname in page and table headers

PAGE_BREAK = "@@"    # Insert a (column) break
INDEX_TAB = "@@"+PLUS    # Start a new index tab at latest BLOCKSTART

TITLE = "@@@"+TAB+LINE    
            # Skip "@@@", output line as text
            # Title is used in page headers


#CHAR_ENTRY = '(?:(?:%s)|(?:%s))' % (NAME_LINE, RESERVED_LINE) # HACK!
