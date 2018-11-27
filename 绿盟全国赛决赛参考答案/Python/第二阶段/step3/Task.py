class DeliveryCost:
    def __init__(self, u, v,cost):
        self.u = u
        self.v = v
        self.cost = cost
kMaxN = 55
kMaxM = 10
kMaxS = 1024

class Task:
    def solve(self, n, cost_e, employees, cost_b):
#********* Begin *********#
        #初始化二维列表并设置每个元素为无穷大
        floyd = [[float("inf")]*kMaxN for _ in range(kMaxN)]

        for i in range(1,n+1):
            floyd[i][i] = 0
        m = len(cost_e)
        for i in range(m):
            a = cost_e[i].u
            b = cost_e[i].v
            floyd[a][b] = cost_e[i].cost
            floyd[b][a] = cost_e[i].cost

        for k in range(1,n+1):
            for i in range(1,n+1):
                for j in range(1,n+1):
                    floyd[i][j] = min(floyd[i][j],floyd[i][k]+floyd[k][j])

        f = [[float("inf")]*kMaxN for _ in range(kMaxS)]
        for i in range(1,n+1):
            f[0][i] = 0
        num_employees = len(employees)
        for i in range(num_employees):
            f[1 << i][employees[i]] = 0

        num_states = 1 << num_employees

        for i in range(num_states):
            for j in range(1,n+1):
                s = i & (i - 1)
                while s > 0:
                    f[i][j] = min(f[i][j], f[s][j] + f[i - s][j])
                    s = (s-1)&i

            for j in range(1,n+1):
                for k in range(1,n+1):
                    f[i][j] = min(f[i][j],f[i][k] + floyd[k][j])

        g = [float("inf")]*kMaxS
        for i in range(num_states):
            for j in range(num_employees):
                if ((i >> j)&1) >0:
                    g[i] = min(g[i],f[i][employees[j]] + cost_b[j])

        h = [float("inf")]*kMaxS
        for i in range(num_states):
            h[i] = g[i]

            s = i & (i - 1)
            while s > 0:
                h[i] = min(h[i],h[s] + g[i-s])
                s = (s - 1) & i

        return h[num_states - 1]

#********* End *********#


