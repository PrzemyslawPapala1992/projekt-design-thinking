# Etap 3 – Ideacja

Zasady z „mapy myśli”: **ilość, nie jakość**, bez krytyki w fazie generowania. Strategia z wykładu: **strategia nadmiaru** (dużo pomysłów → później selekcja), wzorem case study 3 (74 → 13).

Proponowany przebieg warsztatu (ok. 90 min):

| Czas | Technika (wykład) | Wejście | Wyjście |
|---|---|---|---|
| 10 min | Rozgrzewka: **myślenie lateralne** – „platforma, która nie wymaga logowania” / „uczelnia bez maili” | – | luźne skojarzenia |
| 18 min | **3-12-3**: 3 min pomysły indywidualnie, 12 min łączenie w podgrupach, 3 min prezentacja | pytania HMW 1–3 | 2–3 koncepcje na podgrupę |
| 30 min | **Metoda 635** (6 osób × 3 pomysły × 5 min, kartki krążą) – przy mniejszej grupie: **brainwriting** | pytania HMW 4–7 | do 108 pomysłów |
| 15 min | **Kwiat lotosu** (poniżej) | centrum: „Kampus+” | 64 pomysły cząstkowe |
| 10 min | **TRIZ** – rozwiązywanie sprzeczności (`triz.md`) | sprzeczności | pomysły „nieoczywiste” |
| 10 min | **Głosowanie** – każdy 5 głosów (jak CS1) + **matryca wpływu i wysiłku** | lista pomysłów | wybór do prototypu |
| – | **Kula armatnia** (wykład s. 12) – moderator „bombarduje” 3 wybrane pomysły pytaniami krytycznymi | top 3 | lista ryzyk |

## 1. Kwiat lotosu (wykład s. 19)

Centrum: **Kampus+**. 8 płatków = problemy cząstkowe; każdy rozwijamy w kolejny „kwiat” z 8 pomysłami. Poniżej po 4 przykładowe pomysły na płatek (dopiszcie resztę na warsztacie).

| Płatek | Przykładowe pomysły |
|---|---|
| 1. Terminy | oś czasu; eksport do kalendarza; odliczanie; zmiana terminu = powiadomienie wszystkich |
| 2. Materiały | szablon tygodnia; wyszukiwarka pełnotekstowa; wersjonowanie; „co nowego od ostatniej wizyty” |
| 3. Nauka mobilna | mikrolekcje; offline; transkrypcje; prędkość odtwarzania i zakładki |
| 4. Ocenianie | rubryki; komentarze audio; przewidywana ocena; potwierdzenie oddania |
| 5. Komunikacja | Q&A kursu; FAQ dziekanatu; jeden kanał ogłoszeń; PL/EN |
| 6. Społeczność | mentor rówieśniczy; grupy projektowe; wydarzenia roku; tablica „szukam zespołu” |
| 7. Prowadzący | kopiowanie kursu; bank pytań; eksport ocen do USOS; szablony |
| 8. Jakość | puls tygodnia; panel trudności; ankieta końcowa z widocznymi skutkami; statystyki pytań |

## 2. Metoda analogii i analizy znanych systemów (wykład s. 16)

| Znany system | Co działa | Przeniesienie do Kampus+ |
|---|---|---|
| Duolingo | krótkie lekcje, przypomnienia, poczucie postępu | mikrolekcje + quiz + pasek postępu |
| Aplikacja bankowa | „saldo” widoczne od razu po zalogowaniu | „saldo punktów” i przewidywana ocena na pulpicie |
| Kurier (śledzenie paczki) | status przesyłki i potwierdzenia | status zadania: wysłane → odebrane → ocenione |
| Booksy | rezerwacja wolnego slotu | konsultacje w slotach |
| Spotify offline | pobierz i słuchaj bez sieci | pobieranie lekcji offline |
| Kalendarz Google | jeden widok z wielu kalendarzy | oś czasu z wszystkich kursów |
| **Bionika** – mrówki (ślad feromonowy) | najczęściej używane ścieżki się wzmacniają | najczęstsze pytania automatycznie trafiają do FAQ kursu |

## 3. Bank pomysłów i selekcja

Pełna lista 30 pomysłów z kierunkiem (A–H z `00_analiza_materialow.md`), techniką, głosami i oceną wpływu/wysiłku: `dane/pomysly.csv`.
Wykresy: `python skrypty/generuj_wszystko.py` → `wizualizacje/matryca_wplyw_wysilek.png`, `wizualizacje/glosowanie.png`.

**Matryca wpływu i wysiłku** (wykład s. 34–35): ćwiartka *wysoki wpływ / niski wysiłek* = „szybkie wygrane” – trafiają do prototypu w pierwszej kolejności. *Wysoki wpływ / wysoki wysiłek* = projekty strategiczne (np. SSO + USOS) – w prototypie tylko udajemy integrację.

### Wybór do prototypu (wykład s. 25: „wybrać co najmniej 2–3 rozwiązania”)

Wynik na **przykładowych** danych (po waszej sesji przelicz skryptem):

| Priorytet | Pomysły | Uzasadnienie |
|---|---|---|
| Rdzeń (w obu wariantach prototypu) | #1 oś terminów, #3 szablon kursu, #5 powiadomienia, #9 panel postępu, #12 potwierdzenie oddania | najwięcej głosów, wysoki wpływ, niski/średni wysiłek |
| Nauka mobilna | #6 mikrolekcje, #7 transkrypcje, #8 offline | odpowiedź na personę Marek |
| Prowadzący | #4 kopiowanie kursu, #10 rubryki, #17 puls tygodnia | bez tego brak adopcji przez prowadzących |
| Wsparcie | #14 FAQ dziekanatu, #15 mentor rówieśniczy | persony Ahmed, 1. rok |
| Odłożone (backlog) | #19 SSO/USOS (wysoki wysiłek – etap wdrożenia), #22 projekty z firmami, #28 VR | poza zakresem prototypu |

**Dwa alternatywne prototypy do porównania** (rdzeń ten sam, inny pulpit):
- **Wariant A – „Oś czasu”**: pulpit to chronologiczna lista wszystkiego, co trzeba zrobić (Dziś / Jutro / Ten tydzień).
- **Wariant B – „Kafelki kursów”**: pulpit to kafelki przedmiotów z licznikami zadań i postępem (bliżej dzisiejszego Moodle).
