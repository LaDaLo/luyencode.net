/*
---------------luyencode.net----------------------------------
---------------Problem: QMIN-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-14 23:12:31.343411+07:00---------
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

#define FAST_IO ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
using namespace std;

const int MOD = 1000000007;

class SparseTable {
public:
    SparseTable(const std::vector<int>& data) {
        n = data.size();
        log.resize(n + 1);
        for (int i = 2; i <= n; ++i) {
            log[i] = log[i / 2] + 1;
        }
        
        k = log[n] + 1;
        st.resize(n, std::vector<int>(k));

        // Initialize the sparse table
        for (int i = 0; i < n; ++i) {
            st[i][0] = data[i];
        }

        for (int j = 1; (1 << j) <= n; ++j) {
            for (int i = 0; i + (1 << j) - 1 < n; ++i) {
                st[i][j] = std::min(st[i][j - 1], st[i + (1 << (j - 1))][j - 1]);
            }
        }
    }

    // Query the minimum in range [L, R]
    int query(int L, int R) {
        int j = log[R - L + 1];
        return std::min(st[L][j], st[R - (1 << j) + 1][j]);
    }

private:
    int n; // Size of the input array
    int k; // Maximum power of 2
    std::vector<int> log; // Precomputed log values
    std::vector<std::vector<int>> st; // Sparse table
};

int main() {
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    FAST_IO;
    // --------------- Solve -------------------
    int N, Q; cin >> N >> Q;
    vector<int> arr(N);
    for (auto &v : arr) cin >> v;
    SparseTable table(arr);

    while (Q--) {
        int u, v; cin >> u >> v;
        cout << table.query(u - 1, v - 1) << " ";
    }
    ////////////////////////////////////////////
    return 0;
}
