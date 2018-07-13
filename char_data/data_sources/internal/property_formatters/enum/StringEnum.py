from char_data.data_sources.internal.data.read import StringData

from Enum import Enum


class StringEnum(Enum, StringData):
    """
    Provides expansion of strings to provide more meaning,
    e.g. a "General Category" of "Lm" might be converted to
    "Letter, Modifier"
    """
