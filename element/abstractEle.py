from abc import ABC, abstractmethod


# 抽象元素
class AbstractEle(ABC):
    def __init__(self, name, icon, level=0, is_first=False, is_last=None):
        self.name = name  # 元素名称
        self.icon = icon  # 图标
        self.level = level  # 层级
        self.is_first = is_first
        if is_last is None:
            is_last = []
        self.is_last = is_last

    @abstractmethod
    def accept(self, visitor):
        """
        接受访问者对象访问
        """
        pass

    @abstractmethod
    def create_iterator(self):
        """
        创建迭代器
        """
        pass
