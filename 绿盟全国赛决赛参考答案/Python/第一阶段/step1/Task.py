# -*- coding: utf-8 -*-
class Task:

    def sort(self,xlist):
    #********* Begin *********#
        global swapped1
        global swapped2
        swapped1 = 0
        swapped2 = 0
        left = 0
        right = len(xlist) - 1
        while left < right:
            for i in range(left,right):
                if xlist[i] > xlist[i + 1]:
                    self.Swap(xlist, i, i + 1)
                    swapped1 = 1
                    print(' '.join(map(str, xlist)))
            right -= 1

            for i in range(right,left,-1):
                if xlist[i - 1] > xlist[i]:
                    self.Swap(xlist, i - 1, i)
                    swapped2 = 1
                    print(' '.join(map(str, xlist)))
            left += 1
        if swapped1 == 0 and swapped2 == 0:
            print(' '.join(map(str, xlist)))        
    
    def Swap(self,xlist,i,j):
        temp = xlist[i]
        xlist[i] = xlist[j]
        xlist[j] = temp
    #********* End *********#