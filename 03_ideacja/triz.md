# TRIZ dla platformy e-learningowej

Na podstawie: H. Obora, *Metoda twórczego rozwiązywania problemów TRIZ*, Zeszyty Naukowe UEK nr 775, 2008.

TRIZ to narzędzie **systematyczno-analityczne** – uzupełnia intuicyjną burzę mózgów. Pomaga uciec od **„wektora inercji”** (szukania rozwiązań tylko w dotychczasowym doświadczeniu – u nas: „zróbmy kolejnego Moodle’a, tylko ładniejszego”).

## 1. Idealny wynik końcowy (IFR)

> **Student nigdy nie szuka informacji – właściwa informacja sama do niego trafia we właściwym momencie, na urządzeniu, które ma w ręku, a prowadzący nie wykonuje w tym celu żadnej dodatkowej pracy.**

Cechy IFR (Obora, s. 125): eliminuje wady stanu obecnego (rozproszenie), zachowuje zalety (swoboda prowadzącego, istniejący USOS), nie komplikuje, nie wprowadza nowych wad (np. spamu powiadomień).

Strategia **wyniku idealnego** (wykład s. 22): od IFR idziemy wstecz – co musi być prawdą, żeby to działało? → dane o terminach w jednym miejscu → wprowadzane raz przez prowadzącego → a najlepiej kopiowane automatycznie z poprzedniego roku z przesunięciem dat.

## 2. Sprzeczności i zasady innowacyjności

| # | Sprzeczność (poprawiamy X, pogarsza się Y) | Zasada TRIZ (nr z tabeli 1) | Rozwiązanie w Kampus+ |
|---|---|---|---|
| 1 | **Spójność** dla studenta (każdy kurs wygląda tak samo) ↔ **swoboda** prowadzącego | 3 Lokalnej jakości, 1 Segmentacji | Stały „szkielet” kursu (sylabus, terminy, oceny, Q&A) + swobodny środek tygodnia (dowolne materiały, kolejność) |
| 2 | **Więcej powiadomień** (nikt nie przegapi) ↔ **mniej szumu** (nikt nie wyłączy) | 19 Działań impulsowych, 23 Sprzężenia zwrotnego | Dzienne podsumowanie o 7:00 + push tylko < 48 h przed terminem i przy zmianie terminu; student sam ustawia próg |
| 3 | **Bogate materiały** (wideo) ↔ **słaby internet / telefon / brak czasu** | 1 Segmentacji, 26 Kopiowania, 34 Odrzucenia i regeneracji | Mikrolekcje 5–10 min, transkrypcja jako „tania kopia” wideo, pobieranie offline, automatyczne usuwanie obejrzanych plików |
| 4 | **Więcej feedbacku** dla studenta ↔ **mniej pracy** prowadzącego | 25 Samoobsługi, 6 Uniwersalności | Rubryki (jedna rubryka = ocena + komentarz), quizy sprawdzane automatycznie, ocena koleżeńska w projektach, komentarz audio 30 s zamiast pisania |
| 5 | **Weryfikacja samodzielności** ↔ **zaufanie i prywatność** (bez kamer i proctoringu) | 13 Wykonania na odwrót | Zamiast pilnować wyniku – oceniać proces: wersje pracy w platformie + 5-min obrona ustna |
| 6 | **Odpowiedzi na pytania 24/7** ↔ **ograniczony czas dziekanatu i prowadzących** | 10 Zapobiegania, 25 Samoobsługi | FAQ budowane z najczęstszych pytań (zasada „śladu feromonowego”), asystent odpowiada zanim pytanie trafi do człowieka |
| 7 | **Nowa platforma** ↔ **koszt i ryzyko wymiany istniejących systemów** | 24 Pośrednictwa, 5 Łączenia | Kampus+ jako „warstwa” nad USOS/Moodle/Teams (integracje, SSO) – nie zastępuje ich od razu |
| 8 | **Wsparcie dla 1. roku / Erasmus** ↔ **brak etatów na opiekunów** | 22 Zamiany strat na korzyści, 8 Przeciwwagi | Starsi studenci jako mentorzy rówieśniczy (dla nich: punkty ECTS/zaświadczenie – materiał *5 steps elective*) |
| 9 | **Kontrola jakości zajęć** ↔ **brak oceniania prowadzących „po fakcie”** | 23 Sprzężenia zwrotnego, 19 Działań impulsowych | Cotygodniowy anonimowy „puls” (3 pytania) widoczny dla prowadzącego od razu, zamiast jednej ankiety na koniec semestru |

## 3. ARIZ w skrócie – zastosowanie do sprzeczności nr 1

1. **Sformułowanie zadania:** studenci gubią się, bo każdy kurs ma inną strukturę; prowadzący nie chcą narzuconego układu.
2. **Założenia:** nie zmieniamy treści zajęć ani metod prowadzącego; zmieniamy strukturę prezentacji informacji.
3. **Analiza:** IFR – „struktura kursu tworzy się sama z tego, co prowadzący i tak robi”. Element, który nie spełnia funkcji: menu kursu (dowolne). Przyczyna: brak pól obowiązkowych.
4. **Ocena:** ryzyko – prowadzący uzna szablon za ograniczenie → wariant: szablon wypełnia się automatycznie (terminy z zadań, oceny z rubryk), prowadzący dodaje tylko treść.
5. **Stadium operacyjne:** porównanie z Canvas (moduły), Google Classroom (strumień) – nasz wyróżnik: wspólny widok terminów ze **wszystkich** kursów.
6. **Synteza:** szablon kursu = 5 stałych zakładek + dowolne bloki w tygodniach.

Ogólny schemat ARIZ (Obora, rys. 3): *problem konkretny → abstrakcja (sprzeczność spójność/swoboda) → rozwiązanie ogólne (lokalna jakość) → analogia → rozwiązanie konkretne (szkielet + swobodny środek)*.
