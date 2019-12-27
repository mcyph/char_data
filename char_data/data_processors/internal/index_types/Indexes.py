from char_data.data_processors.internal.index_types.write.write_fulltext_index import \
    write_fulltext_index
from char_data.data_processors.internal.index_types.write.write_indices_index import \
    write_indices_index
from char_data.data_processors.internal.index_types.write.write_radical_strokes_index import \
    write_radical_strokes_index
from char_data.data_processors.internal.index_types.write.write_integer_keys_index import \
    write_integer_keys_index
from char_data.data_processors.internal.index_types.write.write_string_keys_index import \
    write_string_keys_index
from char_data.data_processors.internal.index_types.write.write_fulltext_index import \
    write_compressed_names_index

from char_data.data_processors.internal.index_types.read.Fulltext import FulltextIndex
from char_data.data_processors.internal.index_types.read.Indices import IndicesIndex
from char_data.data_processors.internal.index_types.read.IntegerKeys import IntegerKeyIndex
from char_data.data_processors.internal.index_types.read.RadicalStrokes import RadicalStrokesIndex
from char_data.data_processors.internal.index_types.read.StringKeys import StringKeyIndex

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
