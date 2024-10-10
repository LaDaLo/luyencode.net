/*
---------------luyencode.net----------------------------------
---------------Problem: NPALIN2-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-07 08:47:36.030089+07:00---------
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

bool palin(int64_t n) {
    int64_t temp1 = n, temp2 = 0;
    while (n) {
        temp2 = temp2 * 10 + n % 10;
        n /= 10;
    }

    return temp1 == temp2;
}

int main() {
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    FAST_IO;
    // --------------- Solve -------------------
    int64_t l, r;
    int ans = 0;
    while (cin >> l >> r) {
        for (int64_t i = l; i <= r; ++i) {
            if (palin(i)) {
                ans += 1;
            }
        }

        cout << "HELLO" << "Hello\n";
    }
    ////////////////////////////////////////////
    return 0;
}
