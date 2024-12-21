/*
---------------luyencode.net----------------------------------
---------------Problem: KNAPSACK1-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-23 20:53:45.144495+07:00---------
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
int64_t dp[100001] = {-1};

int main() {
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    FAST_IO;
    // --------------- Solve -------------------
    fill(dp, dp + 100001, -1);
    dp[0] = 0;
    int N, W, w, v;
    int64_t ans = 0;
    cin >> N >> W;
    for (int i = 0; i < N; ++i) {
        cin >> w >> v;
        for (int j = W; j >= w; --j) {
            if (dp[j - w] != -1) {
                dp[j] = max(dp[j], dp[j - w] + v);
                ans = max(ans, dp[j]);
            }
        } 
    }
    cout << ans;
    ////////////////////////////////////////////
    return 0;
}
