import numpy as np 
import function_x_y 

def Euler(y, x, h, N, order):     
# fill in your implementation here   

    [m] = function_x_y.funcxy(y[0],x[0])

    for i in range(1,int(N+1)):
        y[i][0] = h*(m) + y[i-1][0]
        [m] = function_x_y.funcxy(y[i],x[i])
    return y


def IE(y, x, h, N, order):     
# fill in your implementation here   

    [m] = function_x_y.funcxy(y[0],x[0])
    k1 = h*(m)

    [n] = function_x_y.funcxy(y[0]+k1,x[1])
    k2 = h*(n)


    for i in range(1,int(N+1)):
        y[i][0] = 0.5*(k1+k2) + y[i-1][0]

        if i+1 > N:
            break

        [m] = function_x_y.funcxy(y[i],x[i])
        k1 = h*(m)

        [n] = function_x_y.funcxy(y[i]+k1,x[i+1])
        k2 = h*(n)

    return y

def RK(y, x, h, N, order):     
# fill in your implementation here   

    [m] = function_x_y.funcxy(y[0],x[0])
    k1 = h*(m)

    [n] = function_x_y.funcxy(y[0]+k1/2,x[0]+h/2)
    k2 = h*(n)

    [p] = function_x_y.funcxy(y[0]+k2/2,x[0]+h/2)
    k3 = h*(p)

    [q] = function_x_y.funcxy(y[0]+k3,x[1])
    k4 = h*(q)

    for i in range(1,int(N+1)):
        y[i][0] = (1/6)*(k1+2*k2+2*k3+k4) + y[i-1][0]

        if i+1 > N:
            break

        [m] = function_x_y.funcxy(y[i],x[i])
        k1 = h*(m)

        [n] = function_x_y.funcxy(y[i]+k1/2,x[i]+h/2)
        k2 = h*(n)

        [p] = function_x_y.funcxy(y[i]+k2/2,x[i]+h/2)
        k3 = h*(p)

        [q] = function_x_y.funcxy(y[i]+k3,x[i+1])
        k4 = h*(q)
    return y


def RKF(y, x, h, N, order):     
# fill in your implementation here   

    [m] = function_x_y.funcxy(y[0],x[0])
    k1 = h*(m)

    [n] = function_x_y.funcxy(y[0]+(k1/4),x[0]+(h/4))
    k2 = h*(n)

    [p] = function_x_y.funcxy(y[0]+(3*k1/32)+(9*k2/32),x[0]+(3*h/8))
    k3 = h*(p)

    [q] = function_x_y.funcxy(y[0]+(1932*k1/2197)-(7200*k2/2197)+(7296*k3/2197),x[0]+(12*h/13))
    k4 = h*(q)

    [s] = function_x_y.funcxy(y[0]+(216*k1/439)-(8*k2)+(3680*k3/513)-(845*k4/4104),x[1])
    k5 = h*(s)

    [t] = function_x_y.funcxy(y[0]-(8*k1/27)+(2*k2)-(3544*k3/2565)+(1859*k4/4104)-(11*k5/40),x[0]+h/2)
    k6 = h*(t)

    for i in range(1,int(N+1)):
        y[i][0] = 16*k1/135+6656*k3/12825+28561*k4/56430-9*k5/50+2*k6/55 + y[i-1][0]

        if i+1 > N:
            break

        [m] = function_x_y.funcxy(y[i],x[i])
        k1 = h*(m)

        [n] = function_x_y.funcxy(y[i]+k1/4,x[i]+h/4)
        k2 = h*(n)

        [p] = function_x_y.funcxy(y[i]+3*k1/32+9*k2/32,x[i]+3*h/8)
        k3 = h*(p)

        [q] = function_x_y.funcxy(y[i]+1932*k1/2197-7200*k2/2197+7296*k3/2197,x[i]+12*h/13)
        k4 = h*(q)

        [s] = function_x_y.funcxy(y[i]+216*k1/439-8*k2+3680*k3/513-845*k4/4104,x[i+1])
        k5 = h*(s)

        [t] = function_x_y.funcxy(y[i]-8*k1/27+2*k2-3544*k3/2565+1859*k4/4104-11*k5/40,x[i]+h/2)
        k6 = h*(t)
    return y