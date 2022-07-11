from abc import ABC, abstractmethod
from typing import Optional, List, Union


class CharDataBase(ABC):
    """
    The class "contract" which CharIndexes and CharIndexesClient
    must follow. Not to be instantiated directly.
    """

    @abstractmethod
    def get_data_sources(self) -> List[str]:

        pass

    #=============================================================#
    #                  Get Character Data Keys                    #
    #=============================================================#

    @abstractmethod
    def keys(self,
             data_source: Optional[str] = None) -> List[str]:
        pass

    @abstractmethod
    def get_key_info(self, key: str) -> CharDataKeyInfo:
        pass

    #=============================================================#
    #                     Get Character Data                      #
    #=============================================================#

    @abstractmethod
    def get_all_data_for_codepoint(self, ord_: Union[int, chr]):

        pass

    @abstractmethod
    def raw_data(self,
                 key: str,
                 ord_: Union[int, chr]) -> Union[int, str, tuple]:
        pass

    @abstractmethod
    def formatted(self,
                  key: str,
                  ord_: Union[int, chr]) -> str:

        pass

    @abstractmethod
    def html_formatted(self,
                       key: str,
                       ord_: Union[int, chr]) -> str:

        pass

    #=============================================================#
    #                 Character Heading Mappings                  #
    #=============================================================#

    @abstractmethod
    def get_two_level_mapping(self, key: str):
        """

        :param key:
        :return:
        """
        pass

    #=============================================================#
    #                Group Characters by Headings                 #
    #=============================================================#

    @abstractmethod
    def group_by_unicode_name(self, LRanges, name=None):
        """

        :param LRanges:
        :param name:
        :return:
        """
        pass

    @abstractmethod
    def group_by_block(self, LRanges):
        """

        :param LRanges:
        :return:
        """
        pass

    @abstractmethod
    def group_by_alphabet(self,
                          search: str,
                          char_indexes=None):
        """

        :param search: the ISO code of the language
        :param char_indexes:
        :return:
        """
        pass

    @abstractmethod
    def group_by_chinese_frequency(self, LRanges, LSortBy):
        """

        :param LRanges:
        :param LSortBy:
        :return:
        """
        pass

    @abstractmethod
    def group_by_japanese_frequency(self, LRanges):
        """

        :param LRanges:
        :return:
        """
        pass
