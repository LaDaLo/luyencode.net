"""
---------------luyencode.net----------------------------------
---------------Problem: FIB2-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-21 16:16:02.374416+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
in3 = lambda: map(int, input().split())
MOD = 1000000007
# --------------- Solve ---------------  # 
# f0 'a'      
# f1 'b'
# f2 'ab'                  -----> f2 = f0 + f1
# f3 'bab'                 -----> f3 = f1 + f2 = f1 + f0 + f1
# f4 'abbab'               -----> f4 = f2 + f3 = f0 + f1 + f1 + f0 + f1
# f5 'bababbab'            -----> f5 = f3 + f4 = f3 + f2 + f3 
# f6 'abbabbababbab'
# f7 'bababbababbabbababbab'
# preprocess
A = [0] * 46
L = [0] * 46
A[0] = L[0] = L[1] = 1
for i in range(2, 46):
    A[i] = A[i - 1] + A[i - 2]
    L[i] = L[i - 1] + L[i - 2]

def count(n, k):
    if k == 0:
        return 0
    if n == 0:
        return 1
    if n == 1:
        return 0
    if k <= L[n - 1]:
        return count(n - 1, k)
    else:
        return A[n - 1] + count(n - 2, k - L[n - 1])
    
for i in range(in1()):
    n, k = in3()

    print(A[n] - count(n, L[n] - k))

##########################################
