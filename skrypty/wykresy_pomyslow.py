"""Ideacja: matryca wpływu i wysiłku (wykład s. 34-35) i wyniki głosowania (5 głosów na osobę)."""
import textwrap

import matplotlib.pyplot as plt
import pandas as pd

from wspolne import (DANE, NIEBIESKI, SZARY_NEUTRALNY, TEKST, TEKST_2,
                     styl, zapisz)

PROG = 5.5  # granica ćwiartek na skali 1-10
TOP_N = 10


def wczytaj():
    return pd.read_csv(DANE / "pomysly.csv")


def matryca(df):
    top = set(df.nlargest(TOP_N, "glosy")["id"])
    fig, ax = plt.subplots(figsize=(10, 7.5))
    ax.axvline(PROG, color=TEKST_2, lw=1, ls="--")
    ax.axhline(PROG, color=TEKST_2, lw=1, ls="--")
    etykiety = [(1.2, 9.8, "SZYBKIE WYGRANE\nduży wpływ, mały wysiłek"),
                (9.8, 9.8, "PROJEKTY STRATEGICZNE\nduży wpływ, duży wysiłek"),
                (1.2, 1.2, "DROBNE USPRAWNIENIA\nmały wpływ, mały wysiłek"),
                (9.8, 1.2, "POCHŁANIACZE CZASU\nmały wpływ, duży wysiłek")]
    for x, y, t in etykiety:
        ax.text(x, y, t, ha="left" if x < 5 else "right", va="top" if y > 5 else "bottom",
                fontsize=9, color=TEKST_2, fontweight="bold")
    # lekki rozrzut, żeby punkty o tych samych ocenach się nie zasłaniały
    przesuniecia = {}
    for _, r in df.iterrows():
        klucz = (r.wysilek, r.wplyw)
        k = przesuniecia.get(klucz, 0)
        przesuniecia[klucz] = k + 1
        dx = [0, 0.28, -0.28, 0, 0][k % 5]
        dy = [0, 0, 0, 0.28, -0.28][k % 5]
        wybrany = r.id in top
        ax.scatter(r.wysilek + dx, r.wplyw + dy, s=60 + r.glosy * 40,
                   color=NIEBIESKI if wybrany else SZARY_NEUTRALNY,
                   edgecolor="white", linewidth=2, zorder=3)
        ax.text(r.wysilek + dx, r.wplyw + dy, str(r.id), ha="center", va="center",
                fontsize=7.5, color="white" if wybrany else TEKST, zorder=4, fontweight="bold")
    ax.set_xlim(0.5, 10.5)
    ax.set_ylim(0.5, 10.5)
    ax.set_xlabel("Wysiłek wdrożenia (1 = mały, 10 = duży)")
    ax.set_ylabel("Wpływ na problem (1 = mały, 10 = duży)")
    ax.set_title("Matryca wpływu i wysiłku – 30 pomysłów (rozmiar = liczba głosów)")
    ax.scatter([], [], s=200, color=NIEBIESKI, label=f"top {TOP_N} wg głosów")
    ax.scatter([], [], s=200, color=SZARY_NEUTRALNY, label="pozostałe")
    ax.legend(loc="lower center", bbox_to_anchor=(0.5, -0.16), ncol=2, frameon=False)
    legenda = "\n".join(f"{r.id:>2}. {textwrap.shorten(r.pomysl, 58)}" for _, r in df.iterrows())
    fig.text(0.92, 0.5, legenda, fontsize=6.8, va="center", family="DejaVu Sans Mono", color=TEKST_2)
    zapisz(fig, "matryca_wplyw_wysilek.png")


def glosowanie(df):
    d = df.nlargest(TOP_N, "glosy").sort_values("glosy")
    fig, ax = plt.subplots(figsize=(9, 5.5))
    ax.barh([textwrap.shorten(p, 60) for p in d.pomysl], d.glosy, color=NIEBIESKI, height=0.7)
    for i, v in enumerate(d.glosy):
        ax.text(v + 0.1, i, str(v), va="center", color=TEKST, fontsize=9)
    ax.set_xlabel("Liczba głosów")
    ax.grid(axis="y", visible=False)
    ax.set_title(f"Głosowanie – top {TOP_N} pomysłów (każdy uczestnik: 5 głosów)")
    zapisz(fig, "glosowanie.png")


def szybkie_wygrane(df):
    sw = df[(df.wplyw > PROG) & (df.wysilek <= PROG)].sort_values(["glosy", "wplyw"], ascending=False)
    print("  Szybkie wygrane:", ", ".join(f"#{i}" for i in sw.id))


if __name__ == "__main__":
    styl()
    print("Pomysły:")
    df = wczytaj()
    matryca(df)
    glosowanie(df)
    szybkie_wygrane(df)
