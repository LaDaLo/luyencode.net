"""
---------------luyencode.net----------------------------------
---------------Problem: NHATCHU-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-08 23:28:18.988833+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
MOD = 1000000007
# --------------- Solve ---------------  # 
s = input()
ans = {}

for c in s:
	if c not in ans:
		ans.setdefault(c, 0)
print(*ans, sep='')
##########################################
