"""
---------------luyencode.net----------------------------------
---------------Problem: QSUM-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-11 22:46:04.368808+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
MOD = 1000000007
# --------------- Solve ---------------  # 
class BIT:
    def __init__(self, n):
        self.bit = [0] * (n + 1)
        self.size = n
    
    def update(self, index, value):
        while index <= self.size:
            self.bit[index] += value
            index += index & -index
    
    def query(self, index):
        ans = 0
        while index > 0:
            ans += self.bit[index]
            index -= index & -index
        return ans
    
    def range_query(self, left, right):
        return self.query(right) - self.query(left - 1)
    
n, Q = in2()
arr = in2()
bit = BIT(n)
for i in range(n):
    bit.update(i + 1, arr[i])

for i in range(Q):
    type, a, b = in2()
    if type == 1:
        bit.update(a, b)
    else:
        print(bit.range_query(a, b), end=' ')
##########################################
