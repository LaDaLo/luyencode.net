"""
---------------luyencode.net----------------------------------
---------------Problem: QMIN-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-14 23:03:48.916532+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
in3 = lambda: map(int, input().split())
MOD = 1000000007
# --------------- Solve ---------------  # 
class SparseTable:
    def __init__(self, data):
        self.n = len(data)
        self.log = [0] * (self.n + 1)
        for i in range(2, self.n + 1):
            self.log[i] = self.log[i // 2] + 1
            
        # Prepare the sparse table
        self.k = self.log[self.n] + 1
        self.st = [[0] * self.k for _ in range(self.n)]
        
        # Initialize the sparse table
        for i in range(self.n):
            self.st[i][0] = data[i]
        
        j = 1
        while (1 << j) <= self.n:
            i = 0
            while (i + (1 << j) - 1) < self.n:
                self.st[i][j] = min(self.st[i][j - 1], self.st[i + (1 << (j - 1))][j - 1])
                i += 1
            j += 1

    def query(self, L, R):
        j = self.log[R - L + 1]
        return min(self.st[L][j], self.st[R - (1 << j) + 1][j])
    

N, Q = in3()
arr = in2()
table = SparseTable(arr)
for i in range(Q):
    u, v = in3()
    print(table.query(u - 1, v - 1), end=' ')
##########################################
