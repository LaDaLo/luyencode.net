"""
---------------luyencode.net----------------------------------
---------------Problem: WOODCUT-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-13 10:29:27.297890+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
in3 = lambda: map(int, input().split())
MOD = 1000000007
# --------------- Solve ---------------  # 

# Đọc độ dài N
N, K = in3()
l = []
def generate_binary(N):
    total_strings = 2 ** N
    for i in range(total_strings):
        # Chuyển số nguyên i thành xâu nhị phân có độ dài n
        binary_string = bin(i)[2:].zfill(N)
        yield binary_string

ans = 0
for s in generate_binary(N):
    if "1" * K in s:
        ans += 1
print(ans)


def sol2(N, K):
    return ((2 - N) * pow(N, K)) // (pow(2, K + 1) * pow(1 - N, 2) - pow(N, K + 1) * (1 - N))

print(sol2(N, K))
##########################################
