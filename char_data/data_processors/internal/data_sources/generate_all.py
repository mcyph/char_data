if __name__ == '__main__':
    # Import/write all the data from CCDict/Kanjidic/Unicode/Unihan

    from char_data.data_processors.internal.data_sources.ccdict import ImportCCDict
    from char_data.data_processors.internal.data_sources.kanjidic import ImportKanjidic
    from char_data.data_processors.internal.data_sources.unicode import ImportUnicode
    from char_data.data_processors.internal.data_sources.unihan import ImportUnihan

    ImportCCDict.run()
    ImportKanjidic.run()
    #MultiRads.run()
    ImportUnicode.run()
    ImportUnihan.run()

