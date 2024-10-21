/*
---------------luyencode.net----------------------------------
---------------Problem: MEDIAN-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-12 21:25:30.573902+07:00---------
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

int main() {
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    FAST_IO;
    // --------------- Solve -------------------
    int n, m;
    cin >> n >> m;
    vector<int> arr(n);
    for (auto &v : arr) {
        cin >> v;
    }
    int idx_l = n / 2 - 1, idx_r = n / 2;

    for (int i = 0; i < m; ++i) {
        if (n % 2) {
            cout << arr[idx_r] << " ";
            idx_r += 1;
        }
        else {
            cout << arr[idx_l] << " ";
            idx_l -= 1;
        }
        n -= 1;
    }
    ////////////////////////////////////////////
    return 0;
}
