"""
---------------luyencode.net----------------------------------
---------------Problem: THPTTD_118-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-11-04 23:09:33.936731+07:00---------
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
n = in1()
arr = in2()

count = 0
ans = 1
found = False

for v in arr:
    if v == 1:
        if not found:
            found = True
            count = 0
        else:
            ans *= (count + 1)
            count = 0
    else:
        count += 1

if not found:
    print(0)
else:
    print(ans)
##########################################
