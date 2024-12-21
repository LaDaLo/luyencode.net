/*
---------------luyencode.net----------------------------------
---------------Problem: EXTPALIN-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-13 00:38:25.196409+07:00---------
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
    // freopen("input.txt", "r", stdin);
    // freopen("output.txt", "w", stdout);
#endif
    FAST_IO;
    // --------------- Solve -------------------
    string t; cin >> t;
    string rev = t;
    reverse(rev.begin(), rev.end());
    string s = rev + t;

    int n = s.length();

    vector<int> Z(n, 0);
    int L = 0, R = 0;

    for (int i = 1; i < n; ++i) {
        if (i > R) {
            L = i; R = i;
            while (R < n and s[R] == s[R - L]) {
                R += 1;
            }
            Z[i] = R - L;
            R -= 1;
        }

        else {
            if (Z[i - L] < R - i + 1) {
                Z[i] = Z[i - L];
            }
            else {
                L = i;
                while (R < n and s[R] == s[R - L]) {
                    R += 1;
                }
                Z[i] = R - L;
                R -= 1;
            }
        }
    }

    int idx = 0;
    int l = t.length();
    for (int i = l; i < 2 * l; ++i) {
        if (Z[i] + i >= 2 * l) {
            idx = i - l;
            break;
        }
    }
    cout << t;
    for (int i = idx - 1; i > -1; --i) {
        cout << t[i];
    }
    // ////////////////////////////////////////////
    // return 0;
}