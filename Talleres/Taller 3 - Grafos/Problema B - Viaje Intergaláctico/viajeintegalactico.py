import heapq as ColaPrioridad
from heapq import heappop as extraer_min, heappush as insertar

INF = float('inf')

def dijkstra(vecinos, s):
    dist = [INF] * len(vecinos)
    dist[s] = 0
    cp: ColaPrioridad = [(0, s)]
    while len(cp) > 0: 
        dist_actual, u = extraer_min(cp)
        if not dist_actual > dist[u]:
            for v, p in vecinos[u]:
                if dist[v] > dist_actual + p:
                    dist[v] = dist_actual + p
                    insertar(cp, (dist[v], v))
    return dist

def main():
    vecinos = [
        [(1, 4), (5, 3)],
        [(2, 3), (4, 1)],
        [(3, 1), (4, 1)],
        [],
        [(3, 4)],
        [(4, 3)]
    ]
    print(dijkstra(vecinos, 0))

if __name__ == "__main__":
    main()
