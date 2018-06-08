import numpy as np 
import function_x_y 
import odesolver 
import eval_error 
import time 
 
#Initiating parameters, try to get each value from function_x_y.py 


x0 =  function_x_y.x0
xN =  function_x_y.xN
order =  function_x_y.order
 
 
#Specify h and calculate N 
h =  0.001
N = (xN - x0)/h 
 
#Declaring x and y 
x = np.linspace(x0, xN, N + 1)   
y = np.ndarray([len(x), order]) 
 
# Initializing the first element of y to be the initial condition 
y[0] =  function_x_y.y0
 
#DO NOT change anything below!! 
 
tStart = time.time()  #Process time computing 

y = odesolver.RK (y, x, h, N, order)  # Your algorithm 
print("Results of Frank-Runge-Kutta method:") 
eval_error.error_output(y[:,[0]],x) 

tEnd = time.time() 
print("Total execution time:") 
print(tEnd - tStart) 

