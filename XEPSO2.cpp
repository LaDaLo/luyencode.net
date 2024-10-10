/*
---------------luyencode.net----------------------------------
---------------Problem: XEPSO2-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-07 22:49:10.142906+07:00---------
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

int used[10] = {6, 2, 5, 5, 4, 5, 6, 3, 7, 6};
int count(int64_t val) {
    int ans = 0;
    while (val) {
        ans += used[val % 10];
        val /= 10;
    }
    return ans;
}

int main() {
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    FAST_IO;
    // --------------- Solve -------------------
    int t;
    cin >> t;
    while (t--) {
        int64_t l, r;
        cin >> l >> r;
        int min_val = INT_MAX, max_val = INT_MIN;

        for (int64_t i = l; i <= r; ++i) {
            int number_of_stick = count(i);
            min_val = min(min_val, number_of_stick);
            max_val = max(max_val, number_of_stick);
        }

        cout << min_val << " " << max_val << "\n";
    }
    ////////////////////////////////////////////
    return 0;
}
