# Etap 2 – Definiowanie problemu

## 1. Technika 5 WHY (wykład s. 12, case study 1)

Objaw obserwowany w badaniach: **„Student nie oddał zadania na czas, choć miał je zrobione.”**

| # | Dlaczego? | Odpowiedź |
|---|---|---|
| 1 | Dlaczego nie oddał zadania na czas? | Bo był przekonany, że termin jest w piątek, a był w środę. |
| 2 | Dlaczego miał błędną informację? | Bo termin podano ustnie na zajęciach, a w Moodle była stara data z poprzedniego roku. |
| 3 | Dlaczego w systemie była stara data? | Bo prowadzący skopiował kurs i nie zaktualizował dat; ogłosił zmianę tylko na Teams. |
| 4 | Dlaczego prowadzący używa kilku kanałów i nie aktualizuje dat? | Bo platforma jest niewygodna (aktualizacja dat zadanie po zadaniu), a uczelnia nie ma jednego standardu komunikacji. |
| 5 | Dlaczego nie ma standardu i wygodnego narzędzia? | Bo systemy wdrażano osobno, pod potrzeby administracji (USOS – oceny, Moodle – pliki, Teams – zajęcia zdalne), **a nie pod codzienną pracę studenta i prowadzącego**. |

**Przyczyna źródłowa:** brak jednego, wygodnego dla obu stron „źródła prawdy” o kursie. Problem nie jest „lenistwem studentów”, tylko architekturą informacji.

Druga ścieżka 5 WHY do przeprowadzenia w grupie: *„Student niestacjonarny rezygnuje ze studiów po 1. semestrze”* (hipoteza: materiały niedopasowane do nauki mobilnej w krótkich blokach czasu + samotność).

## 2. Diagram Ishikawy / rybia ość (case study 3)

**Głowa ryby (skutek):** *Studenci i prowadzący nie korzystają efektywnie z e-learningu uczelni.*

| Kategoria (ość) | Przyczyny |
|---|---|
| **Technologia** | kilka niepołączonych systemów; brak wersji mobilnej / offline; brak SSO (wiele haseł); słaba wyszukiwarka |
| **Treści** | nagrania 90 min bez rozdziałów; PDF-y skanów; brak transkrypcji i napisów; materiały nieaktualizowane |
| **Komunikacja** | ogłoszenia w wielu kanałach; brak potwierdzeń; maile z tymi samymi pytaniami; tylko po polsku |
| **Prowadzący** | brak czasu i szkoleń; podwójna praca (Moodle + USOS + Excel); każdy organizuje kurs inaczej |
| **Studenci** | praca zawodowa, mało czasu; 1. rok – nie znają systemów; brak nawyków samoorganizacji; samotność |
| **Procesy / organizacja** | brak standardu kursu; ocenianie nie ma terminu; brak pętli informacji zwrotnej (ankiety raz na semestr, bez skutków – CS1) |

Wizualizacja diagramu: `wizualizacje/tablica-projektu.html`.

## 3. Definicja problemu – Point of View (POV)

> **[Student – zwłaszcza pracujący i 1. roku]** potrzebuje **[w każdej chwili, także na telefonie, wiedzieć, co, do kiedy i jak ma zrobić oraz gdzie stoi z zaliczeniem]**, ponieważ **[dziś informacje są rozproszone w 4–6 kanałach i bywają sprzeczne, co powoduje stres, przegapione terminy i rezygnację]**.

> **[Prowadzący]** potrzebuje **[przekazać informacje i dać feedback raz, w jednym miejscu, bez dodatkowej pracy]**, ponieważ **[obecnie dubluje pracę w kilku systemach i odpowiada na powtarzalne pytania]**.

**Wyzwanie projektowe (jedno zdanie):** *Zaprojektować platformę e-learningową, która jest jedynym źródłem prawdy o kursie dla studenta i nie zwiększa pracy prowadzącego.*

## 4. Pytania „Jak moglibyśmy…?” (HMW) – wejście do ideacji

1. Jak moglibyśmy sprawić, by informacja o terminie **sama znalazła studenta** we właściwym momencie?
2. Jak moglibyśmy pozwolić prowadzącym zachować własny styl, a studentom dać **ten sam układ w każdym kursie**?
3. Jak moglibyśmy umożliwić naukę w **10-minutowych okienkach** w pociągu bez internetu?
4. Jak moglibyśmy skrócić czas od oddania zadania do **informacji zwrotnej** – bez dociążania prowadzącego?
5. Jak moglibyśmy pokazać studentowi **w każdej chwili, czy zaliczy**?
6. Jak moglibyśmy sprawić, by student 1. roku i z zagranicy **nie czuł się sam**?
7. Jak moglibyśmy, by uczelnia **dowiadywała się o problemach w trakcie semestru**, a nie po?

## 5. Miary sukcesu (wykład: „określone są tylko miary postępu prac”)

| Miara | Stan wyjściowy (zmierzyć w badaniach) | Cel dla prototypu |
|---|---|---|
| Czas znalezienia najbliższego terminu | np. 2–3 min, 2–3 systemy | < 30 s, 1 system |
| Skuteczność zadań testowych | – | ≥ 80% bez pomocy |
| Wynik SUS | – | ≥ 68 (powyżej przeciętnej) |
| Liczba systemów używanych do śledzenia studiów | średnio ~4 (ankieta) | 1 + kalendarz |
| Przegapione terminy z powodu braku informacji | % z ankiety | spadek o połowę (do weryfikacji w pilotażu) |
