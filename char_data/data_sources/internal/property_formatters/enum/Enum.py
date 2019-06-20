from .DEnum import DEnum


def get_D_rev_enum():
    DRevEnum = {}
    for key, i_D in list(DEnum.items()):
        DRevEnum[key] = dict((value.split('(')[0].strip(), key) 
                             for key, value in list(i_D.items()))
    #print DRevEnum
    return DRevEnum


DRevEnum = get_D_rev_enum()


class Enum:
    def _format_data(self, ord_, data):
        #print("ENUM FORMAT:", self.key, ord_, data, DEnum.get(self.key))

        if self.key in DEnum and str(data) in DEnum[self.key]:
            return DEnum[self.key][str(data)]
        else: 
            return data # HACK!


if __name__ == '__main__':
    from json import dumps

    print((dumps(DEnum, indent=4, ensure_ascii=False, sort_keys=True)))
