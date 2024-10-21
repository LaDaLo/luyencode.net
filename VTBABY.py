"""
---------------luyencode.net----------------------------------
---------------Problem: VTBABY-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-19 14:10:43.169354+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
in3 = lambda: map(int, input().split())
MOD = 1000000007
# --------------- Solve ---------------  # 
while True:
    n = in1()
    if n == 0:
        break

    rocks = [[-1] * 3 for _ in range(n * 3)]
    idx = 0
    for i in range(n):
        x, y, z = in3()
        rocks[idx][0], rocks[idx][1], rocks[idx][2]  = x, y, z
        rocks[idx + 1][0], rocks[idx + 1][1], rocks[idx + 1][2]  = x, z, y
        rocks[idx + 2][0], rocks[idx + 2][1], rocks[idx + 2][2]  = y, z, x
        idx += 3

    ans = 0
    size = len(rocks)
    dp = [-1] * size

    def find_max(idx):
        if dp[idx] != -1:
            return dp[idx]
        
        max_val = 0
        w, l = rocks[idx][0], rocks[idx][1]
        for i in range(size):
            if rocks[i][0] > w and rocks[i][1] > l:
                max_val = max(max_val, find_max(i))
            if rocks[i][1] > w and rocks[i][0] > l:
                max_val = max(max_val, find_max(i))
        
        dp[idx] = rocks[idx][2] + max_val
        return dp[idx]

    for i in range(size):
        ans = max(ans, find_max(i))
    print(ans)

##########################################
