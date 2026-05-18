import itertools


def knapsack_dynamic(items, capacity):
    """Algorytm programowania dynamicznego"""
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        item = items[i - 1]
        for w in range(capacity + 1):
            if item.weight <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - item.weight] + item.value)
            else:
                dp[i][w] = dp[i - 1][w]

    # Odtwarzanie wybranych przedmiotów
    res = dp[n][capacity]
    w = capacity
    selected_items = []

    for i in range(n, 0, -1):
        if res <= 0:
            break
        if res == dp[i - 1][w]:
            continue
        else:
            item = items[i - 1]
            selected_items.append(item)
            res -= item.value
            w -= item.weight

    total_weight = sum(i.weight for i in selected_items)
    total_value = sum(i.value for i in selected_items)
    return total_value, total_weight, selected_items


def knapsack_greedy(items, capacity):
    """Algorytm zachłanny sortujący po opłacalności"""
    sorted_items = sorted(items, key=lambda x: x.ratio, reverse=True)

    total_value = 0
    total_weight = 0
    selected_items = []

    for item in sorted_items:
        if total_weight + item.weight <= capacity:
            selected_items.append(item)
            total_weight += item.weight
            total_value += item.value

    return total_value, total_weight, selected_items


def knapsack_brute_force(items, capacity):
    """Algorytm siłowy"""
    max_value = 0
    best_combination = []

    # Generowanie wszystkich podzbiorów
    for r in range(len(items) + 1):
        for combination in itertools.combinations(items, r):
            current_weight = sum(item.weight for item in combination)
            current_value = sum(item.value for item in combination)

            if current_weight <= capacity and current_value > max_value:
                max_value = current_value
                best_combination = list(combination)

    total_weight = sum(item.weight for item in best_combination)
    return max_value, total_weight, best_combination