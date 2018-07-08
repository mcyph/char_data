from ListBase import ListBase


class ThreeLevelList(ListBase):
    def __init__(self, heading):
        self.heading = heading

    def get_L(self):
        pass

    def get_L_results(self, subheading):
        pass



class GeneralScriptList(ThreeLevelList):
    def get_L_script_subranges(self, typ):
        #
        range = CharData.search('General Scripts', typ)
        del_font_script, LRanges = iter_ranges(range)

        LRtn = []
        for i_type, value in LRanges:
            if i_type == 'Block':
                LRtn.append(value)

        if typ == 'Common' or typ == 'Inherited':
            LRtn.sort()
        return (typ, LRtn)
