try:
    from char_data.DataClass import Data
    from char_data.IndexesClass import Indexes

    Data = Data()
    Indexes = Indexes()

    # Define various shortcuts
    keys = Data.keys
    raw_data = Data.raw_data
    formatted = Data.formatted

    idx_search = Indexes.search
    idx_keys = Indexes.keys
    idx_values = Indexes.values
except:
    # This happens e.g. if the data was corrupted
    # due to a failed import, so continue on without
    # loading the data
    import traceback
    traceback.print_exc()
