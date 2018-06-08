#Example1 : first order ODE 
import numpy as np 
import math 

def funcxy(y, x):      
	return [          math.exp((-1)* x **2)         ] 
 
order = 1 
x0 = 0 #staring point of the solution interval 
xN = 1 #end point of the solution interval 
y0 = 1 #initial condition of y(x0), y'(x0), y''(x0), … 
"""
#Example2 : high order ODE 

def funcxy(y,x):  #standard form of    
	return [        y[1],          
					(-1)/x*y[1]-y[0] ,  
		            
                    ]
order = 2
x0 = 1 #staring point of interval 
xN = 2 #end point of interval 
y0 = [0,0]  #initial condition of y(x0), y'(x0) 
"""
#Example3 : high order ODE 
"""
def funcxy(y,x):  #standard form of 
	return [        y[1],           
					y[2] ,            
		            (-1)/2*y[0]*y[2]
                    ]
order = 3
x0 = 0 #staring point of interval 
xN = 1 #end point of interval 
y0 = [0,0,0.332]  #initial condition of y(x0), y'(x0) 
"""