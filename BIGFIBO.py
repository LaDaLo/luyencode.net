"""
---------------luyencode.net----------------------------------
---------------Problem: BIGFIBO-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-12 15:40:03.965266+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
MOD = 1000000007
# --------------- Solve ---------------  # 
def mul(A, B):
    ans = [[0, 0], [0, 0]]
    ans[0][0] = (A[0][0] * B[0][0] + A[0][1] * B[1][0]) % MOD
    ans[0][1] = (A[0][0] * B[0][1] + A[0][1] * B[1][1]) % MOD
    ans[1][0] = (A[1][0] * B[0][0] + A[1][1] * B[1][0]) % MOD
    ans[1][1] = (A[1][0] * B[0][1] + A[1][1] * B[1][1]) % MOD
    return ans

def pow(mat, n):
    ans = [[1, 0], [0, 1]]
    while n:
        if n % 2:
            ans = mul(ans, mat)
        n //= 2
        mat = mul(mat, mat)
    return ans
        

n = in1()
mat = [[1, 1], [1, 0]]
if n < 2:
    print(1)
else:
    A = pow(mat, n - 1)
    print((A[0][0] + A[0][1]) % MOD)
##########################################
