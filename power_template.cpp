/*
---------------luyencode.net----------------------------------
---------------Problem: power_template-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-20 16:17:39.760765+07:00---------
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
    cout << pow(123, 5, 1000007);
    ////////////////////////////////////////////
    return 0;
}
