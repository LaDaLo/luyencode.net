"""
---------------luyencode.net----------------------------------
---------------Problem: PTIT002-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-21 20:20:42.726731+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
in3 = lambda: map(int, input().split())
MOD = 1000000007
# --------------- Solve ---------------  # 
arr = [in2() for _ in range(3)]

def determinant_3x3(matrix):
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    
    det = (a * (e * i - f * h) 
         - b * (d * i - f * g) 
         + c * (d * h - e * g))
    
    return det

print(determinant_3x3(arr))
##########################################
