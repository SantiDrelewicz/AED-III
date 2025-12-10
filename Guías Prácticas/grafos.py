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

    def agregar_nodo(self, v: Nodo):
        self.V.add(v)
        if v not in self.N: self.N[v] = []

    def eliminar_arista(self, a: Arista):
        v, w = a
        self.N[v].remove(w)
        self.N[w].remove(v)
        try:
            self.E.remove((v, w))
        except KeyError:
            self.E.remove((w, v))
        


class GrafoPesado(Grafo):
    def __init__(self):
        super().__init__()
        self.peso: dict[Arista, Real] = {}

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
    
    def eliminar_arista(self, a: Arista):
        v, w = a
        try:
            del self.peso[(v, w)]
            super().eliminar_arista((v, w))
        except KeyError:
            del self.peso[(w, v)]
            super().eliminar_arista((w, v))



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
        self.E.add((v, w))

        if v not in self.N_out: self.N_out[v] = []
        self.N_out[v].append(w)
        
        if w not in self.N_out:  self.N_out[w] = []

        if w not in self.N_in:  self.N_in[w] = []
        self.N_in[w].append(v)
        
        if v not in self.N_in: self.N_in[v] = []

    def agregar_nodo(self, v: Nodo) -> None:
        self.V.add(v)
        if v not in self.N_out: self.N_out[v] = []
        if v not in self.N_in: self.N_in[v] = []

    def eliminar_arista(self, a: Arista) -> None:
        v, w = a
        self.N_out[v].remove(w)
        self.N_in[w].remove(v)
        self.E.remove((v, w))

    def transponer(self) -> 'Digrafo':
        D_t = Digrafo()
        for v in self.V:
            D_t.agregar_nodo(v)
        for v in self.N_out:
            for w in self.N_out[v]:
                D_t.agregar_arista((w, v))
        return D_t


class DigrafoPesado(Digrafo):
    def __init__(self) -> None:
        super().__init__()
        self.peso: dict[Arista, Real] = dict()

    def agregar_arista(self, a: Arista, peso: Real) -> None:
        super().agregar_arista(a)
        self.peso[a] = peso

    def peso(self, a: Arista) -> Real:
        return 0 if a[0] == a[1] else self.peso[a]
    
    def eliminar_arista(self, a: Arista) -> None:
        del self.peso[a]
        super().eliminar_arista(a)

    def transponer(self) -> 'DigrafoPesado':
        D_t = DigrafoPesado()
        for v in self.V:
            D_t.agregar_nodo(v)
        for v in self.N_out:
            for w in self.N_out[v]:
                D_t.agregar_arista((w, v), self.peso[(v, w)])
        return D_t