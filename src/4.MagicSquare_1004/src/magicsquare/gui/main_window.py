"""Main PyQt window: grid entry, validate/solve via boundary, result display."""

from __future__ import annotations

from PyQt6.QtWidgets import (
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QSpinBox,
    QWidget,
)

from magicsquare.boundary import solve, validate
from magicsquare.constants import CELL_MAX_VALUE, MATRIX_SIZE


class MainWindow(QMainWindow):
    """4×4 spin boxes, Solve button, and read-only solution line."""

    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Magic Square 4×4")
        central = QWidget(self)
        self.setCentralWidget(central)
        outer = QGridLayout(central)

        self._cells: list[list[QSpinBox]] = []
        for r in range(MATRIX_SIZE):
            row_boxes: list[QSpinBox] = []
            for c in range(MATRIX_SIZE):
                spin = QSpinBox(central)
                spin.setRange(0, CELL_MAX_VALUE)
                spin.setValue(0)
                spin.setMinimumWidth(48)
                outer.addWidget(spin, r, c)
                row_boxes.append(spin)
            self._cells.append(row_boxes)

        btn_row = QHBoxLayout()
        solve_btn = QPushButton("풀기", central)
        solve_btn.clicked.connect(self._on_solve_clicked)
        btn_row.addWidget(solve_btn)
        btn_row.addStretch()
        outer.addLayout(btn_row, MATRIX_SIZE, 0, 1, MATRIX_SIZE)

        outer.addWidget(QLabel("결과 (r1, c1, n1, r2, c2, n2):", central), MATRIX_SIZE + 1, 0)
        self._result = QLabel("—", central)
        self._result.setMinimumWidth(280)
        outer.addWidget(self._result, MATRIX_SIZE + 1, 1, 1, MATRIX_SIZE - 1)

    def _read_grid(self) -> list[list[int]]:
        return [
            [self._cells[r][c].value() for c in range(MATRIX_SIZE)]
            for r in range(MATRIX_SIZE)
        ]

    def _on_solve_clicked(self) -> None:
        grid = self._read_grid()
        try:
            validate(grid)
            solution = solve(grid)
        except ValueError as exc:
            QMessageBox.warning(self, "입력 오류 또는 해 없음", str(exc))
            self._result.setText("—")
            return
        self._result.setText(", ".join(str(x) for x in solution))
