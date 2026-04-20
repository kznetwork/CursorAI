"""Pure domain rules for Magic Square (no UI / IO / framework imports)."""

from __future__ import annotations

from magicsquare.constants import (
    CELL_MAX_VALUE,
    CELL_MIN_VALUE,
    MAGIC_SUM,
    MATRIX_SIZE,
)


class NoMagicSolutionError(Exception):
    """Neither FR-05 placement yields a completed 4×4 magic square."""


def find_blank_coords(grid: list[list[int]]) -> tuple[tuple[int, int], tuple[int, int]]:
    """Return the two ``0`` cells in 1-based row-major order.

    Preconditions (caller-validated): ``grid`` is ``MATRIX_SIZE``×``MATRIX_SIZE``
    and contains exactly two cells with value ``0``.

    Returns:
        ``((r1, c1), (r2, c2))`` where ``(r1, c1)`` is the first zero in
        row-major scan, and ``(r2, c2)`` is the second.

    """
    found: list[tuple[int, int]] = []
    for r in range(MATRIX_SIZE):
        for c in range(MATRIX_SIZE):
            if grid[r][c] == 0:
                found.append((r + 1, c + 1))
    return (found[0], found[1])


def _copy_grid(grid: list[list[int]]) -> list[list[int]]:
    return [list(row) for row in grid]


def _sum_row(grid: list[list[int]], row: int) -> int:
    return sum(grid[row][c] for c in range(MATRIX_SIZE))


def _sum_col(grid: list[list[int]], col: int) -> int:
    return sum(grid[r][col] for r in range(MATRIX_SIZE))


def _sum_main_diagonal(grid: list[list[int]]) -> int:
    return sum(grid[i][i] for i in range(MATRIX_SIZE))


def _sum_anti_diagonal(grid: list[list[int]]) -> int:
    return sum(grid[i][MATRIX_SIZE - 1 - i] for i in range(MATRIX_SIZE))


def find_missing_pair_sorted(grid: list[list[int]]) -> tuple[int, int]:
    """Return ``(n_small, n_large)`` for the two values missing from 1..CELL_MAX."""
    present: set[int] = set()
    for r in range(MATRIX_SIZE):
        for c in range(MATRIX_SIZE):
            v = grid[r][c]
            if v != 0:
                present.add(v)
    missing = sorted(
        v for v in range(CELL_MIN_VALUE, CELL_MAX_VALUE + 1) if v not in present
    )
    return (missing[0], missing[1])


def is_completed_magic_square(grid: list[list[int]]) -> bool:
    """True iff the grid has no zeros and every magic line sums to ``MAGIC_SUM``."""
    for r in range(MATRIX_SIZE):
        for c in range(MATRIX_SIZE):
            if grid[r][c] == 0:
                return False

    expected = MAGIC_SUM
    for r in range(MATRIX_SIZE):
        if _sum_row(grid, r) != expected:
            return False
    for c in range(MATRIX_SIZE):
        if _sum_col(grid, c) != expected:
            return False
    if _sum_main_diagonal(grid) != expected:
        return False
    if _sum_anti_diagonal(grid) != expected:
        return False
    return True


def solve_placement(grid: list[list[int]]) -> list[int]:
    """Apply FR-05: two placements; return ``[r1,c1,n1,r2,c2,n2]`` or raise.

    Args:
        grid: Valid input (caller must enforce I1–I4). Not mutated.

    Raises:
        NoMagicSolutionError: If both attempts fail.

    """
    (r1, c1), (r2, c2) = find_blank_coords(grid)
    n_small, n_large = find_missing_pair_sorted(grid)
    r1i, c1i, r2i, c2i = r1 - 1, c1 - 1, r2 - 1, c2 - 1

    def trial(first: int, second: int) -> list[list[int]]:
        g = _copy_grid(grid)
        g[r1i][c1i] = first
        g[r2i][c2i] = second
        return g

    first_grid = trial(n_small, n_large)
    if is_completed_magic_square(first_grid):
        return [r1, c1, n_small, r2, c2, n_large]

    second_grid = trial(n_large, n_small)
    if is_completed_magic_square(second_grid):
        return [r1, c1, n_large, r2, c2, n_small]

    raise NoMagicSolutionError
