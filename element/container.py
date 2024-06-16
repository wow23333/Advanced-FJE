from iterator.concrete_iterator import ConcreteIterator
from .abstractEle import AbstractEle


# 容器类
class Container(AbstractEle):
    def __init__(self, name, icon, level=0, is_first=False, is_last=None):
        super().__init__(name, icon, level, is_first, is_last)
        self.child = []

    def accept(self, visitor):
        """
        接受访问者对象访问
        """
        visitor.visit_container(self)

    def create_iterator(self):
        """
        创建迭代器
        """
        return ConcreteIterator(self.child)

    def add(self, node):
        """
        添加子节点
        """
        self.child.append(node)
