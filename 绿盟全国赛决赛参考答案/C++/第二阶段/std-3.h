#ifndef SOLVER_H_
#define SOLVER_H_

#include <bits/stdc++.h>
using namespace std;

const int kMaxN = 55;
const int kMaxM = 10;
const int kMaxS = 1024;

struct DeliveryCost {
  int u;
  int v;
  int cost;
};

class Solver {
 public:
  double solve(int n,
               vector<DeliveryCost> cost_e,
               vector<int> employees,
               vector<int> cost_b) {
    /*********begin*********/
    static int floyd[kMaxN][kMaxN];
    memset(floyd, 0x3f, sizeof(floyd));
    for (int i = 1; i <= n; ++i) {
      floyd[i][i] = 0;
    }
    int m = cost_e.size();
    for (int i = 0; i < m; ++i) {
      int a = cost_e[i].u;
      int b = cost_e[i].v;
      floyd[a][b] = cost_e[i].cost;
      floyd[b][a] = cost_e[i].cost;
    }
    for (int k = 1; k <= n; ++k) {
      for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= n; ++j) {
          floyd[i][j] = min(floyd[i][j], floyd[i][k] + floyd[k][j]);
        }
      }
    }

    static int f[kMaxS][kMaxN];
    memset(f, 0x3f, sizeof(f));
    for (int i = 1; i <= n; ++i) {
      f[0][i] = 0;
    }
    int num_employees = employees.size();
    for (int i = 0; i < num_employees; ++i) {
      f[1 << i][employees[i]] = 0;
    }
    int num_states = 1 << num_employees;
    for (int i = 0; i < num_states; ++i) {
      for (int j = 1; j <= n; ++j) {
        for (int s = i & (i - 1); s; s = (s - 1) & i) {
          f[i][j] = min(f[i][j], f[s][j] + f[i - s][j]);
        }
      }
      for (int j = 1; j <= n; ++j) {
        for (int k = 1; k <= n; ++k) {
          f[i][j] = min(f[i][j], f[i][k] + floyd[k][j]);
        }
      }
    }

    static int g[kMaxS];
    memset(g, 0x3f, sizeof(g));
    for (int i = 0; i < num_states; ++i) {
      for (int j = 0; j < num_employees; ++j) {
        if ((i >> j) & 1) {
          g[i] = min(g[i], f[i][employees[j]] + cost_b[j]);
        }
      }
    }

    static int h[kMaxS];
    for (int i = 0; i < num_states; ++i) {
      h[i] = g[i];
      for (int s = i & (i - 1); s; s = (s - 1) & i) {
        h[i] = min(h[i], h[s] + g[i - s]);
      }
    }

    return h[num_states - 1];
    /*********end*********/
  }
};

#endif
