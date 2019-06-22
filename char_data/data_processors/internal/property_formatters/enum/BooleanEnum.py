from char_data.data_processors.internal.data_types.read import Boolean

from .Enum import Enum


class BooleanEnum(Enum, Boolean):
    """
    Same as StringEnum, except only `True`/`False` allowed,
    used for e.g. IICore to indicate whether a character is
    common in East Asia or not
    """
