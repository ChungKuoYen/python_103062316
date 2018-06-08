import numpy as np 
import matplotlib.pyplot as plt 
from exact_value import exacty 
 
def error_output(y_approx, x):   

	print("Output") 
	print("Approximated values of y:") 
	print(y_approx)
	print("Exact values of y:") 
	print(exacty(x)) 
	print("Maximum error:") 

	y = exacty(x)

	print(abs(y[-1]-y_approx[-1])) 
