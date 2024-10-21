"""
---------------luyencode.net----------------------------------
---------------Problem: PTIT003-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-21 20:24:20.031519+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
in3 = lambda: map(int, input().split())
MOD = 1000000007
# --------------- Solve ---------------  # 
n = in1()
arr = in2()

temp1, temp2 = 0, 0
for i in range(n - 1):
    temp2 += arr[i]
    temp1 += temp2
S = n * (n + 1) // 2

ans = []
no_ans = False
if (S - temp1) % n == 0:
    f1 = (S - temp1) // n
    ans.append(f1)
    for i in range(n - 1):
        f1 += arr[i]
        ans.append(f1)
else:
    no_ans = True

idx = 1
for v in sorted(ans):
    if v != idx:
        no_ans = True
    idx += 1

if no_ans:
    print("-1")
else:
    print(*ans)
##########################################
