"""
---------------luyencode.net----------------------------------
---------------Problem: TUONGDAI-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-09 22:32:47.395836+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
MOD = 1000000007
# --------------- Solve ---------------  # 
n, k = in2()
w = in2()

prefix_sum = [0] * (n + 1)
for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + w[i - 1]

for i in range(k):
    u, v = in2()
    print(prefix_sum[v] - prefix_sum[u - 1], end=' ')
##########################################
