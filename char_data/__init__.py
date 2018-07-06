#try:

if False:
    class Forward:
        def __init__(self, forward_to):
            self.forward_to = forward_to

        def __getattr__(self, item):
            while 1:
                try:
                    return getattr(eval(self.forward_to), item)
                except NameError:
                    pass

    char_data = Forward('_char_data')
    char_indexes = Forward('_char_indexes')

    def init_me():
        from CharData import CharData
        from CharIndexes import CharIndexes

        global _char_data, _char_indexes
        _char_data = CharData()
        _char_indexes = CharIndexes()
    import thread
    thread.start_new_thread(init_me, ())
else:
    from CharData import CharData
    from CharIndexes import CharIndexes

    char_data = CharData()
    char_indexes = CharIndexes()

# Define various shortcuts
#keys = char_data.keys
#char_data.raw_data = char_data.char_data.raw_data
#formatted = char_data.formatted

#char_indexes.search = char_indexes.search
#idx_keys = char_indexes.keys
#idx_values = char_indexes.values

#except:
    # This happens e.g. if the data was corrupted
    # due to a failed import, so continue on without
    # loading the data
#    import traceback
#    traceback.print_exc()
