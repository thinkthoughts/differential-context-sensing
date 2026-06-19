from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

DATA = ROOT / "data"
FIGURES = ROOT / "figures"
NOTEBOOKS = ROOT / "notebooks"


def ensure_dirs() -> None:
    DATA.mkdir(parents=True, exist_ok=True)
    FIGURES.mkdir(parents=True, exist_ok=True)
    NOTEBOOKS.mkdir(parents=True, exist_ok=True)
