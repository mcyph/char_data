from abc import ABC, abstractmethod


class CharDataBase(ABC):
    """
    The class "contract" which CharIndexes and CharIndexesClient
    must follow. Not to be instantiated directly.
    """

    @abstractmethod
    def get_data_sources(self):
        """
        Get a list of the possible data sources, such as "unicodedata"
        (internal sources) or "hanzi_variants" (external sources)
        :return: a list of data sources
        """
        pass

    #=============================================================#
    #                  Get Character Data Keys                    #
    #=============================================================#

    @abstractmethod
    def keys(self, data_source=None):
        """
        Get a list of the possible data source/key combinations

        :param data_source: one of the data sources returned by
                            get_data_sources (optional)
        :return: a list of ["source.key", ...]
        """
        pass

    @abstractmethod
    def get_key_info(self, key):
        """
        Get information about internal key `key`,
        e.g. to allow displaying the key to humans
        (Kanjidic "freq" might be "Japanese Frequency", for instance)

        :param key: a key in the format "source.key" as returned by
                    `keys()`, or just "key" (will default to the
                    first data source with that key as returned by
                    `get_data_sources()`)
        :return: a `CharDataKeyInfo` object with key information
        """
        pass

    #=============================================================#
    #                     Get Character Data                      #
    #=============================================================#

    @abstractmethod
    def get_all_data_for_codepoint(self, ord_):
        """
        Get a list of all the data associated
        with this codepoint, grouped by heading.

        :param ord_: the character ordinal
        :return: a list of (heading, (property key,
                            short description,
                            html value,
                            raw data),
                            ...)
        """
        pass

    @abstractmethod
    def raw_data(self, key, ord_):
        """
        Get the raw data from formatter instance `key`
        about character ordinal or character `ord_`

        :param key: a key in the format "source.key" as returned by
                    `keys()`, or just "key" (will default to the
                    first data source with that key as returned by
                    `get_data_sources()`)
        :param ord_: the ordinal (or string character) of the
                     character to look up
        :return: the raw data. The format may differ from source
                 to source - may be an integer, a tuple of
                 `((description, ordinal), ...)` for related
                 characters, etc.
        """
        pass

    @abstractmethod
    def formatted(self, key, ord_):
        """
        Get the formatted data from formatter instance `key`
        about character ordinal or character `ord_`

        :param key: a key in the format "source.key" as returned by
                    `keys()`, or just "key" (will default to the
                    first data source with that key as returned by
                    `get_data_sources()`)
        :param ord_: the ordinal (or string character) of the
                     character to look up
        :return: the formatted data as a string
        """
        pass

    @abstractmethod
    def html_formatted(self, key, ord_):
        """
        Uses the formatted() method above, but also adds basic
        HTML formatting

        :param key: a key in the format "source.key" as returned by
                    `keys()`, or just "key" (will default to the
                    first data source with that key as returned by
                    `get_data_sources()`)
        :param ord_: the ordinal (or string character) of the
                     character to look up
        :return: the formatted HTML data as a string
        """
        pass

    #=============================================================#
    #                 Character Heading Mappings                  #
    #=============================================================#

    @abstractmethod
    def get_two_level_mapping(self, key):
        """

        :param key:
        :return:
        """
        pass

    #=============================================================#
    #                Group Characters by Headings                 #
    #=============================================================#

    @abstractmethod
    def group_into_unicode_name_headings(self, LRanges, name=None):
        """

        :param LRanges:
        :param name:
        :return:
        """
        pass

    @abstractmethod
    def group_into_block_headings(self, LRanges):
        """

        :param LRanges:
        :return:
        """
        pass

    @abstractmethod
    def group_into_alphabet_headings(self, search, char_indexes=None):
        """

        :param search:
        :param char_indexes:
        :return:
        """
        pass

    @abstractmethod
    def group_into_chinese_frequency_headings(self, LRanges, LSortBy):
        """

        :param LRanges:
        :param LSortBy:
        :return:
        """
        pass

    @abstractmethod
    def group_into_japanese_frequency_headings(self, LRanges):
        """

        :param LRanges:
        :return:
        """
        pass
