#!/usr/bin/env python3
"""Review a local CSV file for structural issues without exposing content.

This utility is intentionally limited to metadata: row count, required-column
presence and blank required values. It never prints cell values.
"""

from __future__ import annotations

import argparse
import csv
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class ReviewResult:
    rows: int
    blank_required_values: int
    missing_columns: tuple[str, ...]


def review_csv(path: Path, required_columns: tuple[str, ...] = ()) -> ReviewResult:
    """Return aggregate validation counts for a local CSV file."""
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.reader(handle)
        try:
            headers = next(reader)
        except StopIteration as exc:
            raise ValueError("CSV vazio: cabeçalho não encontrado.") from exc

        if not headers or any(not name.strip() for name in headers):
            raise ValueError("Cabeçalho contém nome de coluna vazio.")
        if len(headers) != len(set(headers)):
            raise ValueError("Cabeçalho contém nomes de coluna duplicados.")

        missing = tuple(name for name in required_columns if name not in headers)
        required_indexes = [headers.index(name) for name in required_columns if name in headers]

        row_count = 0
        blank_count = 0

        for row in reader:
            if not row or all(not value.strip() for value in row):
                continue
            row_count += 1
            for index in required_indexes:
                if index >= len(row) or not row[index].strip():
                    blank_count += 1

        return ReviewResult(rows=row_count, blank_required_values=blank_count, missing_columns=missing)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Valida a estrutura de um CSV local sem imprimir os dados das células."
    )
    parser.add_argument("csv_file", type=Path, help="caminho do CSV localizado no ambiente local")
    parser.add_argument(
        "--required-column",
        action="append",
        default=[],
        help="nome de coluna obrigatória; pode ser informado mais de uma vez",
    )
    args = parser.parse_args()

    if not args.csv_file.is_file():
        print(f"Erro: arquivo não encontrado: {args.csv_file}", file=sys.stderr)
        return 2

    try:
        result = review_csv(args.csv_file, tuple(args.required_column))
    except (OSError, UnicodeError, csv.Error, ValueError) as exc:
        print(f"Erro ao revisar CSV: {exc}", file=sys.stderr)
        return 2

    print(f"Linhas de dados: {result.rows}")
    print(f"Valores obrigatórios vazios: {result.blank_required_values}")

    if result.missing_columns:
        print("Colunas obrigatórias ausentes: " + ", ".join(result.missing_columns))
        return 1

    if result.blank_required_values:
        return 1

    print("Revisão estrutural concluída; os valores das células não foram exibidos.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
