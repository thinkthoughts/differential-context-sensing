from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data"
FIGURES = ROOT / "figures"
REPORTS = ROOT / "reports"
NOTEBOOKS = ROOT / "notebooks"


def ensure_dirs() -> None:
    for path in (DATA, FIGURES, REPORTS, NOTEBOOKS):
        path.mkdir(parents=True, exist_ok=True)
