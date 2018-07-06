from write import write_fulltext_index, write_indices_index, \
                  write_radical_strokes_index, write_integer_keys_index, \
                  write_string_keys_index, write_compressed_names_index

from read import FulltextIndex, IndicesIndex, IntegerKeyIndex, \
                 RadicalStrokesIndex, StringKeyIndex

DIndexWriters = {
    'CompressedNames': write_compressed_names_index, 
    'Fulltext': write_fulltext_index, 
    'Indices': write_indices_index,
    'IntegerKeys': write_integer_keys_index,
    'RadicalStrokes': write_radical_strokes_index,
    'StringKeys': write_string_keys_index
}

DIndexReaders = {
    'CompressedNames': FulltextIndex, 
    'Fulltext': FulltextIndex, 
    'Indices': IndicesIndex,
    'IntegerKeys': IntegerKeyIndex,
    'RadicalStrokes': RadicalStrokesIndex,
    'StringKeys': StringKeyIndex
}
