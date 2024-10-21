/*
---------------luyencode.net----------------------------------
---------------Problem: KNAP-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-19 22:52:53.959096+07:00---------
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

int dp[5001];
int items[50001][2];

int main() {
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    FAST_IO;
    // --------------- Solve -------------------
    int n, M;
    cin >> n >> M;

    for (int i = 0; i < n; ++i) {
        cin >> items[i][0] >> items[i][1];
    }
    int ans = 0;
    for (int i = 0; i < n; ++i) {
        for (int j = M; j >= items[i][0]; --j) {
            dp[j] = max(dp[j], items[i][1] + dp[j - items[i][0]]);
            ans = max(ans, dp[j]);
        }
    }
    cout << ans;
    ////////////////////////////////////////////
    return 0;
}
