"""
---------------luyencode.net----------------------------------
---------------Problem: MK119SNT-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-07 09:23:40.223519+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
MOD = 1000000007
# --------------- Solve ---------------  # 
t = in1()

is_prime = [1] * 1000001
is_prime[0] = 0
is_prime[1] = 0
for i in range(2, 1000001):
    if is_prime[i]:
        for j in range(i * i, 1000001, i):
            is_prime[j] = 0

for i in range(3, 1000001):
    is_prime[i] += is_prime[i - 1]

for i in range(t):
    l, r = in2()

    print(is_prime[r] - is_prime[l - 1])

##########################################
