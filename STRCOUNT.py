"""
---------------luyencode.net----------------------------------
---------------Problem: STRCOUNT-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-12 23:23:48.527414+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
MOD = 1000000007
# --------------- Solve ---------------  # 
def z_function(pattern, text):
    s = pattern + text
    n = len(s)
    Z = [0] * n
    L, R = 0, 0

    for i in range(1, n):
        if i > R:
            L, R = i, i
            while R < n and s[R] == s[R - L]:
                R += 1
            Z[i] = R - L
            R -= 1
        else:
            if Z[i - L] < R - i + 1:
                Z[i] = Z[i - L]
            else:
                L = i
                while R < n and s[R] == s[R - L]:
                    R += 1
                Z[i] = R - L
                R -= 1
    return Z

t = input()
Z = z_function(t, t)
n = len(t)
for i in range(1, n + 1):
    count = 0
    for idx in range(n, 2 * n):
        if Z[idx] >= i:
            count += 1
    print(count, end=' ')
##########################################
