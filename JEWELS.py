"""
---------------luyencode.net----------------------------------
---------------Problem: JEWELS-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-11 22:45:14.200437+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
MOD = 1000000007
# --------------- Solve ---------------  # 
def z_function(S, K):
    s = S + K + K
    n = len(s)
    Z = [0] * (n + 1)
    L, R = 0, 0

    for i in range(1, n):
        if i > R:
            L, R = i, i
            while R < n and s[R - L] == s[R]:
                R += 1
            Z[i] = R - L
            R -= 1
        else:
            if Z[i - L] < R - i + 1:
                Z[i] = Z[i - L]
            else:
                L = i
                while R < n and s[R - L] == s[R]: 
                    R += 1
                Z[i] = R - L
                R -= 1
    
    for i in range(len(S), n):
        if Z[i] >= len(S):
            return True
    return False

n, k = in2()
s = input()

for i in range(k):
    t = input()
    if z_function(s, t):
        print("YES")
    else:
        print("NO")

##########################################
