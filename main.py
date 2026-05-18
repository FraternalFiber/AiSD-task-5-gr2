import time
import random
from models import Item
from algorithms import knapsack_dynamic, knapsack_greedy, knapsack_brute_force
from io_utils import read_from_file, read_from_console
from visualization import plot_t_vs_n, plot_t_vs_b, plot_t_vs_n_b


def generate_data(n, max_weight=50, max_value=100):
    items = []
    for i in range(1, n + 1):
        weight = random.randint(1, max_weight)
        value = random.randint(1, max_value)
        items.append(Item(i, weight, value))
    return items


def measure_time(func, *args):
    start = time.perf_counter()
    res = func(*args)
    end = time.perf_counter()
    return res, end - start


def run_experiment_and_report():
    print("\n# Raport z przeprowadzonych eksperymentów\n")

    # 1. Pojedynczy test z dokładnym raportem Markdown
    test_n = 25
    test_b = 50
    test_items = generate_data(test_n)

    print("## 1. Przykładowe dane wejściowe i wyniki pojedynczej instancji\n")
    print(f"**Pojemność plecaka (b):** {test_b}")
    print("**Parametry wejściowego zbioru przedmiotów (id, rozmiar, wartość):**")
    for item in test_items:
        print(f"- {item.id}: r={item.weight}, w={item.value}")

    # Dynamiczny (Optymalny)
    res_dp, t_dp = measure_time(knapsack_dynamic, test_items, test_b)
    val_dp, weight_dp, items_dp = res_dp

    # Zachłanny
    res_gr, t_gr = measure_time(knapsack_greedy, test_items, test_b)
    val_gr, weight_gr, items_gr = res_gr
    is_optimal = "Tak" if val_gr == val_dp else "Nie"

    # Siłowy
    res_bf, t_bf = measure_time(knapsack_brute_force, test_items, test_b)
    val_bf, weight_bf, items_bf = res_bf

    print("\n### Wyniki algorytmów:\n")
    print(
        "| Algorytm | Wybrane przedmioty (ID) | Sumaryczny rozmiar | Wartość funkcji celu | Czas działania (s) | Optymalne? |")
    print(
        "|----------|-------------------------|--------------------|----------------------|--------------------|------------|")
    print(f"| Dynamiczny | {[i.id for i in items_dp]} | {weight_dp} | {val_dp} | {t_dp:.6f} | Tak |")
    print(f"| Zachłanny | {[i.id for i in items_gr]} | {weight_gr} | {val_gr} | {t_gr:.6f} | {is_optimal} |")
    print(f"| Siłowy | {[i.id for i in items_bf]} | {weight_bf} | {val_bf} | {t_bf:.6f} | Tak |\n")

    # 2. Testy wydajnościowe

    results_n = []
    greedy_fails = 0
    total_tests = 0

    # Testy dla t=f(n), stałe b = 50
    for n in range(5, 26):
        items = generate_data(n)
        b = 50

        v_dp, _, _ = knapsack_dynamic(items, b)
        v_gr, _, _ = knapsack_greedy(items, b)
        _, t_dp = measure_time(knapsack_dynamic, items, b)
        _, t_gr = measure_time(knapsack_greedy, items, b)
        _, t_bf = measure_time(knapsack_brute_force, items, b)

        if v_gr < v_dp:
            greedy_fails += 1
        total_tests += 1

        results_n.append({'n': n, 'b': b, 't_dp': t_dp, 't_gr': t_gr, 't_bf': t_bf})

    # Testy dla t=f(b), stałe n = 15
    results_b = []
    items_fixed = generate_data(15)
    for b in range(10, 201, 10):
        _, t_dp = measure_time(knapsack_dynamic, items_fixed, b)
        _, t_gr = measure_time(knapsack_greedy, items_fixed, b)
        _, t_bf = measure_time(knapsack_brute_force, items_fixed, b)
        results_b.append({'n': 15, 'b': b, 't_dp': t_dp, 't_gr': t_gr, 't_bf': t_bf})

    # Testy t=f(n,b) dla losowych wartości
    results_nb = []
    for _ in range(30):
        n = random.randint(10, 20)
        b = random.randint(10, 100)
        items = generate_data(n)
        _, t_dp = measure_time(knapsack_dynamic, items, b)
        _, t_gr = measure_time(knapsack_greedy, items, b)
        _, t_bf = measure_time(knapsack_brute_force, items, b)
        results_nb.append({'n': n, 'b': b, 't_dp': t_dp, 't_gr': t_gr, 't_bf': t_bf})

    # Raport Markdown - teoria
    fail_percent = (greedy_fails / total_tests) * 100
    print("## 3. Wnioski\n")
    print("### Złożoność obliczeniowa zaimplementowanych algorytmów:")
    print("- **Algorytm dynamiczny:** $O(n \\cdot b)$ (Złożoność pseudowielomianowa)")
    print("- **Algorytm zachłanny:** $O(n \\log n)$ (Ze względu na czas sortowania przedmiotów)")
    print("- **Algorytm siłowy:** $O(2^n)$ (Przeszukiwanie wszystkich możliwych podzbiorów)\n")

    print("### Klasy złożoności dla problemu plecakowego 0-1:")
    print("- **Wersja decyzyjna** (czy istnieje podzbiór o wartości $\\ge V$ i wadze $\\le W$?): **NP-zupełny**")
    print("- **Wersja optymalizacyjna** (znajdź maksymalną wartość): **NP-trudny**\n")

    print("### Obserwacje dotyczące algorytmów:")
    print('Algorytm dynamiczny zawsze znajduje optymalne rozwiązanie.')
    print('- Algorytm siłowy jest bardzo nieefektywny ze względu na wykładniczą złożoność obliczeniową wynikającą ze sprawdzania wszystkich możliwych podzbiorów elementów.')
    print(
        f"- Algorytm zachłanny jest najszybszy, ale w przeprowadzonych testach (losowe dane t=f(n)) **nie znalazł rozwiązania optymalnego w {fail_percent:.2f}% przypadków**.")
    print(
        "   - Algorytm nie znajdzie optimum, gdy pozostawia w plecaku wolną przestrzeń, która mogłaby zostać wypełniona przez przedmiot o nieco gorszym stosunku wartości do rozmiaru, ale w sumie z innymi dający większą wartość końcową. Idealnym przykładem błędu jest sytuacja, gdy pojemność plecaka wynosi 50, a mamy przedmioty: A (w: 30, v: 31, ratio: 1.03) oraz dwa przedmioty B i C (w: 25, v: 25, ratio: 1). Algorytm wybierze A, a potem nie zmieści B ani C. Wynik: 31. Optymalnie jest wziąć B i C (wynik: 50.)\n")

    # Wywołanie wykresów
    plot_t_vs_n(results_n)
    plot_t_vs_b(results_b)
    plot_t_vs_n_b(results_nb)


if __name__ == "__main__":
    while True:
        print('=== MENU ===')
        choice = int(input('Wybierz opcję (1 - dane z klawiatury, 2 - testy, 3 - wyjście): '))

        if choice == 1:
            b, items = read_from_console()
            if b is not None and items:
                val, w, sel = knapsack_dynamic(items, b)
                print(f"Wartość: {val}, Waga: {w}")
                print('Wybrane przedmioty:')

                for item in sel:
                    print(f'ID: {item.id}, waga: {item.weight}, wartość: {item.value}')
        elif choice == 2:
            run_experiment_and_report()
        elif choice == 3:
            exit()