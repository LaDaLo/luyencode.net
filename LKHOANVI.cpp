/*
---------------luyencode.net----------------------------------
---------------Problem: LKHOANVI-------------------------------
---------------Author: LaDaLo---------------------------------
---------------Time: 2024-10-06 22:48:35.606530+07:00---------
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

void swap(int &a, int &b) {
    int temp = a;
    a = b;
    b = temp;
}

void permutation(vector<int> &arr, int start, int end) {
    if (start == end) {
        for (auto &v : arr) {
            cout << v << ' ';
        }
        cout << '\n';
        return;
    }

    for (int i = start; i <= end; ++i) {
        swap(arr[start], arr[i]);
        permutation(arr, start + 1, end);
        swap(arr[start], arr[i]);
    }
}

int main() {
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    FAST_IO;
    // --------------- Solve -------------------
    int n;
    cin >> n;
    vector<int> arr(n);
    iota(arr.begin(), arr.end(), 1);
    permutation(arr, 0, n - 1);
    ////////////////////////////////////////////
    return 0;
}
