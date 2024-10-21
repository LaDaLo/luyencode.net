"""
---------------luyencode.net----------------------------------
---------------Problem: PTIT008-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-21 21:25:41.593730+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
in3 = lambda: map(int, input().split())
MOD = 1000000007
# --------------- Solve ---------------  # 
n, m = in3()
arr = [in2() for _ in range(m)]
current_pos, current_h = arr[0][0], arr[0][1]
ans = arr[0][1]
no_ans = False
for next_pos, next_h in arr[1:]:

    length = next_pos - current_pos - abs(next_h - current_h)
    if length < 0:
        no_ans = True
    else:
        ans = max(ans, max(current_h, next_h) + length // 2, max(current_h, next_h))

    current_pos, current_h = next_pos, next_h

if no_ans:
    print("-1")
else:
    print(ans)
##########################################
