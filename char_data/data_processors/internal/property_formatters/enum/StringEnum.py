from char_data.data_processors.internal.data_types.read import StringData

from .Enum import Enum


class StringEnum(Enum, StringData):
    """
    Provides expansion of strings to provide more meaning,
    e.g. a "General Category" of "Lm" might be converted to
    "Letter, Modifier"
    """
