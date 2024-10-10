"""
---------------luyencode.net----------------------------------
---------------Problem: XEPSO1-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-07 20:56:20.136074+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
MOD = 1000000007
# --------------- Solve ---------------  # 
arr1 = [0, 0, 1, 7, 4, 2, 6, 8]
arr2 = [0, 0, 1, 7, 4, 2, 0, 8]
arr = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
# 2 -> 1
# 3 -> 7
# 4 -> 4
# 5 -> 2, 3, 5
# 6 -> 0, 6, 9
# 7 -> 8

def find_max(n):
    if n % 2 == 0:
        return int('1' * (n // 2))
    else:
        return int('7' + '1' * ((n - 3) // 2))

def find_min(val):
    def backtrack(n, count):
        if n == 0:
            return count
        for i in range(min(n, 7), 1, -1):
            c = backtrack(n - i, count + 1)
            if c:
                return c
        return 0
    
    number_of_digits = backtrack(val, 0)
    ans = [float('inf')]
    def backtrack2(n, cur, l, ans):
        if n == 0:
            if l == number_of_digits:
                ans[0] = min(ans[0], cur)
            else:
                return 
        if l == number_of_digits:
            return
        
        if cur == 0:
            for i in range(1, 10):
                backtrack2(n - arr[i], cur * 10 + i, l + 1, ans)
        else:
            for i in range(0, 10):
                backtrack2(n - arr[i], cur * 10 + i, l + 1, ans)
        return

    backtrack2(val, 0, 0, ans)
    return ans[0]
    

max_arr = [0] * 40
min_arr = [0] * 40
# for val in range(2, 40):
#     max_val = find_max(val)
#     min_val = find_min(val)
#     max_arr[val] = max_val
#     min_arr[val] = min_val

t = in1()
for i in range(t):
    n = in1()
    print(find_min(n), find_max(n))

    
##########################################
