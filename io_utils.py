import os
from models import Item


def parse_input_lines(lines):
    try:
        first_line = lines[0].strip().split()
        if len(first_line) != 2:
            raise ValueError("Pierwsza linia musi zawierać n i b.")

        n, b = int(first_line[0]), int(first_line[1])
        if n < 0 or b < 0:
            raise ValueError("Liczba przedmiotów i pojemność muszą być dodatnie.")

        items = []
        for i in range(1, n + 1):
            line = lines[i].strip().split()
            if len(line) != 2:
                raise ValueError(f"Błąd w linii {i + 1}: powinny być dwie liczby (rozmiar, wartość).")
            weight, value = int(line[0]), int(line[1])
            if weight < 0 or value < 0:
                raise ValueError("Rozmiar i wartość muszą być nieujemne.")
            items.append(Item(i, weight, value))

        return b, items
    except Exception as e:
        print(f"Błąd walidacji danych: {e}")
        return None, None


def read_from_file(filename):
    if not os.path.exists(filename):
        print(f"Plik {filename} nie istnieje.")
        return None, None
    with open(filename, 'r') as f:
        lines = f.readlines()
    return parse_input_lines(lines)


def read_from_console():
    print("Wprowadź dane")
    print('W pierwszej linii liczba przedmiotów i pojemność plecaka (n b)')
    print('W następnych liniach n razy rozmiar i wartość przedmiotu (r w)')

    lines = [input()]

    for _ in range(int(lines[0][0])):
        line = input()
        lines.append(line)
    return parse_input_lines(lines)