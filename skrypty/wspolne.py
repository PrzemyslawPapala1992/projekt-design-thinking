"""Wspólne ustawienia dla skryptów projektu: ścieżki, paleta, styl wykresów."""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # zapis do plików, bez okna
import matplotlib.pyplot as plt  # noqa: E402

KATALOG = Path(__file__).resolve().parent.parent
DANE = KATALOG / "dane"
WYKRESY = KATALOG / "wizualizacje"
WYKRESY.mkdir(exist_ok=True)

# Plik-znacznik: istnieje, dopóki dane są przykładowe. Usuńcie go po wpisaniu własnych danych.
ZNACZNIK_PRZYKLADU = DANE / "PRZYKLADOWE.txt"

# Paleta (zwalidowana paleta referencyjna, tryb jasny)
POWIERZCHNIA = "#fcfcfb"
TEKST = "#0b0b0b"
TEKST_2 = "#52514e"
SIATKA = "#e4e3df"
NIEBIESKI = "#2a78d6"      # seria 1
POMARANCZ = "#eb6834"      # seria 2
SZARY_NEUTRALNY = "#c9c8c2"
# Skala rozbieżna 1..5 (czerwony <- szary -> niebieski) do pytań Likerta
LIKERT = ["#c23b3b", "#f0a09f", "#e2e1dc", "#86b6ef", "#2a78d6"]


def styl():
    plt.rcParams.update({
        "figure.facecolor": POWIERZCHNIA,
        "axes.facecolor": POWIERZCHNIA,
        "savefig.facecolor": POWIERZCHNIA,
        "axes.edgecolor": SIATKA,
        "axes.labelcolor": TEKST_2,
        "axes.titlecolor": TEKST,
        "axes.titleweight": "bold",
        "axes.titlesize": 13,
        "axes.titlelocation": "left",
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "grid.color": SIATKA,
        "grid.linewidth": 0.8,
        "xtick.color": TEKST_2,
        "ytick.color": TEKST_2,
        "font.size": 10,
        "font.family": "DejaVu Sans",
    })


def dane_przykladowe() -> bool:
    return ZNACZNIK_PRZYKLADU.exists()


def zapisz(fig, nazwa: str):
    if dane_przykladowe():
        fig.text(0.99, 0.01, "DANE PRZYKŁADOWE – podmień na wyniki swoich badań",
                 ha="right", va="bottom", fontsize=8, color=POMARANCZ, style="italic")
    sciezka = WYKRESY / nazwa
    fig.savefig(sciezka, dpi=160, bbox_inches="tight")
    plt.close(fig)
    print(f"  zapisano {sciezka.relative_to(KATALOG)}")
