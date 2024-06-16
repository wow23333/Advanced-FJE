import copy
from element.container import Container
from element.leaf import Leaf
from visitor.rectangle_visitor import RectangleVisitor
from visitor.tree_visitor import TreeVisitor


# FJE类
class FunnyJsonExplorer:
    def __init__(self, icon_family, style):
        self.root = None
        self.max_level = 0
        self.max_len = 0
        self.name_len = 0
        self.icon_family = icon_family or {"container": " ", "leaf": " "}
        self.style = style

    def load(self, file_data):
        """
        加载并解析JSON数据
        """
        self.root = self.parse(file_data, "root", level=0)
        self.max_len = self.max_level * 3 + self.name_len + 5

    def parse(self, data, name, level=0, is_last=None, is_first=False):
        """
        解析JSON数据，递归地创建容器和叶子元素
        """
        if is_last is None:
            is_last = []

        self.max_level = max(self.max_level, level)
        self.name_len = max(self.name_len, len(name))

        if isinstance(data, dict):
            container = Container(name, icon=self.icon_family.get("container", ""), level=level, is_first=is_first,
                                  is_last=is_last)

            for i, (key, value) in enumerate(data.items()):
                child_is_last = copy.deepcopy(is_last)
                child_is_last.append(i == len(data) - 1)

                if isinstance(value, dict):
                    child_node = self.parse(value, key, level + 1, child_is_last, is_first=(i == 0 and name == "root"))
                else:
                    child_node = Leaf(f"{key}: {value}", icon=self.icon_family.get("leaf", ""), level=level + 1,
                                      is_last=child_is_last, is_first=(i == 0 and name == "root"))
                    self.name_len = max(self.name_len, len(f"{key}: {value}"))

                container.add(child_node)

            return container
        else:
            leaf = Leaf(f"{name}: {data}", icon=self.icon_family.get("leaf", ""), level=level)
            self.name_len = max(self.name_len, len(f"{name}: {data}"))
            return leaf

    def show(self, file_data):
        """
        显示解析后的JSON数据
        """
        global visitor
        self.load(file_data)
        if self.root:
            if self.style == "tree":
                visitor = TreeVisitor()
            elif self.style == "rectangle":
                visitor = RectangleVisitor(self.max_len)
            iterator = self.root.create_iterator()
            while iterator.has_next():
                iterator.next().accept(visitor)
