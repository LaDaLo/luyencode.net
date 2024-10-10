/*
---------------luyencode.net----------------------------------
---------------Problem: POWER2-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-06 23:11:00.374194+07:00---------
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

#define FAST_IO ios::sync_with_stdio(false);cin.tie(0);cout.tie(0);
using namespace std;

const int MOD = 1000000007;

string mul(string &a, string &b) {
    int len_a = a.length();
    int len_b = b.length();
    vector<int> ans(len_a + len_b, 0);
    int carry = 0;

    for (int i = len_a - 1; i >= 0; --i) {
        for (int j = len_b - 1; j >= 0; --j) {
            int idx = len_a - 1 - i + len_b - 1 - j;
            int val = ans[idx] + (a[i] - '0') * (b[j] - '0') + carry;
            ans[idx] = val % 10;
            carry = val / 10;
        }

        ans[len_a - 1 - i + len_b] = carry;
        carry = 0;
    }

    while (!ans.empty() && ans.back() == 0) {
        ans.pop_back();
    }

    if (ans.empty()) {
        return "0";
    }
    else {
        string ans_s;
        for (int i = ans.size() - 1; i >= 0; --i) {
            ans_s.push_back(ans[i] + '0');
        }
        return ans_s;
    }
    return "0";
}

string pow(string &a, int n) {
    string ans = "1";
    while (n) {
        if (n % 2) {
            ans = mul(ans, a);
        }
        n /= 2;
        a = mul(a, a);
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
    string a;
    int n;
    cin >> a >> n;
    cout << pow(a, n);
    ////////////////////////////////////////////
    return 0;
}
