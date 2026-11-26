"""Testowanie: wynik SUS (System Usability Scale) z dane/sus_wyniki.csv."""
import matplotlib.pyplot as plt
import pandas as pd

from wspolne import DANE, NIEBIESKI, POMARANCZ, TEKST, TEKST_2, styl, zapisz

SREDNIA_RYNKOWA = 68


def wynik_sus(wiersz) -> float:
    suma = 0
    for i in range(1, 11):
        odp = wiersz[f"q{i}"]
        suma += (odp - 1) if i % 2 == 1 else (5 - odp)
    return suma * 2.5


def ocena_slowna(w):
    if w >= 85:
        return "doskonała"
    if w >= 72:
        return "dobra"
    if w >= SREDNIA_RYNKOWA:
        return "powyżej przeciętnej"
    if w >= 51:
        return "słaba"
    return "nieakceptowalna"


def wykres(df):
    fig, ax = plt.subplots(figsize=(8, 4))
    kolory = {"A": NIEBIESKI, "B": POMARANCZ}
    d = df.sort_values("sus")
    ax.barh(d.uczestnik, d.sus, color=[kolory[w] for w in d.wariant], height=0.7)
    ax.axvline(SREDNIA_RYNKOWA, color=TEKST_2, ls="--", lw=1)
    ax.text(SREDNIA_RYNKOWA + 1, len(d) - 0.5, "średnia rynkowa 68", color=TEKST_2, fontsize=8)
    for i, v in enumerate(d.sus):
        ax.text(v + 1, i, f"{v:.0f}", va="center", fontsize=8, color=TEKST)
    ax.set_xlim(0, 105)
    ax.set_xlabel("Wynik SUS (0–100)")
    ax.grid(axis="y", visible=False)
    for w, k in kolory.items():
        ax.barh([], [], color=k, label=f"wariant {w}")
    ax.legend(frameon=False, loc="lower right")
    ax.set_title("SUS wg uczestnika (kolor = wariant oceniany)")
    zapisz(fig, "sus.png")


if __name__ == "__main__":
    styl()
    print("SUS:")
    df = pd.read_csv(DANE / "sus_wyniki.csv")
    df["sus"] = df.apply(wynik_sus, axis=1)
    for wariant, g in df.groupby("wariant"):
        s = g["sus"].mean()
        print(f"  wariant {wariant}: średni SUS {s:.1f} ({ocena_slowna(s)}), n = {len(g)}")
    print(f"  ogółem: {df['sus'].mean():.1f} ({ocena_slowna(df['sus'].mean())})")
    wykres(df)
