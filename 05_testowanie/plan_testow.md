# Etap 5 – Testowanie

Zasady z wykładu (s. 26–28) i mapy myśli: testujemy **w środowisku użycia, z potencjalnymi użytkownikami, z otwartą głową**; grupy dobrane według profilu; **ta sama metodologia** dla wszystkich grup, żeby wyniki były porównywalne; szukamy uwag **uniwersalnych** (we wszystkich grupach) i **specyficznych** (tylko w jednej grupie). Jeśli żaden prototyp nie spełnia celów – **wracamy** do wcześniejszego etapu.

## 1. Uczestnicy (min. 10 osób)

| Grupa | Liczba | Urządzenie | Odpowiada personie |
|---|---|---|---|
| Studenci stacjonarni | 3–4 | laptop | Kasia |
| Studenci niestacjonarni / pracujący | 3–4 | **telefon** | Marek |
| Student 1. roku lub z zagranicy | 1–2 | telefon | Ahmed |
| Prowadzący | 2 | laptop (rola Prowadzący) | dr Anna |

**Kolejność wariantów:** połowa uczestników zaczyna od A, połowa od B (eliminuje efekt uczenia się).

## 2. Przebieg sesji (25 min)

1. Wstęp (2 min): „Testujemy prototyp, nie Ciebie. Myśl na głos.” Zgoda na notatki.
2. Zadania T1–T5 w wariancie 1 (8 min) – moderator mierzy czas w panelu „Zadanie testowe” w prototypie.
3. Zadania T1–T5 w wariancie 2 (6 min).
4. Ankieta SUS dla wariantu, który uczestnik wolał (3 min) – `ankieta_SUS.md`.
5. Wywiad pogłębiający (5 min): Który wariant i dlaczego? Czego brakowało? Czy zamieniłbyś obecne systemy na to?
6. Technika **głosowania** (wykład s. 11): oceń w skali 1–10 każdą z funkcji: oś terminów, szablon kursu, mikrolekcje, przewidywana ocena, mentor, asystent FAQ.

## 3. Zadania testowe (student)

| ID | Zadanie | Kryterium sukcesu | Cel czasu |
|---|---|---|---|
| T1 | Sprawdź, co masz do oddania w tym tygodniu | wskazuje poprawnie wszystkie zadania | < 30 s |
| T2 | Oddaj zadanie z Baz danych | widzi potwierdzenie oddania | < 60 s |
| T3 | Znajdź mikrolekcję z tygodnia 3 z Design Thinking i pobierz ją offline | pobieranie uruchomione | < 60 s |
| T4 | Sprawdź, ile punktów brakuje Ci do zaliczenia Sieci komputerowych | podaje poprawną liczbę | < 45 s |
| T5 | Zadaj pytanie o termin poprawki | uzyskuje odpowiedź w asystencie lub wysyła pytanie | < 60 s |

Zadania dla prowadzącego: P1 – skopiuj kurs z poprzedniego semestru; P2 – oceń zadanie za pomocą rubryki; P3 – sprawdź, który temat studenci uznali za najtrudniejszy w pulsie tygodnia.

## 4. Metryki i kryteria decyzji

| Metryka | Jak mierzymy | Próg „działa” |
|---|---|---|
| Skuteczność | % zadań zakończonych sukcesem bez pomocy | ≥ 80% |
| Czas | mediana czasu na zadanie (eksport CSV z prototypu) | w celach z tabeli |
| SUS | 10 pytań, wynik 0–100 (`skrypty/sus.py`) | ≥ 68 |
| Preferencja | który wariant wybrał uczestnik | > 60% na jeden wariant = wyraźny zwycięzca |
| Porównanie ze stanem obecnym | czas T1 vs pomiar „przechwytywania klientów” z etapu 1 | co najmniej 3× szybciej |

**Decyzje:**
- Oba warianty poniżej progów → wracamy do **Definiowania** (czy dobrze zrozumieliśmy problem?).
- Zadanie z niską skutecznością w obu wariantach → poprawka funkcji (ideacja dla tego zadania).
- Wyraźny zwycięzca → rozwijamy go, dobieramy najlepsze elementy przegranego (np. kafelki jako drugi widok).

## 5. Arkusz obserwacji (jeden na uczestnika)

| Uczestnik | Grupa | Wariant | Zadanie | Czas | Sukces (T/N/z pomocą) | Gdzie się zawahał | Cytat |
|---|---|---|---|---|---|---|---|

## 6. Analiza
1. Wyeksportuj CSV z prototypu każdego testera → połącz w `dane/testy_wyniki.csv` (kolumny: uczestnik,wariant,zadanie,czas_s,sukces).
2. Wpisz odpowiedzi SUS do `dane/sus_wyniki.csv`.
3. `python skrypty/generuj_wszystko.py` – wykresy czasów, skuteczności i SUS.
4. Tabela uwag: *uniwersalne* (≥ 3 grupy) vs *specyficzne* (1 grupa) – zgodnie z wykładem s. 27.
