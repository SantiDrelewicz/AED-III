import heapq as ColaPrioridad
from heapq import heappop as extraer_min, heappush as insertar

INF = float('inf')

def dijkstra(vecinos, costo, s):
    dist = [INF] * len(vecinos)
    dist[s] = 0
    cp: ColaPrioridad = [(0, s)]
    while len(cp) > 0: 
        dist_actual, u = extraer_min(cp)
        if not dist_actual > dist[u]:
            for v in vecinos[u]:
                if dist[v] > dist_actual + costo[(u, v)]:
                    dist[v] = dist_actual + costo[(u, v)]
                    insertar(cp, (dist[v], v))
    return dist

def main():
    vecinos = [
        [1, 2, 5],
        [2, 4],
        [3, 4],
        [],
        [3],
        [4]
    ]
    costo = {
        (0, 1): 4, (0, 2): 7, (0, 5): 3,
        (1, 2): 3, (1, 4): 1,
        (2, 3): 1, (2, 4): 1,
        (4, 3): 4,
        (5, 4): 3
    }
    print(dijkstra(vecinos, costo, 0))

if __name__ == "__main__":
    main()
