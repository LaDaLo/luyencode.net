/*
---------------luyencode.net----------------------------------
---------------Problem: SUPREFIX-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-13 00:49:10.905887+07:00---------
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
    string a, b;
    cin >> a;
    cin >> b;
    string s = b + a;
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
    int idx = -1;
    int l_a = a.length();
    int l_b = b.length();
    for (int i = l_b; i < n; ++i) {
        if (Z[i] + i >= n) {
            idx = i - l_b;
            break;
        }
    }
    if (idx == -1){
        cout << a << b;
    }
    else {
        cout << a;
        for (int i = l_a - idx; i < l_b; ++i) {
            cout << b[i];
        }
    }

    ////////////////////////////////////////////
    return 0;
}
