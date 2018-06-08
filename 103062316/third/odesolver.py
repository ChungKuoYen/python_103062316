import numpy as np 
import function_x_y 


def RK(y, x, h, N, order):     
# fill in your implementation here   

    if order == 1:

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
    
    if order == 2:
        [m,n] = function_x_y.funcxy(y[0],x[0])
        k11 = h*(m)
        k12 = h*(n)

        a = [y[0][0]+k11/2 ,y[0][1]+k12/2] 
        [m,n] = function_x_y.funcxy(a,x[0]+h/2)
        k21 = h*(m)
        k22 = h*(n)

        a = [y[0][0]+k21/2 ,y[0][1]+k22/2] 
        [m,n] = function_x_y.funcxy(a,x[0]+h/2)
        k31 = h*(m)
        k32 = h*(n)

        a = [y[0][0]+k31/2 ,y[0][1]+k32/2]
        [m,n] = function_x_y.funcxy(a,x[1])
        k41 = h*(m)
        k42 = h*(n)

        for i in range(1,int(N+1)):
            y[i][0] = (1/6)*(k11+2*k21+2*k31+k41) + y[i-1][0]
            y[i][1] = (1/6)*(k12+2*k22+2*k32+k42) + y[i-1][1]

            if i+1 > N:
                break
            [m,n] = function_x_y.funcxy(y[i],x[i])
            k11 = h*(m)
            k12 = h*(n)

            a = [y[i][0]+k11/2 ,y[i][1]+k12/2] 
            [m,n] = function_x_y.funcxy(a,x[i]+h/2)
            k21 = h*(m)
            k22 = h*(n)

            a = [y[i][0]+k21/2 ,y[i][1]+k22/2] 
            [m,n] = function_x_y.funcxy(a,x[i]+h/2)
            k31 = h*(m)
            k32 = h*(n)

            a = [y[i][0]+k31/2 ,y[i][1]+k32/2]
            [m,n] = function_x_y.funcxy(a,x[i+1])
            k41 = h*(m)
            k42 = h*(n)

        return y

    if order == 3:
        [m,n,s] = function_x_y.funcxy(y[0],x[0])
        k11 = h*(m)
        k12 = h*(n)
        k13 = h*(s)

        a = [y[0][0]+k11/2 ,y[0][1]+k12/2 ,y[0][2]+k13/2] 
        [m,n,s] = function_x_y.funcxy(a,x[0]+h/2)
        k21 = h*(m)
        k22 = h*(n)
        k23 = h*(s)

        a = [y[0][0]+k21/2 ,y[0][1]+k22/2 ,y[0][2]+k23/2] 
        [m,n,s] = function_x_y.funcxy(a,x[0]+h/2)
        k31 = h*(m)
        k32 = h*(n)
        k33 = h*(s)

        a = [y[0][0]+k31/2 ,y[0][1]+k32/2 ,y[0][2]+k33/2]
        [m,n,s] = function_x_y.funcxy(a,x[1])
        k41 = h*(m)
        k42 = h*(n)
        k43 = h*(s)

        for i in range(1,int(N+1)):
            y[i][0] = (1/6)*(k11+2*k21+2*k31+k41) + y[i-1][0]
            y[i][1] = (1/6)*(k12+2*k22+2*k32+k42) + y[i-1][1]
            y[i][2] = (1/6)*(k13+2*k23+2*k33+k43) + y[i-1][2]

            if i+1 > N:
                break

            [m,n,s] = function_x_y.funcxy(y[i],x[i])
            k11 = h*(m)
            k12 = h*(n)
            k13 = h*(s)

            a = [y[i][0]+k11/2 ,y[i][1]+k12/2 ,y[i][2]+k13/2] 
            [m,n,s] = function_x_y.funcxy(a,x[i]+h/2)
            k21 = h*(m)
            k22 = h*(n)
            k23 = h*(s)

            a = [y[i][0]+k21/2 ,y[i][1]+k22/2 ,y[i][2]+k23/2] 
            [m,n,s] = function_x_y.funcxy(a,x[i]+h/2)
            k31 = h*(m)
            k32 = h*(n)
            k33 = h*(s)

            a = [y[i][0]+k31/2 ,y[i][1]+k32/2 ,y[i][2]+k33/2]
            [m,n,s] = function_x_y.funcxy(a,x[i+1])
            k41 = h*(m)
            k42 = h*(n)
            k43 = h*(s)
        return y
 