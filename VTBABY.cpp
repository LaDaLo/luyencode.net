/*
---------------luyencode.net----------------------------------
---------------Problem: VTBABY-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-19 16:48:36.806769+07:00---------
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
    while (true) {
        int n; cin >> n;
        if (n == 0) break;
        vector<array<int, 3>> rocks;
        for (int i = 0; i < n; ++i) {
            int a, b, c;
            cin >> a >> b >> c;
            rocks.push_back({a, b, c});
            rocks.push_back({a, c, b});
            rocks.push_back({b, c, a});
        }
        int size = rocks.size();
        vector<int> dp(size, -1);
        function<int(int)> find_max = [&](int idx) -> int {
            if (dp[idx] != -1) {
                return dp[idx];
            }

            int max_val = 0, w = rocks[idx][0], l = rocks[idx][1];
            for (int i = 0; i < size; ++i) {
                if (rocks[i][0] > w && rocks[i][1] > l) {
                    max_val = max(max_val, find_max(i));
                }
                if (rocks[i][1] > w && rocks[i][0] > l) {
                    max_val = max(max_val, find_max(i));
                }
            }
            dp[idx] = rocks[idx][2] + max_val;
            return dp[idx];
        };

        int ans = 0;
        for (int i = 0; i < size; ++i) {
            ans = max(ans, find_max(i));
        }

        cout << ans << "\n";
    }
    ////////////////////////////////////////////
    return 0;
}
