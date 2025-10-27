from queue import Queue
from collections import deque

INF = -1

def bfs(vecinos, r):
    n = len(vecinos)
    visitado, d = [False] * n, [INF] * n
    visitado[r], d[r] = True, 0
    Q = Queue()
    Q.put(r)
    while not Q.empty():
        nodo = Q.get()
        for vecino in vecinos[nodo]:
            if not visitado[vecino]:
                visitado[vecino] = True
                d[vecino] = d[nodo] + 1
                Q.put(vecino)
    return d

def main():
    n, m = map(int, input().split())
    if m <= n: 
        min_clicks = n - m
    else:
        V = 2*m
        N_out = [deque() for _ in range(V)]
        for u in range(V):
            if u < m and u > 0:
                N_out[u].extend((u - 1, 2 * u))
            elif u > m:
                N_out[u].append(u - 1)
        d = bfs(N_out, n)
        min_clicks = d[m]
    print(min_clicks)

if __name__ == "__main__":
    main()
