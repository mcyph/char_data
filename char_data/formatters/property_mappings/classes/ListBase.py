import abc


class ListBase(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_L(self):
        raise NotImplementedError()

    @abc.abstractmethod
    def get_L_results(self, subheading):
        raise NotImplementedError()

