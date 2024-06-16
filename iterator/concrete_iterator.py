from .iterator import Iterator


# 具体迭代器
class ConcreteIterator(Iterator):
    def __init__(self, components):
        self.components = components
        self.index = 0

    def has_next(self):
        """
        判断是否还有下一个元素
        """
        return self.index < len(self.components)

    def next(self):
        """
        获取下一个元素
        """
        component = self.components[self.index]
        self.index += 1
        return component
