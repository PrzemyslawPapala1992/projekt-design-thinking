# Etap 4 – Prototyp „Kampus+”

Zasada z mapy myśli: **„myślenie rękami – nie broń pomysłu”**. Prototyp ma szybko pokazać ideę użytkownikom i zebrać opinie, nie być gotowym produktem (case study 1, krok 4).

## Poziomy prototypu

| Poziom | Forma | Kiedy | Czas |
|---|---|---|---|
| 0. Papierowy | Szkice ekranów na kartkach A5, „klikanie” przez podmianę kartek | pierwsze 2–3 testy, szybkie poprawki | 1 h |
| 1. Klikalny | `prototyp.html` – otwórz w przeglądarce (komputer lub telefon) | testy zadaniowe (`05_testowanie/`) | gotowy |
| 2. Pilotaż | jeden kurs w realnej platformie (np. Moodle z szablonem + kalendarz) | po pozytywnych testach | semestr |

## Co zawiera prototyp klikalny

- **Przełącznik wariantu A / B** – A „Oś czasu”, B „Kafelki kursów” (porównanie dwóch koncepcji pulpitu, wykład s. 25: „wybrać co najmniej 2–3 rozwiązania”).
- **Przełącznik roli** – Student / Prowadzący.
- **Podgląd telefonu** – test dla persony Marek.
- Ekrany studenta: pulpit, kurs w jednolitym szablonie (sylabus / tygodnie z mikrolekcjami / zadania / oceny / Q&A), oddanie zadania z potwierdzeniem, oceny z przewidywaną oceną, ustawienia powiadomień (TRIZ: działania impulsowe), mentor rówieśniczy, asystent FAQ, „puls tygodnia”.
- Ekrany prowadzącego: kursy, ocenianie z rubryką, kopiowanie kursu z poprzedniego semestru, wyniki pulsu.
- **Panel „Zadanie testowe”** z pomiarem czasu i eksportem wyników do CSV – moderator nie potrzebuje stopera.

Dane w prototypie są fikcyjne.

## Mapowanie: bolączka → funkcja → źródło pomysłu

| Bolączka (badania) | Funkcja | Technika, z której pochodzi |
|---|---|---|
| Terminy w wielu miejscach | Pulpit z osią terminów (A) / licznikami (B) | burza mózgów, analogia: kalendarz Google |
| Każdy kurs wygląda inaczej | Jednolity szablon kursu | TRIZ 3 lokalnej jakości |
| „Czy moje zadanie doszło?” | Potwierdzenie oddania z godziną | 5 WHY, analogia: kurier |
| Nie wiem, czy zaliczę | Przewidywana ocena i próg | 635, analogia: aplikacja bankowa |
| Nagrania 90 min, brak internetu | Mikrolekcje, transkrypcja, offline | TRIZ 1 segmentacji, 26 kopiowania |
| Spam vs przegapione terminy | Dzienne podsumowanie + push < 48 h | TRIZ 19 działań impulsowych |
| Samotność 1. roku / Erasmus | Mentor rówieśniczy | *5 steps elective*, TRIZ 22 |
| Te same pytania do dziekanatu | Asystent FAQ | TRIZ 25 samoobsługi, bionika |
| Prowadzący: podwójna praca | Kopiowanie kursu, rubryki | TRIZ 25 samoobsługi |
| Uczelnia nie wie o problemach | Puls tygodnia | TRIZ 23 sprzężenia zwrotnego |

## Czego prototyp celowo NIE robi
Prawdziwe logowanie, integracja z USOS, przechowywanie plików na serwerze, AI. To decyzje wdrożeniowe – w testach sprawdzamy **wartość i zrozumiałość**, nie technologię.
