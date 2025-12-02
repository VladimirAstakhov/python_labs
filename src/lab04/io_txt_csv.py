from pathlib import Path
import csv
from typing import Iterable, Sequence
from src.lib.text import normalize, tokenize
import sys


def read_text(path: str | Path, encoding: str = "utf-8") -> str:

    p = Path(path)
    return p.read_text(encoding=encoding)


def write_csv(
    rows: Iterable[Sequence], path: str | Path, header: tuple[str, ...] | None = None
) -> None:
    p = Path(path)

    rows_list = list(rows)
    if rows_list:
        expected = len(rows_list[0])
        for r in rows_list:
            if len(r) != expected:
                raise ValueError("Все строки CSV должны иметь одинаковую длину")

    p = Path(path)

    with p.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if header is not None:
            writer.writerow(header)
        for row in rows_list:
            writer.writerow(row)


from collections import Counter


def frequencies_from_text(text: str) -> dict[str, int]:
    tokens = tokenize(normalize(text))
    return Counter(tokens)


def sorted_word_counts(freq: dict[str, int]) -> list[tuple[str, int]]:
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))
