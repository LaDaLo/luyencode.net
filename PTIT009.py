"""
---------------luyencode.net----------------------------------
---------------Problem: PTIT009-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-21 21:58:41.946551+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
in3 = lambda: map(int, input().split())
MOD = 1000000007
# --------------- Solve ---------------  # 
n = in1()
S = [input() for _ in range(n)]

d = {S[0] : 0}
idx = 1
temp = S[0]
for _ in range(len(temp) - 1):
    temp = temp[1:] + temp[0]
    d[temp] = idx
    idx += 1

no_ans = False
ans = float("inf")
for pivot, pivot_idx in d.items():
    changes = 0
    for s in S:
        if s not in d:
            no_ans = True
            break

        idx = d[s]
        if pivot_idx < idx:
            changes += len(s) - idx + pivot_idx
        else:
            changes += pivot_idx - idx
    if no_ans:
        break
    ans = min(ans, changes)
if no_ans:
    print("-1")
else:
    print(ans)

##########################################
