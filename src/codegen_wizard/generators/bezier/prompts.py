#向导式交互(Click)
import sys
from pathlib import Path
from typing import List, Tuple

import click
from codegen_wizard.engine.renderer import render

TEMPLATE_DIR = Path(__file__).parent / "templates"

def _parse_points(raw: str) -> List[Tuple[float, float]]:
    pts = []
    for pair in raw.split(";"):
        if not pair.strip():
            continue
        try:
            x, y = map(float, pair.strip().split(","))
        except ValueError as exc:
            raise ValueError(f"坐标格式错误: '{pair}'") from exc
        pts.append((x, y))
    if len(pts) < 2:
        raise ValueError("至少需要两个控制点")
    return pts

@click.command(help="交互式生成『绘制贝塞尔曲线』示例代码")
def cli():
    click.echo("🎨 Bezier 曲线代码生成向导\n")

    # Step 1 控制点
    raw = click.prompt("控制点 (格式: x0,y0; x1,y1; ...)")
    try:
        pts = _parse_points(raw)
    except ValueError as e:
        click.secho(f"❌ {e}", fg="red")
        sys.exit(1)

    # Step 2 语言
    lang = click.prompt(
        "目标语言 [m]atlab / [p]ython",
        type=click.Choice(["m", "p", "matlab", "python"]),
        default="p",
    )
    lang = "matlab" if lang.lower().startswith("m") else "python"

    # Step 3 图例
    legend = click.confirm("是否包含图例?", default=True)

    # 渲染
    tpl_file = TEMPLATE_DIR / f"{lang}.j2"
    ctx = {
        "control_points_py": ", ".join(f"({x}, {y})" for x, y in pts),
        "control_points_mat": "; ".join(f"{x} {y}" for x, y in pts),
        "legend": legend,
    }
    code = render(tpl_file, ctx)

    click.secho("\n✅ 生成完成：\n", fg="green")
    click.echo(code)
