# -*- coding: utf-8 -*-
class Task:

    def concaveValley(self,X):
        res = 0
        up = 0
        down = 0
        for i in range(1, len(X)):
            if up > 0 and X[i - 1] > X[i] or X[i - 1] == X[i]:
                up = down = 0
            if X[i - 1] < X[i]:
                up += 1
            if X[i - 1] > X[i]:
                down += 1
            if up > 0 and down > 0 and up + down + 1 > res:
                res = up + down + 1
        return res
