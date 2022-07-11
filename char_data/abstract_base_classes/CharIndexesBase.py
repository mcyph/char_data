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
        pass

    @abstractmethod
    def keys(self, data_source=None):
        pass

    @abstractmethod
    def get_key_info(self, key):
        pass

    #==================================================================#
    #                          Value-Related                           #
    #==================================================================#

    @abstractmethod
    def values(self, key):
        pass

    @abstractmethod
    def get_value_info(self, key, value):
        pass
