# Zadania do zrobienia – dzisiaj (max 1 h)

Zespół: **Przemek**, **Rafał**, **Szymon**.
Cel: zamienić losowe dane przykładowe na **spójne, zmyślone i zanonimizowane dane**, przeliczyć wykresy i wrzucić do repo.

Pracujecie **równolegle**, każdy ok. **45 min** na swoich plikach (brak konfliktów w gicie), ostatnie 10–15 min Przemek składa całość.

**Skrót:** nie piszemy danych od zera – skrypt `generuj_dane_przykladowe.py` już tworzy dane, my je tylko **poprawiamy**, żeby pasowały do jednej historii.

---

## Wspólne zasady (2 min)

1. **Anonimizacja:** zamiast osób tylko identyfikatory – wywiady `W01`–`W04`, ankieta `R01`–`R40`, testy `U01`–`U10`. Żadnych imion, maili, rozpoznawalnych cytatów.
2. **Jedna historia danych** (żeby wyniki się nie wykluczały):
   - średnio ok. **4 systemy**, ok. **35–40%** przegapiło termin przez brak informacji,
   - najgorzej oceniana **wygoda na telefonie**, najlepiej pomysł **jednej platformy**,
   - w testach **wariant A wygrywa**, najsłabsze zadania to **T4** i **T5**.
3. W README i prezentacji piszemy, że dane są **symulowane na potrzeby ćwiczenia**.
4. Git: `git pull` na start → pracujesz → `git add <swoje pliki>` → `commit` → `push`.

---

## Przemek – ankieta + złożenie całości (ok. 45 min)

| # | Zadanie | Plik | Czas |
|---|---|---|---|
| P1 | `python skrypty/generuj_dane_przykladowe.py --nadpisz`, potem w Excelu/edytorze poprawić kilka wierszy, żeby liczby pasowały do historii (sprawdzić skryptem `python skrypty/analiza_ankiety.py`) | `dane/ankieta_wyniki.csv` | 15 min |
| P2 | Zapisać 4–5 najważniejszych liczb z wyniku skryptu (średnia liczba systemów, % przegapionych terminów, średnie ocen) | `01_empatyzacja/wyniki_badan.md` (nowy) | 10 min |
| P3 | **Po pushach Rafała i Szymona:** `git pull`, usunąć `dane/PRZYKLADOWE.txt`, w README zamienić uwagę o danych przykładowych na „dane symulowane”, `python skrypty/generuj_wszystko.py`, rzut oka na wykresy, commit + push | `README.md`, `wizualizacje/*.png` | 15 min |
| P4 | Wpisać liczby do elevator pitcha (`[X]`, `[Y]`, `[Z]`, `[W]`) | `06_prezentacja/prezentacja.md` | 5 min |

## Rafał – wywiady i definiowanie (ok. 45 min)

| # | Zadanie | Plik | Czas |
|---|---|---|---|
| R1 | Notatki z **4 zmyślonych wywiadów** (`W01` stacjonarny, `W02` niestacjonarny, `W03` Erasmus, `W04` prowadzący): profil w 1 linii + 3 wiersze tabeli *cytat / emocja / bolączka / potrzeba* | `01_empatyzacja/wywiady.md` (nowy) | 25 min |
| R2 | Pod wywiadami: krótka synteza – 3–4 wspólne wątki i które wywiady je potwierdzają, plus pomiar stanu obecnego (ile trwało znalezienie terminu w obecnych systemach, np. 1,5–3 min) | `01_empatyzacja/wywiady.md` | 10 min |
| R3 | Przy każdej personie dopisać jedną linię „**Weryfikacja:** potwierdzone w W0x / nowa obserwacja” | `01_empatyzacja/persony.md` | 10 min |

## Szymon – prototyp, testy i głosowanie (ok. 45 min)

| # | Zadanie | Plik | Czas |
|---|---|---|---|
| S1 | Przeklikać `04_prototyp/prototyp.html` (oba warianty, obie role, też na telefonie) i spisać błędy w punktach | `05_testowanie/uwagi_do_prototypu.md` (nowy) | 15 min |
| S2 | Poprawić wygenerowane `testy_wyniki.csv` i `sus_wyniki.csv`, żeby pasowały do historii (A szybszy i lepiej oceniany, T4 i T5 najsłabsze); sprawdzić `python skrypty/analiza_testow.py` i `python skrypty/sus.py` | `dane/testy_wyniki.csv`, `dane/sus_wyniki.csv` | 15 min |
| S3 | Głosy w `pomysly.csv`: warsztat 6 osób × 5 głosów, więc suma kolumny `glosy` = 30 (najwięcej #1, #3, #9) | `dane/pomysly.csv` | 5 min |
| S4 | 5–6 zdań wniosków z testów: który wariant wygrywa, co poprawić | `05_testowanie/wyniki_testow.md` (nowy) | 10 min |

---

## Plan godziny

| Minuta | Co |
|---|---|
| 0–2 | Wszyscy: zasady + `git pull` |
| 2–45 | Każdy swoją część, push po skończeniu |
| 45–60 | Przemek: P3–P4 (złożenie całości), reszta zerka na wykresy |

## Później (nie dziś)
- Prezentacja 12 slajdów: Przemek 1–4, Rafał 5–8, Szymon 9–12.
- Aktualizacja tablicy `IDEAS` w `wizualizacje/tablica-projektu.html` po zmianie głosów (Szymon).
- Druga ścieżka 5 WHY w `02_definiowanie/definiowanie_problemu.md` (Rafał).
- Kurs z `Kursy.txt` – każdy indywidualnie.
