from heapq import heappop as extraer_min, heappush as insertar
from collections import deque
from bisect import bisect_left

INF = float('inf')

def prox_t_disp(t, busy):
    # busy es una lista ordenada de tiempos ocupados
    i = bisect_left(busy, t)
    while i < len(busy) and busy[i] == t:
        t += 1
        i += 1
    return t


def dijkstra_paciente(conexiones, s, f):
    n = len(conexiones)
    dist = [INF] * n
    dist[s] = 0
    cp = [(0, s)]
    while len(cp) > 0:
        t, a = extraer_min(cp)
        if t > dist[a]:
            continue
        elif a == f:
            return t
        t = prox_t_disp(t, T[a])
        for b, w in conexiones[a]:
            prox_t = t + w
            if dist[b] > prox_t:
                dist[b] = prox_t
                insertar(cp, (prox_t, b))
    return dist

def main():
    n, m = map(int, input().split())
    conexiones = [deque() for _ in range(n)]
    for _ in range(m):
        a, b, w = map(int, input().split())
        conexiones[a].append((b, w))
        conexiones[b].append((a, w))
    T = []
    for i in range(n):
        ki = list(int(t_ij) for t_ij in input().split())
        T.append(ki)
    distancias = dijkstra_paciente(conexiones, 0)


if __name__ == "__main__":
    main()
