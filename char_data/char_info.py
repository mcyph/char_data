try:
    from char_data.CharData import CharData
    from char_data.CharIndexes import CharIndexes

    char_data = CharData()
    char_indexes = CharIndexes()

    # Define various shortcuts
    keys = char_data.keys
    raw_data = char_data.raw_data
    formatted = char_data.formatted

    idx_search = char_indexes.search
    idx_keys = char_indexes.keys
    idx_values = char_indexes.values
except:
    # This happens e.g. if the data was corrupted
    # due to a failed import, so continue on without
    # loading the data
    import traceback
    traceback.print_exc()
