/*
---------------luyencode.net----------------------------------
---------------Problem: STRCOUNT-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-12 23:38:25.196409+07:00---------
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

class BIT {
public:
    std::vector<int> tree; 
    int size;


    BIT(int n) {
        size = n + 1;
        tree.resize(size, 0);
    }

    void update(int index, int value) {
        while (index < size) {
            tree[index] += value; 
            index += index & -index;
        }
    }

    int query(int index) {
        int sum = 0;
        while (index > 0) {
            sum += tree[index];
            index -= index & -index; 
        }
        return sum;
    }
};

int main() {
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    FAST_IO;
    // --------------- Solve -------------------
    string s; cin >> s;
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

    BIT bit(n);
    for (int i = 1; i < n; ++i) {
        if (Z[i] > 0)
            bit.update(Z[i], 1);
    }
    int max = bit.query(n);
    for (int i = 1; i < n; ++i) {
        cout << max - bit.query(i - 1) + 1 << ' ';
    }
    cout << 1;
    // ////////////////////////////////////////////
    // return 0;
}
