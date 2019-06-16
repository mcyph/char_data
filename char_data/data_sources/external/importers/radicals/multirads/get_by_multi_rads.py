# -*- coding: utf-8 -*-

# 一夂刀斉刈而鼠馬气化香力匚毛尤言身鼎犯｜癶水買戈方尸麻示羽疋皿血立齊母行ハ舌金青
# 囗鬯忙日飛魚川食非止工士韭黹耒凵穴豸勿亀冂禹缶冊二小匕五冖舛艮舟無亠鬥走音風髟犬
# 耳色攵谷厶爻爿禾十聿乃黄片釆酉手及免里彑竹角麦高牛瓜也彡衣矢入卩ヨ火自韋屯曰米已
# 廴用歹糸見广巾頁爪亅雨文門肉月王牙厂井斗世甘辛尚貝亡欠尢木冫个革臣竜田殳鬲鬼丶隹
# 礼品心羊奄无毋父黍扎子氏戸巛卜口鳥赤瓦鼓屮杰石干并勹夕幺黽虫艾老宀玄弋首矛弓疔初
# 土阡龠斤大邦豆女支皮辰生隶鼻人岡込儿滴汁元面久又車虍至ノ鹿黒豕比乙九マ几ユ巨足歯目
# 山彳鹵巴長骨寸白臼西廾


def get_by_multi_rads(LRads, Trad):
    xx = 0
    DRads = DBothRads
    DPossible = {}
    for iRad in LRads:
        # print('iRad:', iRad.encode('utf-8'))
        # Only append if either the first radical or already
        # found by previous radicals to filter down to only
        # characters with those multirads
        nDPossible = {}
        for SearchForRad in iRad:
            if SearchForRad in DRads:
                for AppendChar in DRads[SearchForRad]:
                    # print('AppendChar:', AppendChar.encode('utf-8'))
                    if (xx == 0) or (AppendChar in DPossible):
                        nDPossible[AppendChar] = None
        DPossible = nDPossible
        xx += 1

    # HACK: Add z-variants
    # NOT RECOMMENDED as 變 is shown under 亠
    if False:
        for Char in tuple(DPossible.keys()):
            LZVariant = char_data.raw_data('unihan.zvariant', Char)
            if LZVariant:
                for Variant in LZVariant:
                    DPossible[Variant] = None
    LRtn = list(DPossible.keys())
    LRtn.sort()
    return LRtn
