from abc import ABC, abstractmethod
from numpy.random import randint
from numpy.random import rand
from numpy.random import choice
from numpy import mean
from numpy import arange
import matplotlib.pyplot as plt

class Solver(ABC):

    @abstractmethod
    def get_parameters(self):
        ...

    @abstractmethod
    def solve(self, problem, pop0, *args, **kwargs):
        ...


class GeneticAlgorithm(Solver):
    """Algorytm genetyczny z selekcją ruletkową, krzyżowaniem jednopunktowym oraz sukcesją generacyjną.
    pop - population, ind - individual, prob - probability"""

    def __init__(self, iter_number=75, cross_prob=0.9, mut_prob=0.005, pop_number=50, bits_number=200):
        self._iter_number = iter_number
        self._cross_prob = cross_prob
        self._mut_prob = mut_prob
        self._pop_number = pop_number
        self._bits_number = bits_number

    def get_parameters(self):
        """Zwraca słownik hiperparametrów."""
        return{
            "iterations number": self._iter_number,
            "crossover probability": self._cross_prob,
            "mutation probability": self._mut_prob,
            "population number": self._pop_number,
            "individual's length": self._bits_number
        }

    def generate_random_population(self):
        """Inicjalizuje populację początkową o zadanym rozmiarze i liczbie genów osobnika"""
        return [randint(0, 2, self._bits_number).tolist() for _ in range(self._pop_number)]

    def crossover(self, ind1, ind2):
        """Krzyżuje dwóch osobników względem losowo wybranego punktu (poza skrajnymi)."""
        if rand() < self._cross_prob:
            point = randint(1, len(ind1)-2)
            return [ind1[:point] + ind2[point:], ind2[:point] + ind1[point:]]
        return [ind1, ind2]

    def mutation(self, ind):
        """Mutuje geny pojedynczego osobnika."""
        for i in range(len(ind)):
            if rand() < self._mut_prob:
                ind[i] = int(not ind[i])
        return ind

    def selection(self, pop, problem):
        """Selekcjonuje nową populację metodą ruletkową
        z odpowiednio przeskalowanymi wartościami dla ujemnych wyników."""
        const = abs(min([problem(i) for i in pop]))+1
        # wartości funkcji celu tylko dodatnie
        values = [problem(i)+const for i in pop]
        min_val = min(values)
        max_val = max(values)
        for i in range(len(values)):
            if max_val == min_val:
                values[i] = 1
            else:
                values[i] = (values[i] - min_val)/(max_val -
                                                   min_val)  # normalizacja wartości
        val_sum = sum(values)
        # obliczenie prawdopodobieństw wystąpienia
        selection_probs = [value/val_sum for value in values]
        return [pop[choice(len(pop), p=selection_probs)] for _ in range(self._pop_number)]

    def evaluation(self, problem, pop):
        """Wybiera najepszego osobnika z populacji."""
        best_ind, best_score = 0, problem(pop[0])
        scores = [problem(ind) for ind in pop]
        for i in range(self._pop_number):
            if scores[i] > best_score:
                best_ind, best_score = pop[i], scores[i]
        return best_ind, best_score

    def solve(self, problem, pop0, *args, **kwargs):
        best_ind, best_score = self.evaluation(problem, pop0)
        for generation in range(self._iter_number):
            selected = self.selection(pop0, objective_f)
            next_generation = []
            for i in range(0, self._pop_number, 2):
                ind1, ind2 = selected[i], selected[i+1]
                for new_ind in self.crossover(ind1, ind2):
                    self.mutation(new_ind)
                    next_generation.append(new_ind)
            evaluation = self.evaluation(problem, pop0)
            if best_score > evaluation[1]:
                best_ind, best_score = evaluation
            pop0 = next_generation  # sukcesja generacyjna
        return [best_ind, best_score]


def objective_f(x):
    """Funkcja celu - symulacja lądowania rakiety."""
    speed = 0
    mass = 200 + sum(x)
    height = 200
    for step in x:
        acceleration = (45 / mass)*step - 0.09
        # jeżeli silnik był włączony przysp. się zwieksza, jeśli nie - pomniejsza o grawitację
        mass -= step    # pomniejszenie masy o zużyte paliwo
        speed += acceleration
        height += speed
        if height < 2 and abs(speed) < 2:
            return 2000 - sum(x)
        elif height < 0:
            return -1000 - sum(x)
    return -1000 - sum(x)

def plotter(parameters, mean_values):
    """Tworzy wykres zmieniających się wartości xt w kolejnych iteracjach."""
    plt.plot(parameters, mean_values, 'ro')
    plt.xlabel('Prawdopodobieństwo krzyżowania')
    plt.ylabel('Średnia wartość funkcji celu')
    plt.grid(True)
    plt.show()

def evaluate_best_cross_prob(steps, n=100):
    """Badanie efektywności różnych wartości cross_prob na wykresach"""
    means = []
    for step in steps:
        outcome = []
        for _ in range(n):
            solver = GeneticAlgorithm(cross_prob=step)
            pop0 = solver.generate_random_population()
            outcome.append(solver.solve(objective_f, pop0)[1])
        means.append(mean(outcome))
    plotter(steps, means)

if __name__ == "__main__":
    steps = arange(0.81, 1, 0.01)   #przedział wartości do badania
    evaluate_best_cross_prob(steps, 5)
    
