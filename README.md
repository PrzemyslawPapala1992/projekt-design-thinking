# Projekt DT nr 7 – Platforma e-learningowa dla uczelni wyższej

Roboczy tytuł rozwiązania: **„Kampus+” – jedna platforma, w której student w 30 sekund wie, co, do kiedy i jak ma zrobić.**

Projekt jest prowadzony metodą Design Thinking według 5 etapów z wykładu (Ingle, 2015) i z „mapy myśli” (Empatia → Synteza/Definiowanie → Ideacja → Prototyp → Testowanie). Każdy etap ma swój folder: co robimy, jakimi technikami (z materiałów zajęciowych) i jaki jest wynik.

## Struktura folderu

| Folder / plik | Co zawiera |
|---|---|
| `00_analiza_materialow.md` | Co wynika z każdego pliku w materiałach i jak to wykorzystać w temacie 7 |
| `01_empatyzacja/` | Persony, mapy empatii, scenariusz wywiadu, ankieta, mapa podróży studenta, mapa kontekstowa, interesariusze |
| `02_definiowanie/` | 5 Why, diagram Ishikawy (rybia ość), definicja problemu (POV), pytania „Jak moglibyśmy…?” |
| `03_ideacja/` | Burza mózgów / 635 / 3-12-3, kwiat lotosu, TRIZ (sprzeczności + 40 zasad + IFR), analogie, głosowanie, matryca wpływu i wysiłku |
| `04_prototyp/` | Opis 2 wariantów prototypu, klikalny prototyp HTML (`prototyp.html`) |
| `05_testowanie/` | Plan testów, scenariusze zadań, kryteria sukcesu, ankieta SUS, arkusz obserwacji |
| `06_prezentacja/` | Elevator pitch (4 kroki), model Me–We dla zespołu, szkielet prezentacji końcowej |
| `skrypty/` | Skrypty Python: matryca wpływu/wysiłku, wyniki głosowania, analiza ankiety, wynik SUS |
| `dane/` | Pliki CSV z pomysłami i (przykładowymi) odpowiedziami z ankiety – do podmiany na wasze dane |
| `wizualizacje/` | `tablica-projektu.html` (wszystkie diagramy w jednym miejscu) + wygenerowane wykresy PNG |

## Jak pracować z tym materiałem w grupie

1. **Najpierw przeczytajcie** `00_analiza_materialow.md` i `01_empatyzacja/persony.md`.
2. **Przeprowadźcie prawdziwe badania** – 5–8 wywiadów (scenariusz w `01_empatyzacja/scenariusz_wywiadu.md`) + ankietę wśród studentów. Persony w tym folderze są *hipotezami startowymi* – po wywiadach poprawcie je.
3. Wpiszcie wyniki ankiety do `dane/ankieta_wyniki.csv` i pomysły z waszej burzy mózgów do `dane/pomysly.csv`, a potem uruchomcie skrypty:
   ```bash
   cd projekt-design-thinking/skrypty
   python generuj_wszystko.py
   ```
   Wykresy pojawią się w `wizualizacje/`.
4. Prototyp: otwórzcie `04_prototyp/prototyp.html` w przeglądarce – są w nim dwa warianty (A: „Oś czasu”, B: „Kafelki kursów”) do testów porównawczych.
5. Testy: według `05_testowanie/plan_testow.md`.
6. Prezentacja: `06_prezentacja/`.

> **Uwaga:** liczby w `dane/ankieta_wyniki.csv`, głosy i oceny w `dane/pomysly.csv` są **przykładowe** (wymyślone na potrzeby szablonu). Przed oddaniem projektu zastąpcie je wynikami z waszych badań i sesji – inaczej wnioski będą fikcyjne.

## Inny wymóg z materiałów

`Kursy.txt` to osobne zadanie zaliczeniowe (nie część projektu DT): ukończenie kursu Coursera „Creative thinking techniques and tools for success” **lub** Navoica „Process and Product Design in the Conditions of Industry 4.0”.
