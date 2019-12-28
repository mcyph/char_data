from dicts.chinese.variants import LinkDB
from dicts.misc.TextOut import w_word
from char_data.toolkit.list_operations.rem_dupes import fast_rem_dupes
from dicts.misc.ExpandTree import open, close

from dicts.chinese.variants.LinkDB import DNoDisp, DTypes


class HTMLLinks(LinkDB):
    def get_html_links(self, LWords, DFrom):
        DProcess = {}
        LHeader = []
        #print 'get_html_links:', ' '.join(LWords)
        
        for typ, opposite, LVariant in self.iter_variants(LWords):
            # Add any variants
            if not opposite in DNoDisp:
                LHeader.append(opposite)
            DProcess.setdefault(typ, []).append(LVariant)
            #print ' '.join(LVariant)
        LHeader = fast_rem_dupes(LHeader)
        
        for typ, LVariant in self.get_links(LWords):
            # Add any links
            DProcess.setdefault(typ, []).append(LVariant)
        LKeys = list(DProcess.keys())
        LKeys.sort(key=lambda x: x.lower())
        
        LHTML = []
        for key in LKeys:
            # Output as HTML
            types = DTypes.get(key, 'Both')
            if types == 'Both': 
                # TODO: Order me properly!
                LTypes = ['trad', 'simp']
            else: 
                LTypes = [types]
            
            LHTML.append(open('expand', text=key))
            LHTML.append('<ul style="margin-left: 8px">')
            DProcess[key] = fast_rem_dupes(DProcess[key]) # HACK!
            
            for LVariant in DProcess[key]:
                if LTypes == ['trad'] and not LVariant[1]:
                    continue
                elif LTypes == ['simp'] and not LVariant[0]:
                    continue
                    
                LHTML.append('<li>')
                for i_type in LTypes:
                    # OPEN ISSUE: Should Pinyin be output?
                    # TODO: Gray out the "other" type!
                    
                    if i_type == 'simp' and LVariant[0]:
                        LHTML.append('<a href="FIXME">%s</a> ' % w_word(DFrom, s=LVariant[0], 
                                                                        script='Simplified', 
                                                                        chars='cmn:eng', # What about Cantonese?
                                                                        show_snd=False, translit=False))
                    elif i_type == 'trad' and LVariant[1]:
                        LHTML.append('<a href="FIXME">%s</a> ' % w_word(DFrom, s=LVariant[1], 
                                                                        script='Traditional', 
                                                                        chars='cmn:eng',
                                                                        show_snd=False, translit=False))
                LHTML.append('</li>')
                
            LHTML.append('</ul>')
            LHTML.append(close('expand'))
        return ', '.join(LHeader), ''.join(LHTML)

#HTMLLinks = HTMLLinks()
