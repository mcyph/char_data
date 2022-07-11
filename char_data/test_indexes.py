def test():
    char_data = CharData()
    char_indexes = CharIndexes(char_data=char_data)
    del char_indexes
    char_indexes = CharIndexes(char_data=char_data)

    print(char_indexes.search('name', 'smile'))

    LKeys = []
    for key in list(char_indexes.keys()):
        print(key)
        ciki = char_indexes.get_key_info(key)
        cdki = char_data.get_key_info(key)
        inst = char_data.get_class_by_property(key)

        header = cdki.header_const
        LKeys.append((header, key, inst))
    LKeys.sort()

    for header, key, inst in LKeys:
        print((header, key, inst))
        continue

        LValues = char_indexes.values((source, key))
        if not LValues:
            continue

        print(LValues)
        for value in LValues:
            print(('KEY/VALUE:', (key, value), char_indexes.search((source, key), value)))


if __name__ == '__main__':
    test()
