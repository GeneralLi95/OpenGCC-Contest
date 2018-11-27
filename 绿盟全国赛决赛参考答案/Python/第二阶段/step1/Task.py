# -*- coding: utf-8 -*-
import math
class Task:
   
    def solve(self,x1,y1,r1,x2,y2,r2):
    #********* Begin *********#
        kPi = math.acos(-1.0)
        d = math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))
        area1 = r1 * r1 * kPi
        area2 = r2 * r2 * kPi
        if d >= (r1 + r2):
            return area1 + area2
        elif d <= (r1 - r2) or d <= (r2 - r1):
            return max(area1,area2)
        else:
            alpha = 2.0 * math.acos((d * d + r1 * r1 - r2 * r2) / (2.0 * d * r1))
            beta = 2.0 * math.acos((d * d + r2 * r2 - r1 * r1) / (2.0 * d * r2))
            area = area1 * (2.0 * kPi - alpha) / (2.0 * kPi) + area2 * (2.0 * kPi - beta) / (2.0 * kPi) + 0.5 * r1 * r1 * math.sin(alpha) + 0.5 * r2 * r2 * math.sin(beta)
            return area
    #********* End *********#