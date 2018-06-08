from scipy.integrate  import odeint 

import numpy as np 
import math 
import function_x_y 

#You can also use python package to get exact_value 
#by calling the function odeint from scipy 
#Example : y = odeint(function_x_y.funcxy, y0 , x) 
def exacty(x):  #Note: x is a linspace array          
	
    def g(y, x):
        y0 = y[0]
        y1 = math.exp((-1)* x **2)
        return y1

        # Initial conditions on y, y' at x=0
    init = 1
        # First integrate from 0 to 2
    a = np.linspace(0,1,1001)
    sol=odeint(g, init, a)


    return sol[:,[0]]  #Note: y is an 1 column array 
"""
def exacty(x):  #Note: x is a linspace array          
	
    def g(y, x):
        y0 = y[0]
        y1 = y[1]    				 
        y2 = (-1)/x*y[1]-y[0]
        return y1,y2

        # Initial conditions on y, y' at x=0
    init = 0,0
        # First integrate from 0 to 2
    a = np.linspace(1,2,1001)
    sol=odeint(g, init, a)


    return sol[:,[0]]  #Note: y is an 1 column array 
"""
"""
def exacty(x):  #Note: x is a linspace array          
	
    def g(y, x):
        y0 = y[0]
        y1 = y[1]    				 
        y2 = y[2]
        y3 = (-1)/2*y[0]*y[2]
        return y1,y2,y3


        # Initial conditions on y, y' at x=0
    init = 0,0,0.332
        # First integrate from 0 to 2
    a = np.linspace(0,1,1001)
    sol=odeint(g, init, a)


    return sol[:,[0]]  #Note: y is an 1 column array 

"""