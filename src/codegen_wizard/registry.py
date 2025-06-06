"""
插件注册中心：发现并加载 entry_point = 'codegen_wizard.generators'
"""
from importlib.metadata import entry_points

def discover_generators() -> dict:
    eps = entry_points(group="codegen_wizard.generators")
    return {ep.name: ep.load() for ep in eps}
