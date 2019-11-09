from abc import ABC, abstractmethod


class IndexBase:
    @abstractmethod
    def values(self):
        pass

    @abstractmethod
    def get_value_info(self, value):
        pass

    @abstractmethod
    def search(self, search):
        pass

