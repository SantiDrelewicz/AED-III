#include <iostream>
#include <deque>
#include <queue>
#include <vector>

using namespace std;

using ll = long long;

const ll INF = 1e18;

struct Portal {
    ll p_destino;
    ll t_transferencia;
};

struct TiempoPlaneta {
    ll tiempo;
    ll planeta;
    bool operator>(const TiempoPlaneta& other) const {
        return tiempo > other.tiempo;
    }
};

ll prox_tiempo_disp(ll t, vector<ll>& tiempos_llegada) {
    // busco dónde se encuentra el tiempo igual o más cercano a t
    ll i = 0;
    while (i < tiempos_llegada.size() && tiempos_llegada[i] < t) {
        i++;
    }
    // busco el siguiente tiempo disponible
    while (i < tiempos_llegada.size() && tiempos_llegada[i] == t) {
        i++; t++;
    }
    return t;
}

ll dijkstra_intergalactico(vector<deque<Portal>>& portales, vector<vector<ll>>& tiempos_llegada) {
    ll n = portales.size();
    ll s = 0; ll f = n - 1;
    
    vector<ll> t_min(n, INF);
    t_min[s] = 0;

    priority_queue<TiempoPlaneta, vector<TiempoPlaneta>, greater<TiempoPlaneta>> pq;
    pq.push({s, 0});

    while (!pq.empty()) {
        TiempoPlaneta actual = pq.top(); pq.pop();
        ll a = actual.planeta; ll t = actual.tiempo;

        if (t > t_min[a]) continue;
        if (a == f) return t;

        auto t_partida = prox_tiempo_disp(t, tiempos_llegada[a]);

        for (auto portal : portales[a]) {
            auto b = portal.p_destino;
            auto w = portal.t_transferencia;

            ll t_llegada = t_partida + w;

            if (t_llegada < t_min[b]) {
                t_min[b] = t_llegada;
                pq.push(TiempoPlaneta{t_llegada, b});
            }
        }
    }
    return t_min[f];
}


int main() {
    ll n, m;
    cin >> n >> m;
    vector<deque<Portal>> portales(n);
    for (ll i = 0; i < m; i++) {
        ll a, b, w;
        cin >> a >> b >> w;
        portales[a-1].push_back(Portal{b-1, w});
        portales[b-1].push_back(Portal{a-1, w});
    }
    vector<vector<ll>> tiempos_llegada(n);
    for (ll i = 0; i < n; i++) {
        ll k;
        cin >> k;
        tiempos_llegada[i].resize(k);
        for (ll j = 0; j < k; j++) {
            cin >> tiempos_llegada[i][j];
        }
    }
    auto res = dijkstra_intergalactico(portales, tiempos_llegada);
    if (res < INF) {
        cout << res << "\n";
    } else {
        cout << -1 << "\n";
    }

    return 0;
}

