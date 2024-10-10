"""
---------------luyencode.net----------------------------------
---------------Problem: ODDCOIN-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-09 00:57:47.992874+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
MOD = 1000000007
# --------------- Solve ---------------  # 
import bisect
for i in range(in1()):
    coins1 = [1, 3, 5, 10, 30, 50, 100, 300, 500, 1000, 3000, 5000, 10000, 30000, 50000, -1]
    coins2 = [1, 3, 5, 10, 30, 50, 100, 300, 500, 1000, 3000, 5000, 10000, 30000, 50000, -1]
    x, val = in2()
    i = bisect.bisect_left(coins2, x)
    coins2[i] = x

    idx = 15
    ans1 = 0
    t = val
    while t:
        if coins1[idx] != -1 and coins1[idx] <= t:
            used = t // coins1[idx]
            t = t % coins1[idx]
            ans1 += used
        idx -= 1

    idx = 15
    ans2 = 0
    t = val
    while t:
        if coins2[idx] != -1 and coins2[idx] <= t:
            used = t // coins2[idx]
            t = t % coins2[idx]
            ans2 += used
        idx -= 1
    
    print(min(ans1, ans2))

##########################################
