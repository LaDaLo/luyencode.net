/*
---------------luyencode.net----------------------------------
---------------Problem: PALIN-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-07 00:08:20.262554+07:00---------
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
    string s;
    cin >> s;
    int ans = 0;
    int l = s.length();

    vector<vector<int>> dp(l, vector<int>(l, 0));

    for (int i = 0; i < l; ++i) {
        dp[i][i] = 1;
    }

    for (int i = 0; i < l - 1; ++i) {
        if (s[i] == s[i + 1]) dp[i][i + 1] = 2;
        else dp[i][i + 1] = 1;
    }

    for (int i = 2; i < l; ++i) {
        for (int j = 0; j < l - i; ++j) {
            if (s[j] == s[i + j]) {
                dp[j][i + j] = 2 + dp[j + 1][i + j - 1];
            }
            else {
                dp[j][i + j] = max(dp[j + 1][i + j - 1], max(dp[j + 1][i + j], dp[j][i + j - 1]));
            }
        }
    }

    cout << dp[0][l - 1];
    ////////////////////////////////////////////
    return 0;
}
