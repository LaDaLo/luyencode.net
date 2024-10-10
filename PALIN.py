"""
---------------luyencode.net----------------------------------
---------------Problem: PALIN-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-06 23:43:28.020814+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
MOD = 1000000007
# --------------- Solve ---------------  # 
def preprocess(s):
    """Add special characters to handle even-length palindromes."""
    return '#' + '#'.join(s) + '#'

def manacher(s):
    """Manacher's algorithm to find the longest palindromic substring."""
    T = preprocess(s)  # Transform the string
    n = len(T)
    P = [0] * n  # Array to hold the length of palindromes
    C = R = 0  # Center and right boundary

    for i in range(1, n - 1):
        mirror = 2 * C - i  # Mirror of i around center C

        if R > i:
            P[i] = min(R - i, P[mirror])  # Use the mirror value

        # Attempt to expand the palindrome centered at i
        while i + P[i] + 1 < n and i - P[i] - 1 >= 0 and T[i + P[i] + 1] == T[i - P[i] - 1]:
            P[i] += 1

        # Update the center and right boundary if needed
        if i + P[i] > R:
            C = i
            R = i + P[i]

    # Find the maximum length and its center
    max_length = 0
    center_index = 0
    for i in range(1, n - 1):
        if P[i] > max_length:
            max_length = P[i]
            center_index = i

    # Recover the longest palindromic substring
    start = (center_index - max_length) // 2  # Calculate start index in original string
    return s[start:start + max_length]

s = input()

print(manacher(s))
##########################################
