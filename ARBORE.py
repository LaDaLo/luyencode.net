"""
---------------luyencode.net----------------------------------
---------------Problem: ARBORE-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-20 10:18:17.063381+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
in3 = lambda: map(int, input().split())
MOD = 666013
# --------------- Solve ---------------  # 
def count_ways(N, edges):
    from collections import defaultdict

    MOD = 666013
    
    # Xây dựng cây
    tree = defaultdict(list)
    for x, y in edges:
        tree[x].append(y)
        tree[y].append(x)

    dp = [0] * (N + 1)  # dp[i] là số cách gán cho cây có gốc là i
    size = [0] * (N + 1)  # Kích thước của cây con

    def factorial(n):
        if n == 0 or n == 1:
            return 1
        res = 1
        for i in range(2, n + 1):
            res = (res * i) % MOD
        return res

    def mod_inverse(x):
        return pow(x, MOD - 2, MOD)

    def dfs(node, parent):
        size[node] = 1  # Bắt đầu từ nút này
        total_ways = 1  # Số cách cho cây con

        child_sizes = []

        for neighbor in tree[node]:
            if neighbor != parent:
                child_size = dfs(neighbor, node)
                size[node] += child_size
                child_sizes.append(child_size)
                total_ways = (total_ways * dp[neighbor]) % MOD

        if child_sizes:
            total_ways = (total_ways * factorial(size[node] - 1)) % MOD
            total_ways = (total_ways * mod_inverse(factorial(len(child_sizes)))) % MOD
        
        dp[node] = total_ways
        return size[node]

    dfs(1, -1)  # Bắt đầu từ nút 1
    return dp[1]

# Đọc dữ liệu
N = int(input())
edges = [tuple(map(int, input().split())) for _ in range(N - 1)]

# Tính số cách
result = count_ways(N, edges)
print(result)


##########################################
