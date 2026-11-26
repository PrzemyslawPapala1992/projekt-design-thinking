# Badania: wywiady, ankieta, obserwacja

Kolejność zgodna z wykładem (s. 8): **desk research → techniki obserwacyjne i jakościowe → badania ilościowe**.

## 1. Desk research (1–2 h, cały zespół)
- Jakie systemy używa dziś nasza uczelnia (USOS, Moodle, Teams, poczta)? Zróbcie listę i zrzuty ekranu.
- Przegląd rozwiązań: Moodle, Canvas, Google Classroom, MS Teams for Education, Blackboard, Duolingo (analogia: mikrolekcje, powiadomienia), Notion/Todoist (analogia: listy zadań).
- Wnioski z 3 case studies (patrz `00_analiza_materialow.md`).

## 2. Wywiady pogłębione (5–8 osób, 20–30 min)
Rekrutacja: min. 2 studentów stacjonarnych, 2 niestacjonarnych, 1 z zagranicy / 1. roku, 2 prowadzących, 1 osoba z dziekanatu.

Zasady: pytamy o **konkretne sytuacje z przeszłości**, nie o opinie o hipotetycznych funkcjach; nie sugerujemy rozwiązań; notujemy dosłowne cytaty; oddzielamy **fakty od interpretacji** (ćwiczenie z *5 steps elective*).

### Scenariusz – student
1. Opowiedz o swoim ostatnim tygodniu na studiach. Skąd wiedziałeś/aś, co masz zrobić?
2. Z jakich systemów i kanałów korzystasz? Pokaż na telefonie (obserwacja!).
3. Opowiedz o ostatniej sytuacji, gdy przegapiłeś/aś termin albo prawie przegapiłeś/aś. Co się stało?
4. Kiedy ostatnio szukałeś/aś materiału z zajęć? Ile to trwało? Gdzie był?
5. Gdzie i na jakim urządzeniu się uczysz? O której?
6. Jak dowiadujesz się, ile masz punktów i czy zaliczysz przedmiot?
7. Co robisz, gdy masz pytanie do prowadzącego? Ile czekasz na odpowiedź?
8. Jak się czujesz, kiedy otwierasz Moodle / USOS? (technika **sortowania obrazów**: pokaż 8 kart z emocjami, poproś o wybór 2)
9. Gdybyś miał/a czarodziejską różdżkę – co jedno zmieniłbyś/zmieniłabyś?
10. Kogo jeszcze powinniśmy zapytać?

### Scenariusz – prowadzący
1. Jak wygląda przygotowanie kursu na nowy semestr? Ile to trwa?
2. Jak przekazuje Pan/Pani studentom materiały, terminy, zmiany?
3. Jak wygląda ocenianie zadań – od oddania do wpisu w USOS?
4. Jakie pytania od studentów powtarzają się najczęściej?
5. Skąd Pan/Pani wie, czy studenci rozumieją materiał w trakcie semestru?
6. Co w obecnych narzędziach najbardziej przeszkadza? Co działa dobrze i trzeba zachować?
7. Jak radzi sobie Pan/Pani z niesamodzielnymi pracami (ściąganie, AI)?

### Arkusz notatek (jedna osoba pyta, druga notuje)
| Cytat (dosłownie) | Fakt / interpretacja | Emocja | Bolączka | Potrzeba |
|---|---|---|---|---|

## 3. Obserwacja / „przechwytywanie klientów” (wykład s. 10)
Poproście 3 studentów, by przy was wykonali: *znajdź termin najbliższego zadania z dowolnego przedmiotu* i *znajdź materiał z ostatniego wykładu*. Mierzcie czas i liczbę kliknięć/systemów. To **pomiar stanu wyjściowego** – w testach prototypu porównacie z nim wynik.

## 4. Ankieta ilościowa (min. 30 osób, Google/MS Forms)
Skala 1–5 (1 = bardzo źle, 5 = bardzo dobrze), wzorem case study 3. Kolumny są zgodne z `dane/ankieta_wyniki.csv`, więc wyniki z formularza można wkleić i uruchomić skrypt.

| Kolumna CSV | Pytanie |
|---|---|
| `tryb` | Tryb studiów (stacjonarne / niestacjonarne / wymiana) |
| `rok` | Rok studiów (1–5) |
| `liczba_systemow` | Z ilu różnych systemów/kanałów korzystasz, by śledzić studia? (liczba) |
| `przegapiony_termin` | Czy w tym semestrze przegapiłeś/aś termin przez brak informacji? (tak/nie) |
| `ocena_dostepu_info` | Jak oceniasz łatwość znalezienia informacji o terminach i zadaniach? |
| `ocena_materialow` | Jak oceniasz dostępność i jakość materiałów online? |
| `ocena_mobile` | Jak oceniasz wygodę korzystania z platform na telefonie? |
| `ocena_feedback` | Jak oceniasz szybkość i jakość informacji zwrotnej od prowadzących? |
| `ocena_komunikacji` | Jak oceniasz komunikację z prowadzącymi i dziekanatem? |
| `chce_jedna_platforma` | Jak oceniasz pomysł jednej platformy zamiast kilku systemów? |
| `chce_mikrolekcje` | Jak oceniasz pomysł krótkich lekcji (5–10 min) z transkrypcją i trybem offline? |
| `chce_mentor` | Jak oceniasz pomysł mentora rówieśniczego ze starszego roku? |
| `najwiekszy_problem` | (otwarte) Jaki jest Twój największy problem z obecnymi platformami? |

## 5. Synteza badań
Po badaniach: każda obserwacja na osobnej karteczce → grupowanie podobnych (technika **„las i drzewa”** z wykładu: pojedyncze karteczki = drzewa, wspólne wątki = las) → poprawione persony i mapa podróży → przejście do `02_definiowanie/`.
