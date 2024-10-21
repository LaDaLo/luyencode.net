/*
---------------luyencode.net----------------------------------
---------------Problem: BITSTR-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-20 15:10:13.156561+07:00---------
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

const int MOD = 1000007;
int dp[2][100001];

int64_t pow(int64_t a, int64_t n, int64_t mod=0) {
    int64_t result = 1;
    a = mod ? a % mod : a;

    while (n) {
        if (n % 2 == 1) {
            result = (mod ? (result * a) % mod : result * a);
        }
        n = n >> 1;
        a = (mod ? (a * a) % mod : a * a);
    }
    return result;
}

int main() {
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    FAST_IO;
    // --------------- Solve -------------------
    int N, K;
    cin >> N >> K;

    int ans = 0, current = 1, temp1 = 1;
    for (int i = 1; i <= N; ++i) {
        for (int j = 0; j < i; ++j) {
            dp[0][i] = (dp[0][i] + dp[1][j]) % MOD;
        }
        
        for (int j = 1; j < K; ++j) {
            if (i - j >= 0) dp[1][i] = (dp[1][i] + dp[0][i - j]) % MOD;
        }
    }

    cout << (pow(2, N, MOD) - dp[0][N] - dp[1][N]) % MOD;
    ////////////////////////////////////////////
    return 0;
}
