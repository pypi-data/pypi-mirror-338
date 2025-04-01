from dataclasses import dataclass


@dataclass
class ModelRunStats:
    model_name: str
    sum_execution_time: float = 0
    min_execution_time: float | None = None
    max_execution_time: float | None = None
    call_count: int = 0
