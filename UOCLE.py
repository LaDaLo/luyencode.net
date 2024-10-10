"""
---------------luyencode.net----------------------------------
---------------Problem: UOCLE-------------------------------
---------------Author: HeHe---------------------------------
---------------Time: 2024-10-08 22:36:59.055167+07:00---------
"""
in1 = lambda: int(input())
in2 = lambda: list(map(int, input().split()))
MOD = 1000000007
# --------------- Solve ---------------  # 
t = in1()
for i in range(t):
	n = in1()
	
	if n % 2 == 0:
		while n % 2 == 0:
			n //= 2
		print(n)
	else:
		i = 3
		check = False
		while i * i <= n:
			if n % i == 0:
				check = True 
				break
			i += 2
		if check:
			print(n // i)
		else:
			print(1)

##########################################
