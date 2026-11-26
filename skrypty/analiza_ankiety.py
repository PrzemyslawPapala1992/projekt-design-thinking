"""Empatia: analiza ankiety studentów (dane/ankieta_wyniki.csv), wykres Likerta + podsumowanie."""
import matplotlib.pyplot as plt
import pandas as pd

from wspolne import DANE, LIKERT, NIEBIESKI, TEKST, styl, zapisz

PYTANIA = {
    "ocena_dostepu_info": "Łatwość znalezienia terminów i zadań",
    "ocena_mobile": "Wygoda na telefonie",
    "ocena_feedback": "Informacja zwrotna od prowadzących",
    "ocena_komunikacji": "Komunikacja z prowadzącymi i dziekanatem",
    "ocena_materialow": "Dostępność i jakość materiałów",
    "chce_mentor": "POMYSŁ: mentor rówieśniczy",
    "chce_mikrolekcje": "POMYSŁ: mikrolekcje + offline",
    "chce_jedna_platforma": "POMYSŁ: jedna platforma",
}
SKALA = ["1 bardzo źle", "2", "3", "4", "5 bardzo dobrze"]


def likert(df):
    """Rozbieżny wykres skumulowany: wyśrodkowany na odpowiedzi neutralnej (3)."""
    fig, ax = plt.subplots(figsize=(10, 5.2))
    etykiety = list(PYTANIA.values())
    for i, kol in enumerate(PYTANIA):
        udzialy = df[kol].value_counts(normalize=True).reindex(range(1, 6), fill_value=0).values * 100
        lewo = -(udzialy[0] + udzialy[1] + udzialy[2] / 2)
        for k in range(5):
            ax.barh(i, udzialy[k], left=lewo, color=LIKERT[k], edgecolor="white", linewidth=2, height=0.7,
                    label=SKALA[k] if i == 0 else None)
            if udzialy[k] >= 9:
                ax.text(lewo + udzialy[k] / 2, i, f"{udzialy[k]:.0f}%", ha="center", va="center", fontsize=8,
                        color="white" if k in (0, 4) else TEKST)
            lewo += udzialy[k]
    ax.axvline(0, color=TEKST, lw=0.8)
    ax.set_yticks(range(len(etykiety)), etykiety)
    ax.set_xlim(-100, 100)
    ax.set_xticks(range(-100, 101, 25), [f"{abs(x)}%" for x in range(-100, 101, 25)])
    ax.grid(axis="y", visible=False)
    ax.set_title(f"Ankieta: stan obecny i ocena pomysłów (n = {len(df)})")
    ax.legend(ncol=5, loc="lower center", bbox_to_anchor=(0.5, -0.22), frameon=False)
    zapisz(fig, "ankieta_likert.png")


def systemy(df):
    fig, ax = plt.subplots(figsize=(7, 4))
    licz = df["liczba_systemow"].value_counts().sort_index()
    ax.bar(licz.index, licz.values, color=NIEBIESKI, width=0.7)
    ax.set_xlabel("Liczba systemów/kanałów używanych do śledzenia studiów")
    ax.set_ylabel("Liczba studentów")
    ax.grid(axis="x", visible=False)
    ax.set_title(f"Ile systemów? Średnio {df['liczba_systemow'].mean():.1f}")
    zapisz(fig, "ankieta_liczba_systemow.png")


def podsumowanie(df):
    print(f"  n = {len(df)}; tryby: {df['tryb'].value_counts().to_dict()}")
    print(f"  średnia liczba systemów: {df['liczba_systemow'].mean():.1f}")
    print(f"  przegapiony termin: {(df['przegapiony_termin'] == 'tak').mean() * 100:.0f}%")
    srednie = df[list(PYTANIA)].mean().round(2)
    for kol, s in srednie.items():
        print(f"  {PYTANIA[kol]:<42} {s}")
    print("  średnie wg trybu studiów (dostęp do info / mobile):")
    print(df.groupby("tryb")[["ocena_dostepu_info", "ocena_mobile"]].mean().round(2).to_string())
    print("  najczęstsze problemy:", df["najwiekszy_problem"].value_counts().head(3).to_dict())


if __name__ == "__main__":
    styl()
    print("Ankieta:")
    df = pd.read_csv(DANE / "ankieta_wyniki.csv")
    likert(df)
    systemy(df)
    podsumowanie(df)
