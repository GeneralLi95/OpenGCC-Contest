# -*- coding: utf-8 -*-
class Operation:
	def __init__(self, op, x, y):
		self.op = op
		self.x = x
		self.y = y


MOD = 1000000007
maxn = 1e5 + 10
C1 = [0 for i in range(int(maxn))]
C2 = [0 for i in range(int(maxn))]

def lowbit(i):
	return (i & (-i))

def Sum(C, n):
	sum = 0
	while n > 0:
		sum = (sum + C[n]) % MOD
		n -= lowbit(n)
	return sum % MOD


def change(C, pos, num, n):
	while pos <= n:
		C[pos] = (C[pos] + num) % MOD
		pos += lowbit(pos)


class Task:
	def solve(self, data, operations):
		# ********* Begin *********#
		n = len(data)
		m = len(operations)

		for i in range(1,n+1):
			change(C1, i, data[i - 1], n)

			change(C2, i, data[i - 1] * i, n)


		ans = 0
		for i in range(m):
			op = operations[i].op
			x = operations[i].x + 1
			y = operations[i].y + 1

			if op == 'C':
				item1 = (y - 1 - data[x - 1] + MOD) % MOD
				item2 = (y - 1 - data[x - 1] + MOD) % MOD * x % MOD
				change(C1, x, item1, n)
				change(C2, x, item2, n)
				data[x - 1] = y - 1
			elif op == 'L':
				tmp1 = ((Sum(C1, y) - Sum(C1, x - 1) + MOD) % MOD) * (x - 1) % MOD
				tmp2 = (Sum(C2, y) - Sum(C2, x - 1) + MOD) % MOD
				tmp = (tmp2 - tmp1 + MOD) % MOD
				ans += tmp
				ans %= MOD
			else:
				tmp1 = ((Sum(C1, y) - Sum(C1, x - 1) + MOD) % MOD) * (y + 1) % MOD
				tmp2 = (Sum(C2, y) - Sum(C2, x - 1) + MOD) % MOD
				tmp = (tmp1 - tmp2 + MOD) % MOD
				ans += tmp
				ans %= MOD
		ans %= MOD
		return int(ans)
# ********* End *********#