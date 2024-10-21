"""
---------------luyencode.net----------------------------------
---------------Problem: CHARM-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-21 17:52:36.485923+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
in3 = lambda: map(int, input().split())
MOD = 1000000007
# --------------- Solve ---------------  # 
N, M = in3()
obj = [[0, 0] for _ in range(N)]

for i in range(N):
    obj[i][0], obj[i][1] = in3()
    
dp = [-1] * (M + 1)
dp[0] = 0

ans = 0
for i in range(N):
    for j in range(M, obj[i][0] - 1, -1):
        if dp[j - obj[i][0]] != -1:
            dp[j] = max(dp[j], dp[j - obj[i][0]] + obj[i][1])
            ans = max(ans, dp[j])
print(ans)
##########################################
