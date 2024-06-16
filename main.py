import argparse
import json

from explorer import FunnyJsonExplorer


def main():
    # 解析命令行参数
    parser = argparse.ArgumentParser(description='Funny JSON Explorer (FJE)')
    parser.add_argument('-f', '--file', required=True, help='Path to the JSON file')
    parser.add_argument('-s', '--style', required=True, choices=['tree', 'rectangle'],
                        help='Style of the visualization')
    parser.add_argument('-i', '--icon', required=True, choices=['default', 'poker'],
                        help='Icon family for the visualization')

    args = parser.parse_args()

    # 读取待转换文件
    with open(args.file, 'r', encoding='utf-8') as file:
        json_file = json.load(file)

    # 读取图标簇文件
    icon_path = 'Icon_families/icon_config.json'
    with open(icon_path, 'r', encoding='utf-8') as combined_icon_file:
        # 将JSON文件内容加载到字典中
        icon_families = json.load(combined_icon_file)
    icon = icon_families[args.icon]

    explorer = FunnyJsonExplorer(icon_family=icon, style=args.style)
    explorer.show(json_file)


if __name__ == "__main__":
    main()
