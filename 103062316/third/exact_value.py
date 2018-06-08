from scipy.integrate  import odeint 

import numpy as np 
import math 
import function_x_y 


def exacty(x):  #Note: x is a linspace array          
	
    def g(y, x):
        y0 = y[0]
        y1 = y[1]    				 
        y2 = -0.75*y[0]-2*y[1]

        return y1,y2


        # Initial conditions on y, y' at x=0
    init = 3,-1.5
        # First integrate from 0 to 2
    a = np.linspace(0,1,1001)
    sol=odeint(g, init, a)


    return sol[:,[0]]  #Note: y is an 1 column array 
