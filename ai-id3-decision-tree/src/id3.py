import pandas as pd
import numpy as np
from abc import ABC, abstractmethod


class Solver(ABC):
    """A solver. Parameters may be passed during initialization."""

    @abstractmethod
    def get_parameters(self):
        """Returns a dictionary of hyperparameters"""
        ...

    @abstractmethod
    def fit(self, X, y):
        """
        A method that fits the solver to the given data.
        X is the dataset without the class attribute.
        y contains the class attribute for each sample from X.
        It may return anything.
        """
        ...

    def predict(self, X):
        """
        A method that returns predicted class for each row of X
        """


class Node:
    def __init__(self, attribute_name=None, solution_class=None):
        self.attribute_name = attribute_name
        self.solution_class = solution_class
        self.children = {}

    def add_children(self, value):
        self.children[value] = Node()


class ID3(Solver):
    def __init__(self, X=pd.DataFrame(), y=pd.DataFrame(), max_depth=9):
        self.root = Node()
        self.X = X
        self.y = y
        self.max_depth = max_depth
        if not X.empty and not y.empty:
            self.U = pd.concat([X, y], axis=1)

    def get_parameters(self):
        return {'depth': self.max_depth}

    def inf_gain(self, d, U):
        """Oblicza przyrost informacji dla danej nazwy atrybutu i zbioru U"""
        def entropy(y):
            _, counts = np.unique(y, return_counts=True)
            return -sum(counts * np.log(counts))
        total_entropy = entropy(U.iloc[:, -1])
        divided_entropy = sum([len(U.loc[U[d]==j, d]) / len(U) * entropy(U.loc[U[d]==j, self.y.name]) for j in np.unique(U[d])])
        return total_entropy - divided_entropy

    def fit(self, X=pd.DataFrame(), y=pd.DataFrame()):
        """Buduje drzewo decyzyjne - funkcja może nie pobierać zbiorów X i y,
        wówczas bierze wartości podane przy inicjalizacji drzewa"""
        if not X.empty and not y.empty:
            self.X = X
            self.y = y
            self.U = pd.concat([X, y], axis=1)
        self._fit(self.root, self.X.columns, self.U, 0)

    def _fit(self, node:Node, D:np.ndarray, U:pd.DataFrame, depth):
        # jeżeli wszystkie atrybuty należą do tej samej klasy, zwróć tę klasę
        if len(np.unique(U.iloc[:, -1])) == 1:
            node.solution_class = np.unique(U.iloc[:, -1])[0]
            return

        # jeżeli zbiór atrybutów jest pusty, zwróć najczęstszą klasę w U
        values, counts = np.unique(U.loc[:, self.y.name], return_counts=True)
        node.solution_class = values[np.argmax(counts)]
        if len(D) == 0:
            return

        # jeżeli osiągnięto maksymalną głębokość, zakończ dalsze budowanie drzewa
        if depth >= self.max_depth:
            return

        # znajdź nazwę atrybutu dla, którego przyrost informacji jest największy
        d = D[np.argmax([self.inf_gain(d, U) for d in D])]
        node.attribute_name = d

        # dla każdej możliwej wartości atrybutu d
        for j in np.unique(U[d]):
            node.add_children(j)
            # usuń wybrany atrybut z listy
            D_without_d = np.array([attr for attr in D if attr != d])
            # zwróć poddrzewa dla których usunięto d z D oraz w zbiorze
            # U znajdują się tylko wartości, których dany atrybut d = j
            Uj = U.loc[U[d]==j, np.append(D_without_d, self.y.name)]
            self._fit(node.children[j], D_without_d, Uj, depth+1)

    def predict(self, X:pd.DataFrame):
        """Zwraca tabelę DataFrame z przewidzianą klasą dla każdego wiersza X"""
        return pd.DataFrame(X.apply(lambda x: self.predict_row(x), axis=1), columns=[self.y.name])

    def predict_row(self, x):
        """Podąża ustaloną scieżką drzewa od korzenia"""
        node = self.root
        while node.attribute_name is not None:
            try:
                node = node.children[x.loc[node.attribute_name]]
            except:
                return node.solution_class
        return node.solution_class