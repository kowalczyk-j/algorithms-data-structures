from abc import ABC, abstractmethod
from cmath import e
from autograd import grad
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate


class Solver(ABC):

    @abstractmethod
    def get_parameters(self):
        ...

    @abstractmethod
    def solve(self, problem, x0, learn_rate, tol, *args, **kwargs):
        ...


class Gradient_Descent(Solver):
    """Algorytm gradientu prostego, który dla zadanej funkcji (problem)
    punktu początkowego (x0), wartości kroku ß (learn_rate), 
    dozwolonej tolerancji pomiędzy różnicami xt a xt+1 (tol)
    oraz dozwoloną max liczbą iteracji (max_iterations)
    wylicza minimum funkcji korzystając ze wzoru
    xt+1 = xt - ß*∇q(xt)"""

    def __init__(self, problem, x0, learn_rate=0.1, tol=0.1e-04, max_iterations=10000):
        self.problem = problem
        self.x0 = x0
        self.learn_rate = learn_rate
        self.tol = tol
        self.max_iter = max_iterations

    def get_parameters(self):
        """Zwraca słownik parametrów."""
        return {
            "problem": self.problem,
            "x0": self.x0,
            "learn rate": self.learn_rate,
            "tolerance": self.tol,
            "max iterations": self.max_iter
        }

    def solve(self):
        steps = [self.x0]
        x = self.x0.astype(float)
        gradient = grad(self.problem)
        for _ in range(self.max_iter):
            diff = self.learn_rate*gradient(x)
            x = x - diff
            steps.append(x)
            if np.all(np.abs(diff) < self.tol):
                break
        return steps, x


def func_f(x):
    return 0.25*(x[0]**4)


def func_g(x):
    # x = x.astype(float)
    # return 2 - np.exp(-x[0]**2 - x[1]**2) - 0.5*np.exp(-(x[0]+1.5)**2 - (x[1]-2)**2)
    return 2 - e**(-x[0]**2 - x[1]**2) - 0.5*e**(-(x[0]+1.5)**2 - (x[1]-2)**2)


def func_test(x):
    return x[0]**2 + x[0]*x[1] + 2*x[0] + x[1]**2


def plotter(steps, beta):
    """Tworzy wykres zmieniających się wartości xt w kolejnych iteracjach."""
    plt.plot([i for i in range(len(steps))], steps)
    plt.xlabel('Liczba iteracji')
    plt.grid(True)
    plt.legend(['x' + str(i+1) for i in range(len(steps[0]))], title="Zmienne")
    plt.title(f"Parametr kroku = {beta}")
    plt.show()


def generate_random_points(dimension=1, up_bound=3.5, amount=50):
    """Generuje wektory typu float o zadanym wymiarze oraz granicy <-up_bound, up_bound>
    oraz segreguje je względem odległości od początku układu współrzędnych."""
    x = [np.round(np.random.uniform(-up_bound, up_bound, dimension), 2)
         for _ in range(amount)]

    def sort_key(x):
        k = 0
        for i in range(dimension):
            k += x[i]**2
        return k
    points = sorted(x, key=sort_key)
    return points


def generate_tabular_data(num_of_points, problem, dim=1, tol=0.1e-04, max_iter=10000):
    """Tworzy tabelaryczne zestawienie liczby iteracji i wartości końcowej
    algorytmu dla losowo wygenerowanych punktów i wartości kroków 0.01, 0.21, ... , 0.81"""
    points = generate_random_points(dimension=dim, amount=num_of_points)
    data = []
    for point in points:
        point_data = [point]
        for step in np.arange(0.01, 1, 0.2):
            solver = Gradient_Descent(problem, point, step, tol, max_iter)
            steps, minimum = solver.solve()
            point_data.append((len(steps)-1, tuple(np.around(minimum, 4))))
        data.append(point_data)
    return tabulate(data,
                    headers=["Punkt\n(x1, ..., xn)", "Krok 0.01\n(Iteracje, wynik)", "Krok 0.21", "Krok 0.41", "Krok 0.61", "Krok 0.81"])


if __name__ == "__main__":
    # generowanie wykresu
    step = 0.61
    solver = Gradient_Descent(func_f, np.array([1.1]), step)
    steps, x = solver.solve()
    plotter(steps, step)

    # generowanie tabeli
    # print(generate_tabular_data(num_of_points=20, problem=func_f, dim=1))
