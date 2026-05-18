import matplotlib.pyplot as plt
import numpy as np


def plot_t_vs_n(results):
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
    plt.title('t = f(n) przy stałym b')
    plt.legend()
    plt.grid(True, which="both", ls="--")
    plt.show()


def plot_t_vs_b(results):
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
    plt.title('t = f(b) przy stałym n')
    plt.legend()
    plt.grid(True)
    plt.show()


def plot_t_vs_n_b(results):
    ns = [r['n'] for r in results]
    bs = [r['b'] for r in results]
    t_dp = [r['t_dp'] for r in results]

    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(ns, bs, t_dp, c='r', marker='o', label='Dynamiczny')

    ax.set_xlabel('Liczba przedmiotów (n)')
    ax.set_ylabel('Pojemność plecaka (b)')
    ax.set_zlabel('Czas obliczeń [s]')
    ax.set_title('t = f(n, b) dla algorytmu dynamicznego')
    plt.legend()
    plt.show()