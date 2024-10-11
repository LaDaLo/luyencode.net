/*
---------------luyencode.net----------------------------------
---------------Problem: KHOPXAU-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-12 00:31:35.320530+07:00---------
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

void z_function(string pattern, string text) {
    string s = pattern + text;
    int n = s.length();
    vector<int> Z(n, 0);
    int L = 0, R = 0;
    for (int i = 1; i < n; ++i) {
        if (i > R) {
            L = i;
            R = i;
            while (R < n && s[R] == s[R - L]) {
                ++R;
            }
            Z[i] = R - L;
            --R;
        }
        else {
            if (Z[i - L] < R - L + 1) {
                Z[i] = Z[i - L];
            }
            else {
                L = i;
                while (R < n && s[R] == s[R - L]) {
                    ++R;
                }
                Z[i] = R - L;
                --R;
            }
        }
    }

    int p_length = pattern.length();
    for (int i = p_length; i < n; ++i) {
        if (Z[i] >= p_length) {
            cout << i + 1 - p_length << ' ';
        }
    }
    return;
}

int main() {
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    FAST_IO;
    // --------------- Solve -------------------
    string s, t;
    cin >> s;
    cin >> t;
    z_function(t, s);
    ////////////////////////////////////////////
    return 0;
}
