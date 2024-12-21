/*
---------------luyencode.net----------------------------------
---------------Problem: THPTTD_113-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-28 23:29:45.127560+07:00---------
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
#include <deque>

#define FAST_IO ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
using namespace std;

const int MOD = 1000000007;

int main() {
    string __input = "minrange";
    freopen((__input + ".inp").c_str(), "r", stdin);
    freopen((__input + ".out").c_str(), "w", stdout);
    FAST_IO;
    // --------------- Solve -------------------
    int N, K; cin >> N >> K;
    vector<int> arr(N);
    for (auto &v : arr) {
        cin >> v;
    }
    deque<int> q;
    for (int i = 0; i < N; ++i) {
        if (!q.empty() && q.front() < i - K + 1) {
            q.pop_front();
        }

        while (!q.empty() && arr[q.back()] > arr[i]) {
            q.pop_back();
        }

        q.push_back(i);
        if (i >= K - 1) {
            cout << arr[q.front()] << '\n';
        }
    }
    ////////////////////////////////////////////
    return 0;
}
