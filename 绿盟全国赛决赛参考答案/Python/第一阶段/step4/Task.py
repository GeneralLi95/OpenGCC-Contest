# -*- coding: utf-8 -*-
import math 
import numpy
class Task:

    def love(self,n):
    #********* Begin *********#
        if n == 1:
            for y in numpy.arange(1.3,-1.1,-0.06):
                for x in numpy.arange(-1.2,1.2001,0.025):
                    if math.pow((x*x+y*y-1.0),3)- x*x*y*y*y <= 0.0:
                        print(' ',end='')
                    else:
                        print('$',end='')
                print()
            return ''

        else:
            s = "I love you!"
            for y in numpy.arange(1.3,-1.1,-0.06):
                index = 0
                for x in numpy.arange(-1.1,1.100001,0.025):
                    if x*x + math.pow(5.0*y/4.0-math.sqrt(math.fabs(x)),2) - 1 <= 0.0 :                        
                        print(s[(index)%len(s)],end='')
                        index += 1
                    else:
                        print(' ',end='')
                print()
            return ''

                
    #********* End *********#
    