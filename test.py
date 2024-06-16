import json

from explorer import FunnyJsonExplorer


def main():
    # 读取待转换文件
    json_path = 'assets/example.json'
    # json_path = './assets/complex.json'
    # json_path = './assets/middle.json'
    # json_path = './assets/simple.json'
    with open(json_path, 'r', encoding='utf-8') as file:
        json_file = json.load(file)

    # 读取图标簇文件
    icon_path = 'Icon_families/icon_config.json'
    with open(icon_path, 'r', encoding='utf-8') as icon_file:
        # 将JSON文件内容加载到字典中
        icon_families = json.load(icon_file)

    print("Tree Style with Default Icons:")
    icon = icon_families['default']
    style = 'tree'
    explorer = FunnyJsonExplorer(icon_family=icon, style=style)
    explorer.show(json_file)
    print()

    print("Rectangle Style with Default Icons:")
    icon = icon_families['default']
    style = 'rectangle'
    explorer = FunnyJsonExplorer(icon_family=icon, style=style)
    explorer.show(json_file)
    print()

    print("Tree Style with Poker Icons:")
    icon = icon_families['poker']
    style = 'tree'
    explorer = FunnyJsonExplorer(icon_family=icon, style=style)
    explorer.show(json_file)
    print()

    print("Rectangle Style with Poker Icons:")
    icon = icon_families['poker']
    style = 'rectangle'
    explorer = FunnyJsonExplorer(icon_family=icon, style=style)
    explorer.show(json_file)
    print()


if __name__ == "__main__":
    main()
