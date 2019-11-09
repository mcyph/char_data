from abc import ABC, abstractmethod


class ExternalSourceBase(ABC):
    def __init__(self, key):
        """
        The base class from which external sources are derived.
        This is for data in other modules or data structures.

        Each attribute derived from ExternalFormatterBase
        defined in subclasses will be

        :param key: The key as the external source will be referenced,
                    e.g. "cldr_alphabets" or "hanzi_variants"
        """
        self.key = key
