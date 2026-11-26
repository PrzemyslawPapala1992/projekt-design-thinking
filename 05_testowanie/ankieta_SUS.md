# Ankieta SUS (System Usability Scale) – wersja polska

Skala: 1 = zdecydowanie się nie zgadzam … 5 = zdecydowanie się zgadzam. Odpowiedzi wpisz do `dane/sus_wyniki.csv` (kolumny `q1`–`q10`).

| Nr | Stwierdzenie |
|---|---|
| q1 | Myślę, że chciałbym/chciałabym często korzystać z tej platformy. |
| q2 | Platforma wydała mi się niepotrzebnie skomplikowana. |
| q3 | Platforma była łatwa w użyciu. |
| q4 | Myślę, że potrzebowałbym/potrzebowałabym pomocy technicznej, by z niej korzystać. |
| q5 | Funkcje platformy były dobrze zintegrowane. |
| q6 | Platforma wydawała się niespójna. |
| q7 | Myślę, że większość osób szybko nauczyłaby się z niej korzystać. |
| q8 | Platforma była niewygodna w użyciu. |
| q9 | Czułem/czułam się pewnie, korzystając z platformy. |
| q10 | Musiałem/musiałam się wiele nauczyć, zanim zacząłem/zaczęłam z niej korzystać. |

**Liczenie wyniku:** pytania nieparzyste: (odpowiedź − 1); parzyste: (5 − odpowiedź); suma × 2,5 → wynik 0–100. Średnia rynkowa ≈ 68. Skrypt `skrypty/sus.py` liczy to automatycznie.

Pytania dodatkowe (otwarte):
1. Co było najbardziej przydatne?
2. Co było mylące?
3. Czego brakowało?
