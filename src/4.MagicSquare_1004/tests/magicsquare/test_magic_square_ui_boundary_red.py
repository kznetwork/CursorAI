"""UI / boundary RED skeleton — Magic Square 4×4 (dual-track, pytest)."""

from __future__ import annotations

import copy

import pytest

from magicsquare.boundary import solve, validate
from magicsquare.constants import (
    CELL_MAX_VALUE,
    MATRIX_SIZE,
    MSG_DUPLICATE_VALUES,
    MSG_INVALID_VALUE_RANGE,
    MSG_INVALID_ZERO_COUNT,
)

# PRD §9.3 — TQ-01
_TQ_01: list[list[int]] = [
    [16, 2, 3, 13],
    [5, 11, 10, 8],
    [9, 7, 0, 12],
    [4, 14, 15, 0],
]


class TestMagicSquareUiBoundaryRed:
    """Track A — UI RED (§6.2). Methods intentionally fail until GREEN."""

    def test_ui_red_01_non_four_by_four_raises(self) -> None:
        too_few_rows = [[0] * MATRIX_SIZE for _ in range(MATRIX_SIZE - 1)]
        with pytest.raises(ValueError):
            validate(too_few_rows)

        wrong_row_width = [[0] * (MATRIX_SIZE - 1) for _ in range(MATRIX_SIZE)]
        with pytest.raises(ValueError):
            validate(wrong_row_width)

    def test_ui_red_02_blank_count_not_two_raises(self) -> None:
        three_zeros = copy.deepcopy(_TQ_01)
        three_zeros[0][0] = 0
        with pytest.raises(ValueError) as exc_three:
            validate(three_zeros)
        assert str(exc_three.value) == MSG_INVALID_ZERO_COUNT

        one_zero = copy.deepcopy(_TQ_01)
        one_zero[2][2] = 1
        with pytest.raises(ValueError) as exc_one:
            validate(one_zero)
        assert str(exc_one.value) == MSG_INVALID_ZERO_COUNT

    def test_ui_red_03_value_out_of_range_raises(self) -> None:
        bad_high = copy.deepcopy(_TQ_01)
        bad_high[0][0] = CELL_MAX_VALUE + 1
        with pytest.raises(ValueError) as exc_high:
            validate(bad_high)
        assert str(exc_high.value) == MSG_INVALID_VALUE_RANGE

        bad_low = copy.deepcopy(_TQ_01)
        bad_low[0][0] = -1
        with pytest.raises(ValueError) as exc_low:
            validate(bad_low)
        assert str(exc_low.value) == MSG_INVALID_VALUE_RANGE

    def test_ui_red_04_duplicate_non_zero_raises(self) -> None:
        dup = copy.deepcopy(_TQ_01)
        dup[0][0] = 5
        dup[1][0] = 5
        with pytest.raises(ValueError) as exc_dup:
            validate(dup)
        assert str(exc_dup.value) == MSG_DUPLICATE_VALUES

    def test_ui_red_05_solution_returns_length_six(self) -> None:
        sol = solve(_TQ_01)
        assert len(sol) == 6
        assert sol == [3, 3, 6, 4, 4, 1]

    def test_ui_red_06_solution_coords_are_one_indexed(self) -> None:
        sol = solve(_TQ_01)
        r1, c1, _, r2, c2, _ = sol
        for v in (r1, c1, r2, c2):
            assert 1 <= v <= MATRIX_SIZE
