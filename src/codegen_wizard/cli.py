#统一入口：动态收集子命令
import click
from .registry import discover_generators

@click.group()
def main():
    """CodeGen-Wizard：多模板代码/配置生成平台"""
    pass

# 动态添加子命令
for name, plugin in discover_generators().items():
    main.add_command(plugin.cli, name=name)

if __name__ == "__main__":
    main()
