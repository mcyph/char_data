from char_data.datatypes.read import IntegerList


class Frequency(IntegerList):
    DJGrade = {
        1: 'Japanese school grade 1',
        2: 'Japanese school grade 2',
        3: 'Japanese school grade 3',
        4: 'Japanese school grade 4',
        5: 'Japanese school grade 5',
        6: 'Japanese school grade 6',
        8: 'Japanese junior high school (8)',
        9: 'Character for use in names (9)',
        10: 'Character for use in names (10)'
    }

    def __init__(self, key, f, DJSON):
        IntegerList.__init__(self, key, f, DJSON)
    
    def formatted(self, ord_):
        data = self.raw_data(ord_)
        key = self.key
        
        if not data: 
            return None
        
        elif key == 'japanese frequency':
            i_freq = int(data)
            
            if i_freq < 100: 
                data = '%s/2501 extremely common' % data
            elif i_freq < 500: 
                data = '%s/2501 very common' % data
            elif i_freq < 1000: 
                data = '%s/2501 fairly common' % data
            elif i_freq < 2000: 
                data = '%s/2501 not very common' % data
            else: 
                data = '%s/2501 uncommon' % data
            
        elif key == 'chinese frequency':
            i_freq = int(data)
            
            D = {
                1: '1/5 Extremely Common',
                2: '2/5 Very Common',
                3: '3/5 Fairly Common',
                4: '4/5 Not Very Common',
                5: '5/5 Uncommon'
            }
            data = D[data]
        
        elif key == 'hong kong grade':
            # It seems that there aren't any special 
            # codes, e.g. 0, so I'll leave as it is
            data = str(data)
        
        elif key == 'japanese grade':
            # TODO: Rename Japanese Grade -> Japanese Type
            # as some values don't reference gradess
            data = self.DJGrade[int(data)]
        
        return data
