"""
---------------luyencode.net----------------------------------
---------------Problem: THPTTD_113-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-28 23:05:21.935615+07:00---------
"""
import sys
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
in3 = lambda: map(int, input().split())
MOD = 1000000007
input_name = 'minrange'
input_path = f"{input_name}.inp"
output_path = f"{input_name}.out"
from os import path
if path.exists(input_path):
    sys.stdin = open(input_path,"r")
    sys.stdout = open(output_path,"w")
# --------------- Solve ---------------  # 
N, K = in3()
arr = in2()

from collections import deque
queue = deque()

for i in range(N):
    if queue and queue[0] < i - K + 1:
        queue.popleft()
    
    while queue and arr[queue[-1]] > arr[i]:
        queue.pop()
    
    queue.append(i)
    if i >= K - 1:
        print(arr[queue[0]])
    
##########################################
