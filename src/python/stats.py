"""Tiny stats helpers."""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, List

@dataclass
class Summary:
    count: int
    total: float
    mean: float
    minimum: float
    maximum: float

def summarize(values: Iterable[float]) -> Summary:
    data: List[float] = list(values)
    if not data:
        raise ValueError("empty input")
    total = sum(data)
    return Summary(
        count=len(data),
        total=total,
        mean=total / len(data),
        minimum=min(data),
        maximum=max(data),
    )
