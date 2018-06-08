
#Example1 : first order ODE 
import numpy as np 
import math 





def funcxy(y, x):  #standard form of y' = x + y     
	
	return [       y[1],
                    -0.75*y[0]-2*y[1]
         ]

order = 2
x0 = 0 #staring point of the solution interval 
xN = 1 #end point of the solution interval 
y0 = [3,-1.5] #initial condition of y(x0), y'(x0), y''(x0), … 
