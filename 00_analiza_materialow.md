# Analiza materiałów zajęciowych pod kątem tematu 7

## 1. Przegląd plików

| Plik | O czym jest | Co bierzemy do projektu „Platforma e-learningowa” |
|---|---|---|
| **Zagadnienia do rozwiązania metodą DT.pdf** | Lista 10 tematów | Temat 7: *Platforma e-learningowa dla uczelni wyższej* |
| **Techniki Design Thinking w teorii i praktyce – wykład.pdf** | Założenia DT, 5 etapów pracy zespołu (Ingle 2015), techniki badawcze, techniki kreatywne, strategie twórcze, techniki „biznesowe” (mapa empatii, customer journey, mapa kontekstowa, 3-12-3, matryca wpływu i wysiłku, las i drzewa, 20-20, kręgi wpływów), sieci społeczne | Szkielet procesu i niemal wszystkie narzędzia, których używamy w kolejnych folderach |
| **mapa myśli.jpg** | Sketchnote „Etapy Design Thinking” (K. Suślik): Empatia – „wejdź w buty klienta”, Synteza – wyzwanie projektowe, Ideacja – „ilość nie jakość”, Prototyp – „myślenie rękami, nie broń”, Testowanie – „w środowisku użycia, z otwartą głową” | Nazewnictwo etapów i zasady pracy (ilość pomysłów, szybkie prototypy, testy u realnych użytkowników) |
| **Case study DT – Studia Marzeń.pdf** | Przykładowy projekt studentów: mapa empatii studenta, 5 WHY, burza mózgów + głosowanie 5 głosami, prototyp; testowanie pominięte | Wzór dokumentacji. **Ważne:** pomysł „Jeden system do prowadzenia zajęć, oddawania zadań, komunikacji student/prowadzący” – dokładnie nasz temat. Uczymy się na ich błędzie: **my testowanie robimy** |
| **Design thinking – case study 2.pdf** | Persona „Inż. Dominik, 22 l., PWr”, mapa empatii (bolączki: sprzeczne informacje, brak feedbacku, terminy, za dużo teorii), quick thinking 8 osób | Bolączki studenta, które platforma może rozwiązać: *sprzeczne informacje, terminy, brak feedbacku, materiały do nauki*. Pomysł „Stworzenie jednolitej platformy nauczania” |
| **Design thinking – case study 3.pdf** | „Higher Education of the Future” (PWr, międzynarodowy zespół): mapa empatii, **diagram rybiej ości (Fishbone)**, 74 → 13 rozwiązań, prototyp programu, **ankieta 35 studentów** | Fishbone jako technika definiowania problemu; wątek *Lack of online sources*, *Unified platform for whole university with mobile application* zamiast „jsos, eportal, edukacja”; wzór metodologii testów ankietowych |
| **Metoda TRIZ.pdf** (H. Obora, 2008) | TRIZ: wektor inercji, idealny wynik końcowy (IFR), sprzeczności, 40 zasad innowacyjności, algorytm ARIZ | Systematyczno-analityczne narzędzie ideacji: znajdujemy sprzeczności w platformie (np. elastyczność vs spójność) i rozwiązujemy je zasadami TRIZ |
| **5 steps elective.pdf** (R. Bucur, Univ. of Groningen) | Metodologia nauczania/mentoringu w 5 krokach (Winkelaar), **peer mentoring** – starszy student wspiera młodszego (wsparcie akademickie i emocjonalne), fakty vs interpretacje | Funkcja „Mentor rówieśniczy” w platformie; spojrzenie od strony **prowadzącego** jako użytkownika |
| **Me_We.png** | Model warstwowy: Me → We → Discovery → Experimentation → Consolidation → Value for others (tożsamość, ryzyko, porażka, prototyp, test, feedback) | Opis pracy naszego zespołu i dojrzewania pomysłu; slajd w prezentacji |
| **Elevator pitch.jpg** | 4 kroki pitchu: przedstaw się → co robisz → czego chcesz → wezwanie do działania | Struktura 60-sekundowej prezentacji rozwiązania (`06_prezentacja/elevator_pitch.md`) |
| **Kursy.txt** | Wymóg ukończenia kursu online | Osobne zaliczenie, nie część projektu |

## 2. Mapa: etap DT → techniki z materiałów → gdzie w projekcie

