#Dataclass / Pydantic 模型
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Any, List, Tuple

@dataclass
class TemplateContext:
    control_points: List[Tuple[float, float]]
    legend: bool

@dataclass
class RenderResult:
    code: str
    output_path: Path | None = None   # 预留：如果未来直接写文件
