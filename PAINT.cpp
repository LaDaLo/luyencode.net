/*
---------------luyencode.net----------------------------------
---------------Problem: PAINT-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-09 00:14:57.879881+07:00---------
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
#include <array>

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
    int n; cin >> n;
    vector<array<int, 3>> command = {{-1, 'a', 'a'}};
    string ans = "";
    int idx = 0, type;
    char a, b;
    for (int i = 0; i < n; ++i) {
        cin >> type;
        if (type == 1) {
            cin >> a;
            ans.push_back(a);
            idx += 1;
        }
        else {
            cin >> a >> b;
            command.push_back({idx - 1, a, b});
        }
    }

    vector<int> true_color(26);
    iota(true_color.begin(), true_color.end(), 0);

    for (int i = command.size() - 1; i > 0; --i) {
        true_color[command[i][1] - 'a'] = true_color[command[i][2] - 'a'];
        for (int j = command[i][0]; j > command[i - 1][0]; --j) {
            ans[j] = true_color[ans[j] - 'a'] + 'a';
        }
    }

    cout << ans;
    ////////////////////////////////////////////
    return 0;
}
