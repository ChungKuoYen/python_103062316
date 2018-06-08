#Example1 : first order ODE 
import numpy as np 
import math 
def funcxy(y, x):  #standard form of y' = x + y     
	
	return [       x+y[0]       ]

order = 1 
x0 = 0 #staring point of the solution interval 
xN = 1 #end point of the solution interval 
y0 = 0 #initial condition of y(x0), y'(x0), y''(x0), … 
