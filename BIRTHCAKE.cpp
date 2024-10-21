/*
---------------luyencode.net----------------------------------
---------------Problem: BIRTHCAKE-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-14 00:31:21.630555+07:00---------
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
    priority_queue<int> maxHeap;
    auto minHeap = std::priority_queue<int, std::vector<int>, std::greater<int>>();

    int N, T;
    cin >> N >> T;
    vector<array<int64_t, 2>> cakes(N);
    for (int i = 0; i < N; ++i) {
        cin >> cakes[i][0] >> cakes[i][1];
    }

    vector<int> min_val_next(N);
    int min_val = INT_MAX, idx = N;
    for (int i = N - 1; i >= 0; --i) {
        min_val_next[i] = idx;
        if (cakes[i][0] + cakes[i][1] < min_val) {
            min_val = cakes[i][0] + cakes[i][1] ;
            idx = i;
        }
    }

    int64_t used = 0, cnt = 0, ans = 0;
    if (cakes[0][0] + cakes[0][1] <= T) ans = 1;
    else ans = 0;

    for (int i = 0; i < N - 1; ++i) {
        int min_idx = min_val_next[i];
        int r = T - cakes[min_idx][0] - cakes[min_idx][1];
        if (r < 0) break;

        maxHeap.push(cakes[i][1]);
        cnt += 1;
        used += cakes[i][1];

        while (!maxHeap.empty() and used > r) {
            used -= maxHeap.top();
            maxHeap.pop();
            cnt -= 1;
        }
        ans = max(ans, cnt + 1);
    }

    cout << ans;
    ////////////////////////////////////////////
    return 0;
}
