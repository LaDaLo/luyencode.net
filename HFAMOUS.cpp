/*
---------------luyencode.net----------------------------------
---------------Problem: HFAMOUS-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-17 18:36:17.797509+07:00---------
*/
#include <iostream>
#include <iomanip>
#include <vector>
#include <queue>
#include <map>
#include <unordered_map>
#include <set>
#include <unordered_set>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <numeric>
#include <math.h>
#include <cstdint>
#include <climits>
#include <queue>

#define FAST_IO ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
using namespace std;

const int MOD = 1000000007;

int main() {
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    FAST_IO;
    // --------------- Solve -------------------
    int n, m, k, u, v; 
    cin >> n >> m >> k;
    vector<set<int>> graph(n + 1, set<int>());
    for (int i = 0; i < m; ++i) {
        cin >> u >> v;
        graph[u].insert(v);
        graph[v].insert(u);
    }

    vector<bool> eliminated(n + 1, false);
    vector<int> level(n + 1, 0);
    for (int i = 1; i <= n; ++i) {
        level[i] = graph[i].size();
    }

    queue<int> q;

    for (int i = 1; i <= n; ++i) {
        if (level[i] < k) {
            q.push(i);
            eliminated[i] = true;
        }
    }

    while (!q.empty()) {
        int current = q.front(); q.pop();

        for (auto &next : graph[current]) {
            if (!eliminated[next]) {
                level[next] -= 1;
                if (level[next] < k) {
                    q.push(next);
                    eliminated[next] = true;
                }
            }
        }
    }

    int total = 0;
    for (int i = 1; i <= n; ++i) {
        if (!eliminated[i]) {
            ++total;
        }
    }
    cout << total << "\n";
    for (int i = 1; i <= n; ++i) {
        if (!eliminated[i]) {
            cout << i << ' ';
        }
    }
    ////////////////////////////////////////////
    return 0;
}
