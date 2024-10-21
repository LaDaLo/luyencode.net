"""
---------------luyencode.net----------------------------------
---------------Problem: PTIT006-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-21 21:01:03.333360+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
in3 = lambda: map(int, input().split())
MOD = 1000000007
# --------------- Solve ---------------  # 
def generate_spiral_matrix(n):
    # Khởi tạo ma trận rỗng
    matrix = [[0] * n for _ in range(n)]
    
    top, bottom, left, right = 0, n - 1, 0, n - 1
    num = 1

    while top <= bottom and left <= right:
        # Từ trái sang phải
        for i in range(left, right + 1):
            matrix[top][i] = num
            num += 1
        top += 1
        
        # Từ trên xuống dưới
        for i in range(top, bottom + 1):
            matrix[i][right] = num
            num += 1
        right -= 1
        
        if top <= bottom:
            # Từ phải sang trái
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1
            
        if left <= right:
            # Từ dưới lên trên
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1

    return matrix

# Ví dụ sử dụng
n = in1()
spiral_matrix = generate_spiral_matrix(n)
for row in spiral_matrix:
    print(*row)

##########################################
