package step2;

import java.util.List;

public class Task {

	long MOD = 1000000007;
	int maxn = (int) (1e5 + 10);
	long[] C1 = new long[maxn];
	long[] C2 = new long[maxn];

	int lowbit(int x) {
		return x & (-x);
	}

	long Sum(long[] C, int n) {
		long sum = 0;
		while (n > 0) {
			sum = (sum + C[n]) % MOD;
			n -= lowbit(n);
		}
		return sum % MOD;
	}

	void change(long[] C, int pos, long num, int n) {
		while (pos <= n) {
			C[pos] = (C[pos] + num) % MOD;
			pos += lowbit(pos);
		}
	}

	public int solve(List<Integer> data, List<Operation> operations) {
		/********* begin *********/
		int n = (int) data.size();
		int m = (int) operations.size();

		for (int i = 1; i <= n; i++) {
			change(C1, i, data.get(i - 1), n);
			change(C2, i, data.get(i - 1) * i, n);
		}

		long ans = 0;
		for (int i = 0; i < m; i++) {
			String op = operations.get(i).op;
			int x = operations.get(i).x + 1;
			int y = operations.get(i).y + 1;
			if (op.equals("C")) {
				long item1 = (y - 1 - data.get(x - 1) + MOD) % MOD;
				long item2 = (y - 1 - data.get(x - 1) + MOD) % MOD * x % MOD;
				change(C1, x, item1, n);
				change(C2, x, item2, n);
				data.set(x - 1, y - 1);
			} else if (op.equals("L")) {
				long tmp1 = ((Sum(C1, y) - Sum(C1, x - 1) + MOD) % MOD) * (x - 1) % MOD;
				long tmp2 = (Sum(C2, y) - Sum(C2, x - 1) + MOD) % MOD;
				long tmp = (tmp2 - tmp1 + MOD) % MOD;
				ans += tmp;
				ans %= MOD;
			} else if (op.equals("R")) {
				long tmp1 = ((Sum(C1, y) - Sum(C1, x - 1) + MOD) % MOD) * (y + 1) % MOD;
				long tmp2 = (Sum(C2, y) - Sum(C2, x - 1) + MOD) % MOD;
				long tmp = (tmp1 - tmp2 + MOD) % MOD;
				ans += tmp;
				ans %= MOD;
			}
		}
		ans %= MOD;
		return (int) ans;

		/********* end *********/
	}
}

class Operation {
	String op;
	int x;
	int y;
}