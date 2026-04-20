"""Logic RED skeleton — Magic Square 4×4 (dual-track, pytest)."""

from __future__ import annotations

from magicsquare.constants import MATRIX_SIZE
from magicsquare.domain import (
    find_blank_coords,
    find_missing_pair_sorted,
    is_completed_magic_square,
    solve_placement,
)

# PRD §9.3 — TQ-01 (정상 복원)
_TQ_01: list[list[int]] = [
    [16, 2, 3, 13],
    [5, 11, 10, 8],
    [9, 7, 0, 12],
    [4, 14, 15, 0],
]

# 각 행은 MAGIC_SUM이지만 열·대각은 맞지 않음 (도메인 판정용)
_GRID_ROWS_ONLY: list[list[int]] = [
    [10, 10, 10, 4],
    [10, 10, 10, 4],
    [10, 10, 10, 4],
    [10, 10, 10, 4],
]

# 행·열은 MAGIC_SUM이지만 주·부 대각은 아님 (정수, 0 없음)
_GRID_SEMI_NOT_MAGIC: list[list[int]] = [
    [1, 4, 12, 17],
    [2, 6, 7, 19],
    [9, 8, 10, 7],
    [22, 16, 5, -9],
]


def _transpose(g: list[list[int]]) -> list[list[int]]:
    return [[g[r][c] for r in range(MATRIX_SIZE)] for c in range(MATRIX_SIZE)]


def _tq01_completed_magic() -> list[list[int]]:
    g = [list(row) for row in _TQ_01]
    g[2][2] = 6
    g[3][3] = 1
    return g


class TestMagicSquareLogicRed:
    """Track B — Logic RED (§6.3). Methods intentionally fail until GREEN."""

    def test_log_red_01_find_blank_coords_row_major_two_cells(self) -> None:
        # TQ-01: row-major에서 첫 0은 (3,3), 둘째는 (4,4) — §9.3 행렬 리터럴 기준
        first, second = find_blank_coords(_TQ_01)
        assert first == (3, 3)
        assert second == (4, 4)
        assert first != second

    def test_log_red_02_find_not_exist_nums_two_sorted_ascending(self) -> None:
        assert find_missing_pair_sorted(_TQ_01) == (1, 6)

    def test_log_red_03a_is_magic_square_false_when_only_rows_match(self) -> None:
        assert not is_completed_magic_square(_GRID_ROWS_ONLY)

    def test_log_red_03b_is_magic_square_false_when_only_cols_match(self) -> None:
        assert not is_completed_magic_square(_transpose(_GRID_ROWS_ONLY))

    def test_log_red_03c_is_magic_square_false_when_diagonal_wrong(self) -> None:
        assert not is_completed_magic_square(_GRID_SEMI_NOT_MAGIC)

    def test_log_red_03d_is_magic_square_true_for_known_complete(self) -> None:
        assert is_completed_magic_square(_tq01_completed_magic())

    def test_log_red_04a_solution_returns_six_elements_ordered(self) -> None:
        sol = solve_placement(_TQ_01)
        assert len(sol) == 6
        assert sol == [3, 3, 6, 4, 4, 1]

    def test_log_red_04b_solution_coords_one_indexed_in_range(self) -> None:
        sol = solve_placement(_TQ_01)
        r1, c1, _, r2, c2, _ = sol
        for v in (r1, c1, r2, c2):
            assert 1 <= v <= MATRIX_SIZE

    def test_log_red_04c_solution_reverse_policy_after_small_first_fails(self) -> None:
        first, second = find_blank_coords(_TQ_01)
        n_small, n_large = find_missing_pair_sorted(_TQ_01)
        r1i, c1i, r2i, c2i = first[0] - 1, first[1] - 1, second[0] - 1, second[1] - 1
        g_small_first = [list(row) for row in _TQ_01]
        g_small_first[r1i][c1i] = n_small
        g_small_first[r2i][c2i] = n_large
        assert not is_completed_magic_square(g_small_first)
        g_large_first = [list(row) for row in _TQ_01]
        g_large_first[r1i][c1i] = n_large
        g_large_first[r2i][c2i] = n_small
        assert is_completed_magic_square(g_large_first)
        assert solve_placement(_TQ_01) == [3, 3, n_large, 4, 4, n_small]

    def test_log_red_04d_solution_numbers_match_find_not_exist_nums(self) -> None:
        sol = solve_placement(_TQ_01)
        n_small, n_large = find_missing_pair_sorted(_TQ_01)
        assert {sol[2], sol[5]} == {n_small, n_large}
