#include <iostream>
#include <queue>
#include <vector>
#include <list>

using namespace std;

vector<int> bfs(const vector<list<int>>& vecinos, int r) {
	int n = vecinos.size();
	vector<bool> visitado(n, false); vector<int> d(n, -1);
	visitado[r] = true; d[r] = 0;
    queue<int> Q;
    Q.push(r);
    while (!Q.empty()) {
        int u = Q.front(); Q.pop();
        for (int v : vecinos[u]) {
            if (!visitado[v]) {
                visitado[v] = true; d[v] = d[u] + 1;
                Q.push(v);
            }
        }
    }
    return d;
}

int main() {
	int n, m;
	cin >> n >> m;
	int res;
	if (m <= n) res = n - m;
	else {
		int V = 2 * m;
		vector<list<int>> N_out(V);
		for (int u = 0; u < V; u++) {
			if (u < m && u > 0) {
				N_out[u].push_back(u - 1);
				N_out[u].push_back(2 * u);
			} else if (u > m) N_out[u].push_back(u - 1);
		}
		auto dist = bfs(N_out, n);
		res = dist[m];
	}
	cout << res << endl;
	return 0;
}