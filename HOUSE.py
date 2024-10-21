"""
---------------luyencode.net----------------------------------
---------------Problem: HOUSE-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-19 22:40:46.116695+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
in3 = lambda: map(int, input().split())
MOD = 1000000007
# --------------- Solve ---------------  # 
n = in1()
s = input()

ans = 0
i = 0
while i < n:
    j = i
    while j < n and s[j] == s[i]:
        j += 1
    ans += (j - i) // 2
    i = j
print(ans) 

##########################################