| Etap | Techniki (źródło) | Plik w projekcie |
|---|---|---|
| 1. Empatia / zrozumienie | desk research, badania sondażowe, wywiady („przechwytywanie klientów”), grupy fokusowe, sortowanie obrazów, mapa empatii, mapa podróży klienta, mapa kontekstowa, perspektywa interesariuszy, kręgi wpływów (wykład) | `01_empatyzacja/*` |
| 2. Definiowanie | 5 WHY (wykład, CS1), Fishbone (CS3), las i drzewa (wykład), POV + „Jak moglibyśmy” | `02_definiowanie/*` |
| 3. Ideacja | burza mózgów, brainwriting, 635, 3-12-3, kwiat lotosu, analogie, synektyka, TRIZ/IFR, strategia nadmiaru, kula armatnia, głosowanie, matryca wpływu i wysiłku | `03_ideacja/*` |
| 4. Prototyp | wybór 2–3 rozwiązań (wykład s.25), low-fi → klikalny prototyp | `04_prototyp/*` |
| 5. Testowanie | grupy testowe wg profilu, testy wirtualne/terenowe, porównanie wg jednej metodologii, elementy uniwersalne vs specyficzne, powrót do wcześniejszych etapów (wykład s.26–28); ankieta (CS3) | `05_testowanie/*` |
| Prezentacja | elevator pitch, Me–We | `06_prezentacja/*` |

## 3. Wnioski z case studies istotne dla naszego tematu

1. **We wszystkich trzech case studies pojawia się postulat jednej, spójnej platformy** (CS1: „jeden system do prowadzenia zajęć, oddawania zadań, komunikacji”; CS2: „jednolita platforma nauczania”; CS3: „unified platform with mobile application” zamiast kilku systemów). To mocny sygnał z badań innych zespołów – a nasz temat pozwala pójść głębiej.
2. Powtarzające się bolączki studentów: **rozproszone i sprzeczne informacje, terminy, brak informacji zwrotnej, materiały nieprzystające do praktyki, stres i samotność** (zwłaszcza pierwszy rok i studenci z zagranicy).
3. Case study 1 **pominęło testowanie** – to najsłabszy punkt tamtego projektu. Nasza przewaga: klikalny prototyp + test zadaniowy + ankieta SUS.
4. Case study 3 pokazuje dobrą praktykę: *74 pomysły → 13 wybranych → prototyp → ankieta oceniająca stan obecny i propozycje*. Powielamy schemat (strategia nadmiaru → selekcja).
5. Materiał „5 steps” przypomina, że **prowadzący też jest użytkownikiem** – platforma, która dociąża wykładowców, nie zostanie przez nich przyjęta (mechanizm „podporządkowania” zamiast „internalizacji” z wykładu, s.5). Dlatego do badań włączamy prowadzących i dziekanat.

## 4. Możliwe kierunki rozwiązania (szeroka przestrzeń, zanim zawęzimy)

| Kierunek | Opis | Dla kogo |
|---|---|---|
| A. **Jedno źródło prawdy** | Pulpit „Co dziś / ten tydzień” zbierający terminy, zmiany sal, ogłoszenia ze wszystkich kursów; integracja z USOS / Teams / kalendarzem | studenci |
| B. **Standard kursu** | Wspólny szkielet każdego kursu (sylabus, warunki zaliczenia, tygodnie, zadania, oceny) + dowolność w środku | studenci, prowadzący |
| C. **Nauka mobilna i asynchroniczna** | Mikrolekcje 5–10 min, nagrania z transkrypcją i napisami, tryb offline, PWA | niestacjonarni, pracujący |
| D. **Szybki feedback** | Rubryki ocen, komentarze audio, automatycznie sprawdzane quizy, przewidywanie oceny końcowej | studenci, prowadzący |
| E. **Społeczność i wsparcie** | Forum Q&A kursu, mentor rówieśniczy, grupy projektowe, dostęp do pomocy psychologicznej | 1. rok, Erasmus |
| F. **Mniej pracy dla prowadzącego** | Kopiowanie kursu z poprzedniego roku, bank pytań, masowe ocenianie, szablony | prowadzący |
| G. **Sprzężenie zwrotne do uczelni** | Cotygodniowy anonimowy „puls” kursu, panel jakości dla prowadzącego | uczelnia, prowadzący |
| H. **Praktyka** | Projekty z firmami, portfolio studenta, odznaki kompetencji | studenci, pracodawcy |

W `03_ideacja/` te kierunki są rozwijane i oceniane; do prototypu trafiają **A + B + C + D** (rdzeń), a **E** jako rozszerzenie.
