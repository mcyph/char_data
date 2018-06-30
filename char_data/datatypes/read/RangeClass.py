class NO_DATA: pass


class RangeClass:
    def get_range_data(self, ord_):
        for from_, to, value in self.LRanges:
            if from_ > ord_:
                # Stop searching if no greater values
                break
            
            elif ord_>=from_ and ord_<=to: 
                return value
        
        return NO_DATA
