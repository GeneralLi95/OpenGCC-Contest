#ifndef SOLVER_H_
#define SOLVER_H_

#include <bits/stdc++.h>
using namespace std;

struct Operation {
  char op;
  int x;
  int y;
};
///////// code //////////////////
const long long MOD = 1000000007;
const int maxn=1e5+10;
long long C1[maxn];
long long C2[maxn];
inline int lowbit(int x)
{
    return x&(-x);
}
inline long long Sum(long long C[], int n)
{
    long long sum = 0;
    while (n>0) {
        sum = (sum+C[n])%MOD;
        n -= lowbit(n);
    }
    return sum%MOD;
}
inline void change(long long C[], int pos, long long num, int n)
{
    while (pos<=n) {
        C[pos] = (C[pos]+num)%MOD;
        pos += lowbit(pos);
    }
}
class Solver {
 public:
  int solve(vector<int> data, vector<Operation> operations) {
    /*********begin*********/
	int n = (int)data.size();
    int m = (int)operations.size();
    
    for (int i=1; i<=n; i++) {
        change(C1, i, (long long)data[i-1], n);
        change(C2, i, (long long)data[i-1]*i, n);
    }
    
    long long ans = 0;
    for (int i=0; i<m; i++) {
        char op = operations[i].op;
        int x = operations[i].x+1;
        int y = operations[i].y+1;
        if (op=='C') {
            long long item1 = (y-1-data[x-1]+MOD)%MOD;
            long long item2 = (y-1-data[x-1]+MOD)%MOD*x%MOD;
            change(C1, x, item1, n);
            change(C2, x, item2, n);
            data[x-1] = y-1;
        }else if(op=='L'){
            long long tmp1 = ((Sum(C1, y) - Sum(C1, x-1) + MOD)%MOD)*(x-1)%MOD;
            long long tmp2 = (Sum(C2, y) - Sum(C2, x-1) + MOD)%MOD;
            long long tmp = (tmp2-tmp1+MOD)%MOD;
            ans += tmp;
            ans %= MOD;
        }else if(op=='R'){
            long long tmp1 = ((Sum(C1, y) - Sum(C1, x-1) +MOD)%MOD)*(y+1)%MOD;
            long long tmp2 = (Sum(C2, y) - Sum(C2, x-1) + MOD)%MOD;
            long long tmp = (tmp1-tmp2+MOD)%MOD;
            ans += tmp;
            ans %= MOD;
        }
    }
    ans %= MOD;
    return (int)ans;

    /*********end*********/
  }
};

#endif