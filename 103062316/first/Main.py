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
 
y = odesolver.Euler(y, x, h, N, order)  # Your algorithm 
print("Results of Euler method:") 
eval_error.error_output(y[:,[0]],x)  # evaluate error value of the computed y values,  
									 # input x array and the first column of y  
 
y = odesolver.IE(y, x, h, N, order)  # Your algorithm 
print("Results of Improved Euler method:") 
eval_error.error_output(y[:,[0]],x)  


y = odesolver.RK (y, x, h, N, order)  # Your algorithm 
print("Results of Runge-Kutta method:") 
eval_error.error_output(y[:,[0]],x)


y = odesolver.RKF(y, x, h, N, order)  # Your algorithm 
print("Results of Runge–Kutta–Fehlberg method:") 
eval_error.error_output(y[:,[0]],x)  

#y = odesolver.AM (y, x, h, N, order)  # Your algorithm 
print("Results of Adams-Moulton method:") 
print("not finished yet")
#eval_error.error_output(y[:,[0]],x) 


tEnd = time.time() 
print("Total execution time:") 
print(tEnd - tStart) 

