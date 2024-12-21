"""
---------------luyencode.net----------------------------------
---------------Problem: THPTTD_120-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-11-13 19:57:53.190744+07:00---------
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
from collections import defaultdict
d = defaultdict(list)
for _ in range(in1()):
    a, b = in3()
    d[abs(a - b)].append((a, b))

all_keys = list(d.keys())
key = sorted(all_keys, key=lambda x : (len(d[x]), -x), reverse=True)[0]
print(key)
for x, y in d[key]:
    print(x, y)
##########################################
