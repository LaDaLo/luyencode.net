"""
---------------luyencode.net----------------------------------
---------------Problem: MAXFREQ-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-08 08:19:06.739916+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
MOD = 1000000007
# --------------- Solve ---------------  # 
n = in1()
arr = in2()

from collections import Counter
d = Counter(arr)

ans = arr[0]
freq = 0

for key, val in d.items():
    if val > freq:
        freq = val
        ans = key

print(ans, freq)
##########################################
