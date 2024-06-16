from .visitor import Visitor


class TreeVisitor(Visitor):
    def visit_container(self, container):
        """
        访问容器元素
        """
        if container.level > 0:
            prefix = self.get_prefix(container.is_last, container.level)
            print(prefix + container.icon + container.name)
        iterator = container.create_iterator()
        while iterator.has_next():
            iterator.next().accept(self)

    def visit_leaf(self, leaf):
        """
        访问叶子元素
        """
        prefix = self.get_prefix(leaf.is_last, leaf.level)
        name = leaf.name.split(":")[0] if 'None' in leaf.name else leaf.name
        print(prefix + leaf.icon + name)

    @staticmethod
    def get_prefix(is_last, level):
        """
        根据元素的位置和层级获取打印前缀
        """
        prefix = ''.join(['   ' if last else '│  ' for last in is_last])
        if level > 0:
            prefix = prefix[:-3] + ('└─ ' if is_last[-1] else '├─ ')
        return prefix[:-1]
