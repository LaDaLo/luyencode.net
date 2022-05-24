/*
---------------luyencode.net----------------------------------
---------------Problem: CB04-------------------------------
---------------Author: LaDaLo---------------------------------
---------------Time: 2022-05-24 18:23:14.654635+07:00---------
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

const int mod = 1000000007;

int main()
{
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    FAST_IO;
    // --------------- Solve ---------------  \\ 
    
    int a, b;
    cin >> a >> b;
    cout << a + b << '\n';
    cout << a - b << '\n';
    cout << a * b << '\n';
    if (b == 0)
        cout << "INF\n";
    else
        cout << fixed << setprecision(2) << static_cast<float>(a) / b << '\n';
}


