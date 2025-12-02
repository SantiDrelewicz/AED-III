from heapq import heappop as extraer_min, heappush as insertar
from collections import deque

INF = float('inf')

def prox_t_disp(t, tiempos_llegada):
    # buesco donde se encuentra el tiempo igual o mas cercano a t
    i = 0
    while i < len(tiempos_llegada) and tiempos_llegada[i] < t:
        i += 1
    # Busco el siguiente tiempo disponible
    while i < len(tiempos_llegada) and tiempos_llegada[i] == t:
        t += 1
        i += 1
    return t
    
def dijkstra_intergalactico(conexiones: int, T, s=0, f=-1):
    n = len(conexiones)
    t_min = [INF] * n
    t_min[s] = 0
    cp = [(0, s)]
    while len(cp) > 0:
        t, a = extraer_min(cp)
        if t > t_min[a]:
            continue
        elif a == f % n:
            return t
        t_partida = prox_t_disp(t, T[a])
        for b, w in conexiones[a]:
            tiempo_hasta_b = t_partida + w
            if t_min[b] > tiempo_hasta_b:
                t_min[b] = tiempo_hasta_b
                insertar(cp, (tiempo_hasta_b, b))
    return t_min[f]

def main():
    n, m = map(int, input().split())
    conexiones = [deque() for _ in range(n)]
    for _ in range(m):
        a, b, w = map(int, input().split())
        conexiones[a-1].append((b-1, w))
    T = []
    for i in range(n):
        tiempos = list(map(int, input().split()))
        if len(tiempos) > 1:
            ki, ti = tiempos[0], tiempos[1:]
            tiempos_llegada = [ti[j] for j in range(ki)]
            T.append(tiempos_llegada)
        else:
            T.append([])
    t_min = dijkstra_paciente(conexiones, T)
    if t_min < INF:
        print(t_min)
    else:
        print(-1)

if __name__ == "__main__":
    main()
