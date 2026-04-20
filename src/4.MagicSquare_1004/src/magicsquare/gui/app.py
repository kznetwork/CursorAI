"""Qt application bootstrap for ``python -m magicsquare``."""

from __future__ import annotations

import sys


def run_app() -> None:
    """Start the event loop and show the main window."""
    from PyQt6.QtWidgets import QApplication

    from magicsquare.gui.main_window import MainWindow

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    raise SystemExit(app.exec())
