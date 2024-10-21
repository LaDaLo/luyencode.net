/*
---------------luyencode.net----------------------------------
---------------Problem: CHARM-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-21 17:58:27.531312+07:00---------
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
    int N, M;
    cin >> N >> M;
    vector<array<int, 2>> obj(N);
    for (int i = 0; i < N; ++i) {
        cin >> obj[i][0] >> obj[i][1];
    }

    vector<int> dp(M + 1, -1);
    dp[0] = 0;

    int ans = 0;
    for (int i = 0; i < N; ++i) {
        for (int j = M; j >= obj[i][0]; --j) {
            if (dp[j - obj[i][0]] != -1) {
                dp[j] = max(dp[j], dp[j - obj[i][0]] + obj[i][1]);
                ans = max(ans, dp[j]);
            }
        }
    }
    cout << ans;
    ////////////////////////////////////////////
    return 0;
}
