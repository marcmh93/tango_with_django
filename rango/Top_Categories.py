from abc import ABC, abstractmethod


class Top_Categories(ABC):

    @abstractmethod
    def getTopCategories(self):
        pass