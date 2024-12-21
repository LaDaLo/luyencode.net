"""
---------------luyencode.net----------------------------------
---------------Problem: THPTTD_119-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-11-04 23:23:32.727695+07:00---------
"""
import sys
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
in3 = lambda: map(int, input().split())
MOD = 1000000007
__input = 'local'
input_path = f"{__input}.inp"
output_path = f"{__input}.out"
sys.stdin = open(input_path,"r")
sys.stdout = open(output_path,"w")
# --------------- Solve ---------------  # 
import math

def lcm(x, y):
    return (x * y) // math.gcd(x, y)

def lcm_three(a, b, c):
    return lcm(lcm(a, b), c)

def find_max_lcm_triplet(N):
    if N < 3:
        return None  # Không có bộ ba nào khi N < 3

    max_lcm = 0
    best_triplet = (1, 1, 1)

    # Kiểm tra các số gần N nhất
    candidates = [N, N-1, N-2]

    if N % 2 == 0:  # Nếu N chẵn, kiểm tra cả N-3
        candidates.append(N-3)
    else:  # Nếu N lẻ, kiểm tra cả N-2
        candidates.append(N-2)

    for A in candidates:
        for B in candidates:
            for C in candidates:
                if A != B and B != C and A != C:
                    current_lcm = lcm_three(A, B, C)
                    if current_lcm > max_lcm:
                        max_lcm = current_lcm
                        best_triplet = (A, B, C)

    return best_triplet, max_lcm

N = in1()
if N == 2:
    print(2)
elif N == 1:
    print(1)
else:
    triplet, max_lcm_value = find_max_lcm_triplet(N)
    print(max_lcm_value)
##########################################
