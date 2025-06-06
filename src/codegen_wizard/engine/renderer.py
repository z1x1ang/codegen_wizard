#Jinja2 环境 + 通用过滤器
from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape

_SHARED_DIR = Path(__file__).parent.parent / "templates_shared"

def _build_env(extra_dirs: list[Path]) -> Environment:
    loader = FileSystemLoader([_SHARED_DIR, *extra_dirs])
    env = Environment(
        loader=loader,
        autoescape=select_autoescape(disabled_extensions=("j2",)),  # 纯文本
        trim_blocks=True,
        lstrip_blocks=True,
    )
    # ⭐ 通用过滤器可在此注册
    return env

def render(template_path: Path, context: dict) -> str:
    env = _build_env([template_path.parent])
    tpl = env.get_template(template_path.name)
    return tpl.render(**context)
