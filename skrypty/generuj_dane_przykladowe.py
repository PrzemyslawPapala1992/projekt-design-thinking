"""Tworzy PRZYKŁADOWE (losowe, fikcyjne) dane ankiety, testów i SUS, żeby skrypty miały na czym działać.

Nie nadpisuje istniejących plików, chyba że podasz --nadpisz.
Po wpisaniu prawdziwych wyników usuń plik dane/PRZYKLADOWE.txt – zniknie znak wodny z wykresów.
"""
import sys

import numpy as np
import pandas as pd

from wspolne import DANE, ZNACZNIK_PRZYKLADU

rng = np.random.default_rng(7)
NADPISZ = "--nadpisz" in sys.argv


def zapisz_csv(df, nazwa):
    sciezka = DANE / nazwa
    if sciezka.exists() and not NADPISZ:
        print(f"  pomijam {nazwa} (istnieje; użyj --nadpisz)")
        return False
    df.to_csv(sciezka, index=False, encoding="utf-8")
    print(f"  utworzono {nazwa} ({len(df)} wierszy)")
    return True


def likert(srednia, n):
    return np.clip(np.rint(rng.normal(srednia, 0.9, n)), 1, 5).astype(int)


def ankieta(n=40):
    tryb = rng.choice(["stacjonarne", "niestacjonarne", "wymiana"], n, p=[0.55, 0.35, 0.10])
    problemy = ["terminy w różnych miejscach", "brak wersji na telefon", "długie nagrania",
                "brak informacji zwrotnej", "nie wiem, ile mam punktów", "za dużo haseł i systemów"]
    return pd.DataFrame({
        "tryb": tryb,
        "rok": rng.integers(1, 6, n),
        "liczba_systemow": rng.integers(2, 7, n),
        "przegapiony_termin": rng.choice(["tak", "nie"], n, p=[0.4, 0.6]),
        "ocena_dostepu_info": likert(2.3, n),
        "ocena_materialow": likert(2.9, n),
        "ocena_mobile": likert(2.0, n),
        "ocena_feedback": likert(2.4, n),
        "ocena_komunikacji": likert(2.7, n),
        "chce_jedna_platforma": likert(4.4, n),
        "chce_mikrolekcje": likert(4.0, n),
        "chce_mentor": likert(3.4, n),
        "najwiekszy_problem": rng.choice(problemy, n),
    })


def testy():
    cele = {"T1": 30, "T2": 60, "T3": 60, "T4": 45, "T5": 60}
    wiersze = []
    for u in range(1, 11):
        for wariant, mnoznik in (("A", 0.8), ("B", 1.1)):
            for zad, cel in cele.items():
                czas = max(6, rng.normal(cel * mnoznik * 0.8, cel * 0.25))
                sukces = int(rng.random() < (0.9 if wariant == "A" else 0.78))
                wiersze.append((f"U{u:02d}", wariant, zad, round(czas, 1), sukces))
    return pd.DataFrame(wiersze, columns=["uczestnik", "wariant", "zadanie", "czas_s", "sukces"])


def sus():
    wiersze = []
    for u in range(1, 11):
        wariant = "A" if rng.random() < 0.7 else "B"
        dobry = 4.2 if wariant == "A" else 3.6
        odp = [int(np.clip(round(rng.normal(dobry if i % 2 == 0 else 6 - dobry, 0.7)), 1, 5)) for i in range(10)]
        wiersze.append([f"U{u:02d}", wariant, *odp])
    return pd.DataFrame(wiersze, columns=["uczestnik", "wariant"] + [f"q{i}" for i in range(1, 11)])


if __name__ == "__main__":
    print("Generuję dane przykładowe:")
    utworzone = [zapisz_csv(ankieta(), "ankieta_wyniki.csv"),
                 zapisz_csv(testy(), "testy_wyniki.csv"),
                 zapisz_csv(sus(), "sus_wyniki.csv")]
    if any(utworzone):
        ZNACZNIK_PRZYKLADU.write_text(
            "Dane w tym folderze (ankieta, testy, SUS, głosy i oceny pomysłów) są PRZYKŁADOWE.\n"
            "Po wpisaniu prawdziwych wyników usuń ten plik – zniknie znak wodny z wykresów.\n",
            encoding="utf-8")
