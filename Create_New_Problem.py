import sys
from datetime import datetime, timezone
_, file, type = sys.argv

if type == "cpp":
    source = """
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

int main() {
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    FAST_IO;
    // --------------- Solve ---------------  \\ 
    
    
    ////////////////////////////////////////////
    return 0;
}
"""
    with open(file + ".cpp", "w") as f:
        f.write("/*\n")
        f.write("-" * 15 + "luyencode.net" + "-" * 34 + '\n')
        f.write("-" * 15 + "Problem: " + file + "-" * 31 + '\n')
        f.write("-" * 15 + "Author: LaDaLo" + "-" * 33 + '\n')
        f.write("-" * 15 + "Time: " + str(datetime.now().astimezone())  + "-" * 9 + '\n')
        f.write("*/")
        for line in source:
            f.write(line)
else:
    source = """
in1 = int(input())
in2 = list(map(int, input().split()))
MOD = 1000000007
# --------------- Solve ---------------  # 
    
    
##########################################
"""
    with open(file + ".py", "w") as f:
        f.write('"""\n')
        f.write("-" * 15 + "luyencode.net" + "-" * 34 + '\n')
        f.write("-" * 15 + "Problem: " + file + "-" * 31 + '\n')
        f.write("-" * 15 + "Author: LaDaLo" + "-" * 33 + '\n')
        f.write("-" * 15 + "Time: " + str(datetime.now().astimezone())  + "-" * 9 + '\n')
        f.write('"""')
        for line in source:
            f.write(line)   

    