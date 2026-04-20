"""Boundary: input validation and orchestration hooks (no PyQt here)."""

from __future__ import annotations

from magicsquare.constants import (
    CELL_MAX_VALUE,
    CELL_MIN_VALUE,
    MATRIX_SIZE,
    MSG_DUPLICATE_VALUES,
    MSG_INVALID_SIZE,
    MSG_INVALID_VALUE_RANGE,
    MSG_INVALID_ZERO_COUNT,
    MSG_NO_SOLUTION,
)
from magicsquare.domain import NoMagicSolutionError, solve_placement


def validate(grid: list[list[int]] | None) -> None:
    """Apply FR-01 / BR-10 checks; raise ``ValueError`` with PRD §8.1 messages.

    Order: I1 (size) → I2 (value range) → I3 (zero count) → I4 (duplicates).

    Raises:
        ValueError: With a fixed ``message`` string for the first violated rule.

    """
    if grid is None:
        raise ValueError(MSG_INVALID_SIZE)
    if len(grid) != MATRIX_SIZE:
        raise ValueError(MSG_INVALID_SIZE)
    for row in grid:
        if row is None or len(row) != MATRIX_SIZE:
            raise ValueError(MSG_INVALID_SIZE)

    zero_count = 0
    for r in range(MATRIX_SIZE):
        for c in range(MATRIX_SIZE):
            v = grid[r][c]
            if v == 0:
                zero_count += 1
            elif CELL_MIN_VALUE <= v <= CELL_MAX_VALUE:
                continue
            else:
                raise ValueError(MSG_INVALID_VALUE_RANGE)

    if zero_count != 2:
        raise ValueError(MSG_INVALID_ZERO_COUNT)

    seen: set[int] = set()
    for r in range(MATRIX_SIZE):
        for c in range(MATRIX_SIZE):
            v = grid[r][c]
            if v == 0:
                continue
            if v in seen:
                raise ValueError(MSG_DUPLICATE_VALUES)
            seen.add(v)


def solve(grid: list[list[int]]) -> list[int]:
    """Validate ``grid``, then return FR-05 solution ``int[6]`` (1-based coords).

    Does not mutate ``grid``.

    Raises:
        ValueError: On FR-01 failure (from ``validate``) or ``NO_SOLUTION`` message.

    """
    validate(grid)
    try:
        return solve_placement(grid)
    except NoMagicSolutionError as exc:
        raise ValueError(MSG_NO_SOLUTION) from exc
