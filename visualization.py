import matplotlib.pyplot as plt


def plot_t_vs_n(results):
    """
    Wykres czau obliczeń (t) od liczby przedmiotów (n) przy stałej pojemności plecaka (b)
    """
    ns = [r['n'] for r in results]
    t_dp = [r['t_dp'] for r in results]
    t_gr = [r['t_gr'] for r in results]
    t_bf = [r['t_bf'] for r in results]

    plt.figure(figsize=(8, 5))
    plt.plot(ns, t_dp, label='Dynamiczny', marker='o')
    plt.plot(ns, t_gr, label='Zachłanny', marker='s')
    plt.plot(ns, t_bf, label='Siłowy', marker='^')

    plt.yscale('log')
    plt.xlabel('Liczba przedmiotów (n)')
    plt.ylabel('Czas obliczeń [s] (skala logarytmiczna)')
    plt.title('Czas obliczeń (t) od liczby przedmiotów (n) przy stałej pojemności plecaka (b)')
    plt.legend()
    plt.grid(True)
    plt.savefig('plots/t_vs_n.png')
    plt.show()


def plot_t_vs_b(results):
    """
    Wykres czasu obliczeń (t) od pojemności plecaka (b) przy stałej liczbie przedmiotów (n)
    """
    bs = [r['b'] for r in results]
    t_dp = [r['t_dp'] for r in results]
    t_gr = [r['t_gr'] for r in results]
    t_bf = [r['t_bf'] for r in results]

    plt.figure(figsize=(8, 5))
    plt.plot(bs, t_dp, label='Dynamiczny', marker='o')
    plt.plot(bs, t_gr, label='Zachłanny', marker='s')
    plt.plot(bs, t_bf, label='Siłowy', marker='^')

    plt.xlabel('Pojemność plecaka (b)')
    plt.ylabel('Czas obliczeń [s]')
    plt.title('Czas obliczeń (t) od pojemności plecaka (b) przy stałej liczbie przedmiotów (n)')
    plt.legend()
    plt.grid(True)
    plt.savefig('plots/t_vs_b.png')
    plt.show()


def plot_t_vs_n_b(results):
    """
    Wykresy 3D
    """
    ns = [r['n'] for r in results]
    bs = [r['b'] for r in results]
    t_dp = [r['t_dp'] for r in results]
    t_gr = [r['t_gr'] for r in results]
    t_bf = [r['t_bf'] for r in results]

    # Wykres 1: Algorytm dynamiczny
    fig1 = plt.figure(figsize=(8, 6))
    ax1 = fig1.add_subplot(111, projection='3d')
    ax1.scatter(ns, bs, t_dp, c='r', marker='o')
    ax1.set_xlabel('Liczba przedmiotów (n)')
    ax1.set_ylabel('Pojemność plecaka (b)')
    ax1.set_zlabel('Czas obliczeń [s]', labelpad=13)
    ax1.set_title('Algorytm dynamiczny: t = f(n, b)')
    fig1.savefig('plots/t_vs_n_b_dynamiczny.png')

    # Wykres 2: Algorytm zachłanny
    fig2 = plt.figure(figsize=(8, 6))
    ax2 = fig2.add_subplot(111, projection='3d')
    ax2.scatter(ns, bs, t_gr, c='g', marker='s')
    ax2.set_xlabel('Liczba przedmiotów (n)')
    ax2.set_ylabel('Pojemność plecaka (b)')
    ax2.set_zlabel('Czas obliczeń [s]')
    ax2.set_title('Algorytm zachłanny: t = f(n, b)')
    fig2.savefig('plots/t_vs_n_b_zachlanny.png')

    # Wykres 3: Algorytm siłowy
    fig3 = plt.figure(figsize=(8, 6))
    ax3 = fig3.add_subplot(111, projection='3d')
    ax3.scatter(ns, bs, t_bf, c='b', marker='^')
    ax3.set_xlabel('Liczba przedmiotów (n)')
    ax3.set_ylabel('Pojemność plecaka (b)')
    ax3.set_zlabel('Czas obliczeń [s]')
    ax3.set_title('Algorytm siłowy: t = f(n, b)')
    fig3.savefig('plots/t_vs_n_b_silowy.png')

    plt.show()