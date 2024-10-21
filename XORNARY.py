"""
---------------luyencode.net----------------------------------
---------------Problem: XORNARY-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-14 23:24:04.020996+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
in3 = lambda: map(int, input().split())
MOD = 1000000007
# --------------- Solve ---------------  # 
def xor(x, y):
    if x == y:
        return '0' 
    else:
        return '1'
    
a, b = input().split()
d = abs(len(a) - len(b))
if len(a) < len(b):
    a = '0' * d + a
else:
    b = '0' * d + b

ans = ['0'] * len(a)
for i in range(len(a)):
    ans[i] = xor(a[i], b[i])

print(int(''.join(ans)))

##########################################
