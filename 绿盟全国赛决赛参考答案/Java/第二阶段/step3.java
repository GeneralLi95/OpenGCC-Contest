package step3;

import java.util.Arrays;
import java.util.List;

public class Task {

	int kMaxN = 55;
	int kMaxM = 10;
	int kMaxS = 1024;

	public int solve(int n, List<DeliveryCost> cost_e, int[] employees, int[] cost_b) {

		/********* Begin *********/
		int[][] floyd = new int[kMaxN][kMaxN];
		for (int nf = 0; nf < kMaxN; nf++) {
			Arrays.fill(floyd[nf], 9999);
		}
		for (int i = 1; i <= n; ++i) {
			floyd[i][i] = 0;
		}
		int m = cost_e.size();
		for (int i = 0; i < m; ++i) {
			int a = cost_e.get(i).u;
			int b = cost_e.get(i).v;
			floyd[a][b] = cost_e.get(i).cost;
			floyd[b][a] = cost_e.get(i).cost;
		}

		for (int k = 1; k <= n; ++k) {
			for (int i = 1; i <= n; ++i) {
				for (int j = 1; j <= n; ++j) {
					floyd[i][j] = Math.min(floyd[i][j], floyd[i][k] + floyd[k][j]);
				}
			}
		}

		int[][] f = new int[kMaxS][kMaxN];
		for (int nfm = 0; nfm < kMaxS; nfm++) {
			Arrays.fill(f[nfm], 9999);
		}
		for (int i = 1; i <= n; ++i) {
			f[0][i] = 0;
		}
		int num_employees = employees.length;
		for (int i = 0; i < num_employees; ++i) {
			f[1 << i][employees[i]] = 0;
		}

		int num_states = 1 << num_employees;
		for (int i = 0; i < num_states; ++i) {
			for (int j = 1; j <= n; ++j) {
				for (int s = i & (i - 1); s > 0; s = (s - 1) & i) {
					f[i][j] = Math.min(f[i][j], f[s][j] + f[i - s][j]);
				}
			}
			for (int j = 1; j <= n; ++j) {
				for (int k = 1; k <= n; ++k) {
					f[i][j] = Math.min(f[i][j], f[i][k] + floyd[k][j]);
				}
			}
		}
		int[] g = new int[kMaxS];
		Arrays.fill(g, 9999);
		for (int i = 0; i < num_states; ++i) {
			for (int j = 0; j < num_employees; ++j) {
				if (((i >> j) & 1) > 0) {
					g[i] = Math.min(g[i], f[i][employees[j]] + cost_b[j]);
				}
			}
		}

		int[] h = new int[kMaxS];
		for (int i = 0; i < num_states; ++i) {
			h[i] = g[i];
			for (int s = i & (i - 1); s > 0; s = (s - 1) & i) {
				h[i] = Math.min(h[i], h[s] + g[i - s]);
			}
		}

		return h[num_states - 1];
		/********* End *********/
	}
	
	public static void main(String[] args) {
			int n = 3;
			String binaryString = Integer.toBinaryString(n) ;
			System.out.println(binaryString);
			System.out.println(Integer.toBinaryString(n-1));
			System.out.println(Integer.toBinaryString(3 & 0));
	}

}

class DeliveryCost {
	public int u;
	public int v;
	public int cost;

	public DeliveryCost(int u, int v, int cost) {
		this.u = u;
		this.v = v;
		this.cost = cost;
	}

}
