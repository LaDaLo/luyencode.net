/*
---------------luyencode.net----------------------------------
---------------Problem: THPTTD_115-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-29 23:13:28.997710+07:00---------
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
    string __input = "cfile";
    freopen((__input + ".inp").c_str(), "r", stdin);
    freopen((__input + ".out").c_str(), "w", stdout);
    FAST_IO;
    // --------------- Solve -------------------
    int N; cin >> N;
    vector<int> arr(N);
    for (auto &v : arr) { cin >> v; }
    sort(arr.begin(), arr.end());
    int idx = 0;
    int64_t ans = 0;
    for (int i = 1; i < N; ++i) {
        while (idx < i && (arr[idx] < 0.9 * arr[i])) {
            ++idx;
        }
        ans += i - idx;
    }

    cout << ans;
    ////////////////////////////////////////////
    return 0;
}
