class ProcessRangeBase:
    def process_range(self, x, s):
        """
        Extracts a range in it's entirety.
        
        Doesn't convert unicode backslashes 
        as I intend to do that later.
        
        TODO: Check this catches all cases! =============================================
        """
        L = []
        backslash_mode = False
        level = 0
        
        while 1:
            # Get the next character
            try: c = s[x]
            except IndexError: break
            #print 'RANGE:', x, c, level, backslash_mode
            
            # Backslash mode
            if backslash_mode:
                L.append(c)
                backslash_mode = False
                
            elif c == '\\':
                backslash_mode = True
                L.append('\\')
            
            elif c == '[':
                level += 1
                L.append('[')
            
            elif c == ']':
                level -= 1
                L.append(']')
                if not level:
                    break
            
            else:
                L.append(c)
            x += 1
        
        return x, ''.join(L)
