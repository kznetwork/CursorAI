"""Official entry: ``python -m magicsquare`` launches the PyQt GUI."""

from __future__ import annotations


def main() -> None:
    """Run the screen layer (requires optional ``[gui]`` dependencies)."""
    try:
        from magicsquare.gui.app import run_app
    except ImportError as exc:
        missing = exc.name if getattr(exc, "name", None) else "PyQt6"
        raise SystemExit(
            f"GUI 의존성이 없습니다 ({missing}). 설치: pip install -e \".[gui]\"",
        ) from exc
    run_app()


if __name__ == "__main__":
    main()
