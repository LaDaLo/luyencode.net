"""
---------------luyencode.net----------------------------------
---------------Problem: NEXTCHAR-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-11 21:51:05.182785+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
MOD = 1000000007
# --------------- Solve ---------------  # 
c = input()
print(chr(((ord(c) - ord('a') + 1) % 26) + ord('a')))
##########################################
