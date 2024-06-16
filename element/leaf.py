from iterator.concrete_iterator import ConcreteIterator
from .abstractEle import AbstractEle


# 叶子类
class Leaf(AbstractEle):
    def accept(self, visitor):
        """
        接受访问者对象访问
        """
        visitor.visit_leaf(self)

    def create_iterator(self):
        """
        创建迭代器
        """
        return ConcreteIterator([])
