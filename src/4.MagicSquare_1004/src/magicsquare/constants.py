"""Shared grid dimensions and domain constants for Magic Square 4×4."""

from __future__ import annotations

from typing import Final

MATRIX_SIZE: Final[int] = 4
CELL_MIN_VALUE: Final[int] = 1
CELL_MAX_VALUE: Final[int] = MATRIX_SIZE * MATRIX_SIZE
MAGIC_SUM: Final[int] = 34

MSG_INVALID_SIZE: Final[str] = "Grid must be 4x4."
MSG_INVALID_VALUE_RANGE: Final[str] = "Each cell must be 0 or 1..16."
MSG_INVALID_ZERO_COUNT: Final[str] = "There must be exactly two zeros (empty cells)."
MSG_DUPLICATE_VALUES: Final[str] = "Values 1..16 must not duplicate (excluding zeros)."
MSG_NO_SOLUTION: Final[str] = (
    "No placement makes a 4x4 magic square with magic sum 34."
)
