/*
---------------luyencode.net----------------------------------
---------------Problem: XEPSO1-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-07 21:15:47.875525+07:00---------
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
    vector<int> arr = {6, 2, 5, 5, 4, 5, 6, 3, 7, 6};
    vector<int64_t> min_arr[40], max_arr[40];
    for (int i = 2; i <= 39; ++i) {
        int64_t min_val = INT64_MAX, max_val = INT64_MIN;

        function<void(int, int64_t)> backtrack = [&](int n, int64_t cur) -> void {
            if (n == 0) {
                min_val = min(min_val, cur);
                max_val = max(max_val, cur);
            }
            else {
                if (cur == 0){
                    for (int i = 1; i < 10; ++i) {
                        if (arr[i] <= n) {
                            backtrack(n - arr[i], cur * 10 + i);
                        }
                    }
                }
                else {
                    for (int i = 0; i < 10; ++i) {
                        if (arr[i] <= n) {
                            backtrack(n - arr[i], cur * 10 + i);
                        }
                    }   
                }
            }
        };
        backtrack(i, 0);
        min_arr[i] = min_val;
        max_arr[i] = max_val;
    }

    int t; cin >> t;
    while (t--) {
        int n; cin >> n;
        cout << min_arr[n] << " " << max_arr[n] << '\n';
    }

    ////////////////////////////////////////////
    return 0;
}
