from DEnum import DEnum


def get_D_rev_enum():
    DRevEnum = {}
    for key, i_D in DEnum.items():
        DRevEnum[key] = dict((value.split('(')[0].strip(), key) 
                             for key, value in i_D.items())
    print DRevEnum
    return DRevEnum


DRevEnum = get_D_rev_enum()


class Enum:
    def _format_data(self, ord_, data):
        if self.key in DEnum and unicode(data) in DEnum[self.key]:
            return DEnum[self.key][unicode(data)]
        else: 
            return data # HACK!


if __name__ == '__main__':
    from json import dumps

    print(dumps(DEnum, indent=4, ensure_ascii=False, sort_keys=True))


