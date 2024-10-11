"""
---------------luyencode.net----------------------------------
---------------Problem: MAGB-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-10 20:12:59.142522+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
MOD = 1000000007
# --------------- Solve ---------------  # 
class BIT:
    def __init__(self, n):
        self.size = n
        self.BIT = [0] * (n + 1)
    
    def update(self, index, value):
        while index <= self.size:
            self.BIT[index] += value
            index += index & (-index)

    def query(self, index):
        total = 0
        while index > 0:
            total += self.BIT[index]
            index -= index & (-index)
        return total
    
    def range_query(self, left, right):
        return self.query(right) - self.query(left - 1)

n = in1()
arr = in2()

ans = 0
max_val = max(arr)
bit = BIT(max_val)
for v in arr:
    ans += bit.range_query(v + 1, max_val)
    bit.update(v, 1)

print(ans)
##########################################
