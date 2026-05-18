# Raport - problem plecakowy

## 1. Przykładowe dane wejściowe i wyniki dla pojedynczej instancji

**Pojemność plecaka (b):** 50  
**Parametry wejściowego zbioru przedmiotów (id, rozmiar, wartość):**
- 1: r=38, w=79
- 2: r=29, w=6
- 3: r=19, w=53
- 4: r=43, w=18
- 5: r=35, w=32
- 6: r=9, w=22
- 7: r=13, w=34
- 8: r=22, w=22
- 9: r=19, w=23
- 10: r=34, w=18
- 11: r=24, w=79
- 12: r=2, w=18
- 13: r=48, w=82
- 14: r=46, w=72
- 15: r=29, w=85
- 16: r=3, w=21
- 17: r=32, w=86
- 18: r=39, w=36
- 19: r=1, w=68
- 20: r=3, w=71
- 21: r=36, w=8
- 22: r=45, w=42
- 23: r=4, w=45
- 24: r=40, w=91
- 25: r=16, w=80

### Wyniki algorytmów:

| Algorytm   | Wybrane przedmioty (ID)     | Sumaryczny rozmiar | Wartość funkcji celu | Czas działania (s) | Optymalne? |
|------------|-----------------------------|--------------------|----------------------|--------------------|------------|
| Dynamiczny | [25, 23, 20, 19, 12, 11]    | 50                 | 361                  | 0.000397           | Tak        |
| Zachłanny  | [19, 20, 23, 12, 16, 25, 3] | 48                 | 356                  | 0.000020           | Nie        |
| Siłowy     | [11, 12, 19, 20, 23, 25]    | 50                 | 361                  | 26.988199          | Tak        |

## 3. Wykresy

![Wykres t = f(n)](/plots/t_vs_n.png)
![Wykres t = f(b)](/plots/t_vs_b.png)
![Wykres t = f(n, b) - algorytm dynamiczny](/plots/t_vs_n_b_dynamiczny.png)
![Wykres t = f(n, b) - algorytm zachłanny](/plots/t_vs_n_b_zachlanny.png)
![Wykres t = f(n, b) - algorytm siłowy](/plots/t_vs_n_b_silowy.png)

## 4. Wnioski

### Złożoność obliczeniowa zaimplementowanych algorytmów:
- **Algorytm dynamiczny:** $O(n \cdot b)$ (Złożoność pseudowielomianowa)
- **Algorytm zachłanny:** $O(n \log n)$ (Ze względu na czas sortowania przedmiotów)
- **Algorytm siłowy:** $O(2^n)$ (Przeszukiwanie wszystkich możliwych podzbiorów)

### Klasy złożoności dla problemu plecakowego 0-1:
- **Wersja decyzyjna** (czy istnieje podzbiór o wartości $\ge V$ i wadze $\le W$?): **NP-zupełny**
- **Wersja optymalizacyjna** (znajdź maksymalną wartość): **NP-trudny**

### Obserwacje dotyczące algorytmów:
Algorytm dynamiczny zawsze znajduje optymalne rozwiązanie.
- Algorytm siłowy jest bardzo nieefektywny ze względu na wykładniczą złożoność obliczeniową wynikającą ze sprawdzania wszystkich możliwych podzbiorów elementów.
- Algorytm zachłanny jest najszybszy, ale w przeprowadzonych testach (losowe dane t=f(n)) **nie znalazł rozwiązania optymalnego w 42.86% przypadków**.
  - Algorytm nie znajdzie optimum, gdy pozostawia w plecaku wolną przestrzeń, która mogłaby zostać wypełniona przez przedmiot o nieco gorszym stosunku wartości do rozmiaru, ale w sumie z innymi dający większą wartość końcową. Idealnym przykładem błędu jest sytuacja, gdy pojemność plecaka wynosi 50, a mamy przedmioty: A (w: 30, v: 31, ratio: 1.03) oraz dwa przedmioty B i C (w: 25, v: 25, ratio: 1). Algorytm wybierze A, a potem nie zmieści B ani C. Wynik: 31. Optymalnie jest wziąć B i C (wynik: 50.)
