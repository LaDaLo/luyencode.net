"""
---------------luyencode.net----------------------------------
---------------Problem: PAINT-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-08 23:58:06.062247+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
MOD = 1000000007
# --------------- Solve ---------------  # 
command = []
n = in1()
for i in range(n):
    command.append(input().split())

ans = []
true_color = [i for i in range(26)]
for i in reversed(range(n)):
    if command[i][0] == '2':
        true_color[ord(command[i][1]) - ord('a')] = true_color[ord(command[i][2]) - ord('a')]
    else:
        ans.append(true_color[ord(command[i][1]) - ord('a')])

for val in reversed(ans):
    print(chr(ord('a') + val), end='')

##########################################
