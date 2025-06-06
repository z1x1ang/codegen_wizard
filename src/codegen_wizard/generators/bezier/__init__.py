#注册到CLI
"""
把本插件暴露给框架。
被 `entry_points` 发现后，会被 `registry.py` 自动加载。
"""
from pathlib import Path
from . import prompts

# 供 CLI 动态挂载
cli = prompts.cli

# 帮助其他插件/测试检索模板根
TEMPLATE_DIR = Path(__file__).parent / "templates"
