# -*- coding: utf-8 -*-

cangjie = u'''A	日 sun	
B	月 moon	
C	金 gold	
D	木 wood	
E	水 water	
F	火 fire	
G	土 earth	
H	竹 bamboo	The slant and short slant, the Kangxi radical 竹
I	戈 weapon	The dot
J	十 ten	The cross shape
K	大 big	The X shape
L	中 centre	The vertical stroke
M	一 one	The horizontal stroke
N	弓 bow	The crossbow and the hook
O	人 person	The dismemberment, the Kangxi radical 人
P	心 heart	The Kangxi radical 心
Q	手 hand	The Kangxi radical 手
R	口 mouth	The Kangxi radical 口
S	尸 corpse	Three-sided enclosure with an opening on the side
T	廿 twenty	Two vertical strokes connected by a horizontal stroke; the Kangxi radical 艸 when written as 艹 (whether the horizontal stroke is connected or broken)
U	山 mountain	Three-sided enclosure with an opening on the top
V	女 woman	A hook to the right, a V shape
W	田 field	Four-sided enclosure
Y	卜 fortune telling	The 卜 shape and rotated forms
X	重/難 collision/difficult	(1) disambiguation of Cangjie code decomposition collisions, (2) code for a "difficult-to-decompose" part
Z	(See note)	Auxiliary code used for entering special characters'''


def get_D_cangjie():
    D = {}
    for line in cangjie.split('\n'):
        letter, middle, description = line.split('\t')
        
        hanzi = middle[0].strip() # WARNING! ===========================================================
        english = middle[2:].strip()
        letter = letter.strip()
        middle = middle.strip()
        description = description.strip()
        
        D[letter] = [hanzi, english, description]
    return D


DCangjie = get_D_cangjie()
