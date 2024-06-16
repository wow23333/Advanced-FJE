from abc import ABC, abstractmethod


# 迭代器模式

# 抽象迭代器
class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        """
        判断是否还有下一个元素
        """
        pass

    @abstractmethod
    def next(self):
        """
        获取下一个元素
        """
        pass
