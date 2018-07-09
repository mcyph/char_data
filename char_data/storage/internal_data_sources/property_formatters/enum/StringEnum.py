from char_data.storage.data.read import StringData

from Enum import Enum


class StringEnum(StringData, Enum):
    """
    Provides expansion of strings to provide more meaning,
    e.g. a "General Category" of "Lm" might be converted to
    "Letter, Modifier"
    """
