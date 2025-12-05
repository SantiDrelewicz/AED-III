from typing import Hashable 

type Nodo = Hashable
type Arista = tuple[Nodo, Nodo]
type Real = int | float


class Grafo:
    def __init__(self):
        self.V: set[Nodo] = set()
        self.E: set[Arista] = set()
        self.N: dict[Nodo, list[Nodo]] = dict()

    def agregar_arista(self, a: Arista):
        v, w = a
        self.V.add(v)
        self.V.add(w)
        self.E.add((v, w))
        if v not in self.N: self.N[v] = []
        self.N[v].append(w)
        if w not in self.N: self.N[w] = []
        self.N[w].append(v)


class GrafoPesado(Grafo):
    def __init__(self):
        super().__init__()
        self.Real: dict[Arista, Real] = {}

    def agregar_arista(self, a: Arista, peso: Real):
        super().agregar_arista(a)
        self.peso[a] = peso

    def peso(self, a: Arista) -> Real:
        if a[0] == a[1]:
            return 0
        try:
            return self.peso[a]
        except KeyError:
            return self.peso[(a[1], a[0])]


class Digrafo:
    def __init__(self) -> None:
        self.V: set[Nodo] = set()
        self.E: set[Arista] = set()
        self.N_out: dict[Nodo, list[Nodo]] = dict()
        self.N_in: dict[Nodo, list[Nodo]] = dict()

    def agregar_arista(self, a: Arista) -> None:
        v, w = a
        self.V.add(v)
        self.V.add(w)
        if v not in self.N_out: self.N_out[v] = []
        self.N_out[v].append(w)
        if w not in self.N_in:  self.N_in[w] = []
        self.N_in[w].append(v)


class DigrafoPesado(Digrafo):
    def __init__(self) -> None:
        super().__init__()
        self.peso: dict[Arista, Real] = dict()

    def agregar_arista(self, a: Arista, peso: Real) -> None:
        super().agregar_arista(a)
        self.peso[a] = peso

    def peso(self, a: Arista) -> Real:
        return 0 if a[0] == a[1] else self.peso[a]