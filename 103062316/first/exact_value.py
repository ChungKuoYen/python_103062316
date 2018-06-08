from scipy.integrate import odeint 
import numpy as np 
import math 
import function_x_y 
 
def exacty(x):  #Note: x is a linspace array          
	Nplus1 = len(x)     
	y = np.ndarray([Nplus1,1])          
	for i in range(0,Nplus1):         
		y[i] = math.exp(x[i]) - x[i] - 1   
	#standard solution to y’ = x + y                      
	return y  #Note: y is an 1 column array
 
#You can also use python package to get exact_value 
#by calling the function odeint from scipy 
#Example : y = odeint(function_x_y.funcxy, y0 , x) 
