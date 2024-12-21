/*
---------------luyencode.net----------------------------------
---------------Problem: THPTTD_116-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-29 23:20:07.350164+07:00---------
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

#define __INPUT__ "pchar"
#define FAST_IO ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#define IO_REDIRECT freopen(__INPUT__ ".inp", "r", stdin);freopen(__INPUT__ ".out", "w", stdout);
using namespace std;

const int MOD = 1000000007;

int main() {
    FAST_IO;
    IO_REDIRECT;
    // --------------- Solve -------------------
    int n; cin >> n;
    string s; cin >> s;

    vector<int> dot(n + 1, 0);
    for (int i = 1; i <= n; ++i) {
        if (s[i - 1] == '.') {
            dot[i] = 1 + dot[i - 1];
        }
        else {
            dot[i] = dot[i - 1];
        }
    }
    int ans = INT_MAX;
    for (int i = 0; i <= n; ++i) {
        int left = i - dot[i];
        int right = dot[n] - dot[i];
        ans = min(ans, left + right);
    }
    cout << ans;
    ////////////////////////////////////////////
    return 0;
}
