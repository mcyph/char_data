from abc import ABC, abstractmethod


class CharIndexesBase(ABC):
    """
    The class "contract" which CharData and CharDataClient must follow.
    Not to be instantiated directly.
    """

    #==================================================================#
    #                           Key-Related                            #
    #==================================================================#

    @abstractmethod
    def search(self, key, value, *args, **kw):
        """
        search the index key for value,
        This could be a FullText index, a
        Radical.AdditionalStrokes index etc

        :param key:
        :param value:
        :param args:
        :param kw:
        :return:
        """
        pass

    @abstractmethod
    def keys(self, data_source=None):
        """
        Get the index keys, e.g. "Arabic Shaping Group"

        :return: a list of keys in format "source.key"
        """
        pass

    @abstractmethod
    def get_key_info(self, key):
        """
        Get information about internal key `key`,
        e.g. to allow displaying the key to humans
        (Kanjidic "freq" might be "Japanese Frequency", for instance)

        :param key:
        :return:
        """
        pass

    #==================================================================#
    #                          Value-Related                           #
    #==================================================================#

    @abstractmethod
    def values(self, key):
        """
        Get a list of possible values in MultiIndex in RAW form
        Returns [[key, key_type], ...]
        key is the property name and key_type is e.g. "Fulltext" etc

        :param key:
        :return:
        """
        pass

    @abstractmethod
    def get_value_info(self, key, value):
        """

        :param key:
        :param value:
        :return:
        """
        pass
