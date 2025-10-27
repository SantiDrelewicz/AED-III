#include <iostream>
#include <unordered_set>
#include <vector>

using namespace std;
 
int n, k;
vector<int> cartas, fav, alegria;
 
vector<vector<int>> memo;
 
/*
MaxAlegria(j, c): maxima alegria que puedo conseguir con j jugadores cuya carta favorita es la misma
habiendo c cartas de ella en el mazo para repartir.
*/
int maxAlegria(int j, int c) {
    if (j == 0) return 0;
    else if (memo[j][c] != -1) return memo[j][c];
    else {
        int res = 0;
        for (int t = 0; t <= min(k, c); t++) {
            res = max(res, alegria[t] + maxAlegria(j - 1, c - t));
        }
        memo[j][c] = res;
        return memo[j][c];
    }
}
 
 
int contar(const vector<int> &s, int n){
    int res = 0;
    for (int i = 0; i < s.size(); i++){
        if (s[i] == n) res ++;
    }
    return res;
}
 
 
int main() {
    cin >> n >> k;
    cartas = vector<int>(n * k);
    for (int i = 0; i < n*k; i++) cin >> cartas[i];
    fav = vector<int>(n);
    for (int i = 0; i < n; i++) cin >> fav[i];
    alegria = vector<int>(k + 1);
    alegria[0] = 0;
    for (int t = 1; t <= k; t++) cin >> alegria[t];   
 
    // Obtengo las cartas favoritas únicas
    unordered_set<int> fav_unicos(fav.begin(), fav.end());
    vector<int> cartas_fav = vector<int>(fav_unicos.begin(), fav_unicos.end());
    
    vector<int> cant_cartas = vector<int>(cartas_fav.size());
    vector<int> cant_jugadores = vector<int>(cartas_fav.size());
 
    // Cuento la cantidad de cartas y jugadores por carta favorita
    for (int f = 0; f < cartas_fav.size(); f++) {
        cant_cartas[f] = contar(cartas, cartas_fav[f]);
        cant_jugadores[f] = contar(fav, cartas_fav[f]);
    }
 
    int max_alegria_total = 0;
 
    // Resuelvo c/grupo de favorito
    for (int f = 0; f < cartas_fav.size(); f++) {
        memo = vector<vector<int>>(
            cant_jugadores[f] + 1, vector<int>(cant_cartas[f] + 1, -1)
        );
        max_alegria_total += maxAlegria(cant_jugadores[f], cant_cartas[f]);
    }
 
    cout << max_alegria_total << endl;
    return 0;
}