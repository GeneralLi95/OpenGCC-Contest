# -*- coding: utf-8 -*-
class Task:

    def virusArea(self,n,m,area):
    #********* Begin *********#
        if area is None: return None
        if area == []: return 0
        # 当数组不为空时，计算行数和列数
        self.c = n
        self.d = m
        x = 0
        for i in range(self.c):
            for j in range(self.d):
                if area[i][j] == 'o':
                    x += 1
                    area = self.change(area, i, j)
        return x

    def change(self, area, i, j):
        area[i][j] = 0
        if i > 0 and area[i - 1][j] == 'o':
            # 置当前点上边的点为0
            area = self.change(area, i - 1, j)
        if i < self.c - 1 and area[i + 1][j] == 'o':
            # 置当前点下边的点为0
            area = self.change(area, i + 1, j)

        if j < self.d - 1 and area[i][j + 1] == 'o':
            # 置当前点右方的点为0
            area = self.change(area, i, j + 1)
        if j > 0 and area[i][j - 1] == 'o':
            # 置当前点左方的点为0
            area = self.change(area, i, j - 1)
        return area
	
	#********* End *********#


