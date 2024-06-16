from abc import ABC, abstractmethod


# 访问者模式

# 抽象访问者
class Visitor(ABC):
    @abstractmethod
    def visit_container(self, container):
        """
        访问容器元素
        """
        pass

    @abstractmethod
    def visit_leaf(self, leaf):
        """
        访问叶子元素
        """
        pass
