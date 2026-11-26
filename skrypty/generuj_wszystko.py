"""Uruchamia wszystkie analizy po kolei. Użycie:  python generuj_wszystko.py"""
import runpy
from pathlib import Path

TUTAJ = Path(__file__).resolve().parent

for skrypt in ["generuj_dane_przykladowe.py",  # tworzy dane tylko, jeśli ich brak
               "wykresy_pomyslow.py",
               "analiza_ankiety.py",
               "analiza_testow.py",
               "sus.py"]:
    print(f"\n=== {skrypt} ===")
    runpy.run_path(str(TUTAJ / skrypt), run_name="__main__")

print("\nGotowe. Wykresy w folderze wizualizacje/.")
