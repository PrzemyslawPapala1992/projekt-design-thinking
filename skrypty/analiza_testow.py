"""Testowanie: porównanie wariantów A/B prototypu (dane/testy_wyniki.csv – eksport z prototyp.html)."""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from wspolne import DANE, NIEBIESKI, POMARANCZ, TEKST_2, styl, zapisz

CELE_S = {"T1": 30, "T2": 60, "T3": 60, "T4": 45, "T5": 60}
KOLORY = {"A": NIEBIESKI, "B": POMARANCZ}
NAZWY = {"A": "A – Oś czasu", "B": "B – Kafelki kursów"}


def wykres(df):
    zadania = sorted(df.zadanie.unique())
    x = np.arange(len(zadania))
    szer = 0.38
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.5))
    for i, w in enumerate(sorted(df.wariant.unique())):
        g = df[df.wariant == w].groupby("zadanie")
        med = g.czas_s.median().reindex(zadania)
        skut = g.sukces.mean().reindex(zadania) * 100
        przes = (i - 0.5) * szer
        ax1.bar(x + przes, med, szer - 0.04, color=KOLORY.get(w), label=NAZWY.get(w, w))
        ax2.bar(x + przes, skut, szer - 0.04, color=KOLORY.get(w), label=NAZWY.get(w, w))
    for j, z in enumerate(zadania):
        if z in CELE_S:
            ax1.plot([j - 0.42, j + 0.42], [CELE_S[z]] * 2, color=TEKST_2, lw=1.5, ls="--")
    ax1.set_xticks(x, zadania)
    ax1.set_ylabel("Mediana czasu [s]")
    ax1.set_title("Czas wykonania zadania (– – cel)")
    ax2.set_xticks(x, zadania)
    ax2.set_ylim(0, 105)
    ax2.axhline(80, color=TEKST_2, lw=1, ls="--")
    ax2.set_ylabel("Skuteczność [%]")
    ax2.set_title("Skuteczność (– – próg 80%)")
    for ax in (ax1, ax2):
        ax.grid(axis="x", visible=False)
    fig.legend(*ax2.get_legend_handles_labels(), frameon=False, loc="lower center", ncol=2, bbox_to_anchor=(0.5, -0.06))
    zapisz(fig, "testy_warianty.png")


if __name__ == "__main__":
    styl()
    print("Testy A/B:")
    df = pd.read_csv(DANE / "testy_wyniki.csv")
    tab = df.groupby("wariant").agg(mediana_czasu_s=("czas_s", "median"),
                                   skutecznosc_proc=("sukces", lambda s: round(s.mean() * 100, 1)),
                                   uczestnicy=("uczestnik", "nunique"))
    print(tab.to_string())
    wykres(df)
