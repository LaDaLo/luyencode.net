/*
---------------luyencode.net----------------------------------
---------------Problem: COWRUN-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-19 17:33:01.018875+07:00---------
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
int dp[10001][501] = {-1};

int main() {
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    FAST_IO;
    // --------------- Solve -------------------
    std::fill(&dp[0][0], &dp[0][0] + sizeof(dp) / sizeof(dp[0][0]), -1);
    int n, m;
    cin >> n >> m;
    vector<int> D(n);
    for (auto &x : D) { cin >> x; }
    dp[n][m] = 0;
    
    for (int i = n - 1; i >= 0; --i) {
        // case j == m
        if (dp[i + 1][m - 1] != -1) {
            dp[i][m] = max(D[i] + dp[i + 1][m - 1], dp[i + 1][m]);
        }
        else {
            dp[i][m] = dp[i + 1][m];
        }
        // case j (1 -> m - 1)
        for (int j = 1; j <= m - 1; ++j){
            int max_val = -1;
            // run
            if (dp[i + 1][j - 1] != -1) {
                max_val = max(max_val, D[i] + dp[i + 1][j - 1]);
            }
            // rest
            if (i + m - j <= n) {
                max_val = max(max_val, dp[i + m - j][m]);
            }
            dp[i][j] = max_val;
        }
        // case j == 0
        if (i + m <= n) {
            dp[i][0] = dp[i + m][m];
        }
    }

    cout << dp[0][m];
    ////////////////////////////////////////////
    return 0;
}
