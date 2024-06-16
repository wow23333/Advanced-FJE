from .visitor import Visitor


class RectangleVisitor(Visitor):
    def __init__(self, max_len):
        self.max_len = max_len

    def visit_container(self, container):
        """
        访问容器元素的方法
        """
        is_first = container.is_first
        icon = container.icon
        name = container.name
        level = container.level

        # 根据容器是否为第一个元素，打印不同格式的头部
        if is_first:
            print(f"┌─{icon}{name} ─"
                  f"{'─' * (self.max_len - len(str(name)) - len(icon))}┐")
        else:
            print(f"{'│  ' * (level - 1)}├─{icon}{name} ─"
                  f"{'─' * (self.max_len - len(str(name)) - 3 * (level - 1) - len(icon))}|")

        iterator = container.create_iterator()
        while iterator.has_next():
            child = iterator.next()
            child.accept(self)

    def visit_leaf(self, leaf):
        """
        访问叶子元素的方法
        """
        is_last = leaf.is_last
        max_len = self.max_len
        name_parts = leaf.name.split(":")
        name = name_parts[0] if 'None' in leaf.name else leaf.name
        level = leaf.level
        icon = leaf.icon

        # 根据叶子元素的位置和层级，确定打印的前缀和后缀
        flag = all(is_last)
        if flag:
            prefix = '└──' + '┴──' * max(0, level - 2) + ('┴─' if level > 1 else '')
            suffix = '─' * (max_len - 3 * (level - 1) - len(name)) + '┘'
        else:
            prefix = '│  ' * (level - 1) + '├─'
            suffix = '─' * (max_len - 3 * (level - 1) - len(name)) + '|'
        print("{}{}{} {}".format(prefix, icon, name, suffix))
