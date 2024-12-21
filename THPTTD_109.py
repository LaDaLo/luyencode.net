"""
---------------luyencode.net----------------------------------
---------------Problem: THPTTD_108-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-23 20:15:58.771550+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
in3 = lambda: map(int, input().split())
MOD = 1000000007
# --------------- Solve ---------------  # 
import sys
sys.stdin = open("FindN.inp", "r")
sys.stdout = open("FindN.out", "w")

#preprocess
length = 0
arr = []
while True:
    length += 1
    if len(arr) >= 1000:
        break

    def dfs(current, idx):
        if idx == length:
            arr.append(current)
            return
        value = [4, 7]
        for v in value:
            current = current * 10 + v
            dfs(current, idx + 1)
            current //= 10
        return

    dfs(0, 0)


for _ in range(in1()):
    N = in1()
    
    print(arr[N - 1])

    
##########################################
