# -*- coding: utf-8 -*-

_KANGXI_DATA = '''
1 3 丶 dot
1 6 亅 hook
1 2 丨 line
1 1 一 one
1 5 乙乚 second
1 4 丿 slash
2 29 又 again
2 27 厂 cliff
2 14 冖 cover
2 25 卜 divination
2 13 冂 down box
2 12 八 eight
2 11 入 enter
2 23 匸 hiding enclosure
2 15 冫 ice
2 18 刀刂 knife
2 10 儿 legs
2 8 亠 lid
2 9 人亻 man
2 17 凵 open box
2 19 力 power
2 28 厶 private
2 22 匚 right open box
2 26 卩 seal
2 149' 讠 speech (standing)
2 21 匕 spoon
2 16 几 table
2 24 十 ten
2 7 二 two
2 162 辶⻌⻍ walk
2 20 勹 wrap
3 37 大 big
3 57 弓 bow
3 59 彡 bristle
3 39 子 child
3 163 阝 city
3 44 尸 corpse
3 94 犭 dog
3 53 广 dotted cliff
3 51 干 dry
3 32 土 earth
3 184' 饣 eat (standing)
3 31 囗 enclosure
3 36 夕 evening
3 183' 飞 fly
3 169' 门 gate
3 34 夂 go
3 35 夊 go slowly
3 140 艹 grass
3 64 扌 hand
3 61 忄 heart
3 187' 马 horse
3 41 寸 inch
3 43 尢 lame
3 54 廴 long stride
3 170 阝 mound
3 46 山 mountain
3 30 口 mouth
3 49 己已巳 oneself
3 47 巛川 river
3 40 宀 roof
3 33 士 scholar
3 56 弋 shoot
3 52 幺 short thread
3 120' 纟 silk (standing)
3 42 小 small
3 58 彐彑 snout
3 45 屮 sprout
3 60 彳 step
3 50 巾 turban
3 55 廾 two hands
3 85 氵 water
3 38 女 woman
3 48 工 work
4 69 斤 axe
4 65 支 branch
4 159' 车 cart
4 83 氏 clan
4 87 爪爫 claw
4 81 比 compare
4 93 牛 cow
4 78 歹 death
4 68 斗 dipper
4 80 毋 do not
4 94 犬 dog
4 63 戶 door
4 89 爻 double x
4 92 牙 fang
4 88 父 father
4 86 火灬 fire
4 82 毛 fur
4 62 戈 halberd
4 90 爿 half tree trunk
4 90' 丬 half tree trunk
4 64 手 hand
4 61 心 heart
4 96 王 jade
4 76 欠 lack
4 130 月 meat (standing)
4 74 月 moon
4 71 无 not
4 66 攴攵 rap
4 73 曰 say
4 67 文 script
4 147' 见 see
4 154' 贝 shell
4 91 片 slice
4 113 礻 spirit
4 70 方 square
4 84 气 steam
4 77 止 stop
4 72 日 sun
4 178' 韦 tanned leather
4 141 虍 tiger
4 75 木 tree
4 162 辶 walk
4 85 水 water
4 79 殳 weapon
4 182' 风 wind
5 111 矢 arrow
5 196' 鸟 bird
5 103 疋 bolt of cloth
5 116 穴 cave
5 78 歺 death
5 108 皿 dish
5 80 母 do not
5 105 癶 dotted tent
5 212' 龙 dragon
5 109 目 eye
5 102 田 field
5 167' 钅 gold (standing)
5 115 禾 grain
5 96 玉 jade
5 100 生 life
5 168' 长 long
5 97 瓜 melon
5 122 罒 net
5 71 旡 not
5 95 玄 profound
5 104 疒 sickness
5 107 皮 skin
5 110 矛 spear
5 113 示 spirit
5 117 立 stand
5 112 石 stone
5 99 甘 sweet
5 98 瓦 tile
5 114 禸 track
5 101 用 use
5 85 氺 water
5 106 白 white
6 126 而 and
6 133 至 arrive
6 118 竹 bamboo
6 143 血 blood
6 137 舟 boat
6 129 聿 brush
6 145 衣 clothes
6 145 衤 clothes
6 139 色 color
6 128 耳 ear
6 210' 齐 even
6 124 羽 feather
6 140 艸 grass
6 142 虫 insect
6 121 缶 jar
6 181' 页 leaf
6 130 肉 meat
6 131 臣 minister
6 134 臼 mortar
6 122 网 net
6 125 老耂 old
6 136 舛 oppose
6 127 耒 plow
6 119 米 rice
6 132 自 self
6 123 羊 sheep
6 120 糸 silk
6 120 糹 silk (standing)
6 138 艮 stopping
6 135 舌 tongue
6 144 行 walk enclosure
6 146 襾西覀 west
7 153 豸 badger
7 151 豆 bean
7 160 辛 bitter
7 158 身 body
7 159 車 cart
7 163 邑 city
7 165 釆 distinguish
7 157 足 foot
7 148 角 horn
7 161 辰 morning
7 152 豕 pig
7 155 赤 red
7 156 走 run
7 147 見 see
7 154 貝 shell
7 149 言 speech
7 149 訁 speech (standing)
7 213' 龟 turtle
7 150 谷 valley
7 166 里 village
7 162 辵 walk
7 164 酉 wine
8 174 靑青 blue
8 210 斉 even
8 195' 鱼 fish
8 169 門 gate
8 167 金 gold
8 167 釒 gold (standing)
8 168 長 long
8 168 镸 long (standing)
8 170 阜 mound
8 173 雨 rain
8 172 隹 short tailed bird
8 171 隶 slave
8 211' 齿 tooth
8 175 非 wrong
9 184 食 eat
9 184 飠 eat (standing)
9 176 面 face
9 183 飛 fly
9 186 香 fragrant
9 185 首 head
9 181 頁 leaf
9 177 革 leather
9 179 韭 leek
9 180 音 sound
9 178 韋 tanned leather
9 182 風 wind
10 188 骨 bone
10 193 鬲 cauldron
10 212 竜 dragon
10 191 鬥 fight
10 194 鬼 ghost
10 190 髟 hair
10 187 馬 horse
10 192 鬯 sacrificial wine
10 189 高 tall
11 196 鳥 bird
11 198 鹿 deer
11 195 魚 fish
11 200 麻 hemp
11 197 鹵 salt
11 213 亀 turtle
11 199 麥 wheat
11 199' 麦 wheat
12 203 黑 black
12 204 黹 embroidery
12 202 黍 millet
12 211 歯 tooth
12 201 黃 yellow
13 207 鼓 drum
13 205 黽 frog
13 205' 黾 frog
13 208 鼠 rat
13 206 鼎 tripod
14 210 齊 even
14 209 鼻 nose
15 211 齒 tooth
16 212 龍 dragon
16 213 龜 turtle
17 214 龠 flute

11 197' 卤 salt
11 162' ⻌ walk
11 201' 黃 yellow
'''.strip()
