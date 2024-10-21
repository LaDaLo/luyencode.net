"""
---------------luyencode.net----------------------------------
---------------Problem: PALINZ-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-21 17:45:51.683225+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
in3 = lambda: map(int, input().split())
MOD = 1000000007
# --------------- Solve ---------------  # 
s = input()
def check(s, L, R):
    m = (R - L) // 2 + L
    if (R - L) % 2 == 0:
        l = r = m
    else:
        l, r = m, m + 1
    
    while l >= L and r <= R:
        if s[l] != s[r]:
            return False
        l -= 1
        r += 1
    return True

for i in range(in1()):
    L, R = in3()
    if check(s, L - 1, R - 1):
        print("YES")
    else:
        print("NO")
##########################################
