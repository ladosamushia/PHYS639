import math as ma 
import matplotlib.pyplot as plt
#define the input function 
def f(x):
    y=x**2-1
    return y
xi=2#start of integration 
xf=7#end of integration
n=1000# defines the accuracy of the definite integration 
h=(abs(xf-xi))/n #marching step size
xd=xi#dummy march variable
I=0#intgrated value for the iterative process
while xd<=xf :#this will maje xd march till xf
    if (f(xd)*f(xd+h))>0: #condition to there is any cross over y=0 line
        I=(1/2)*(f(xd)+f(xd+h))*h+I
    else: #if there is cross over then it is no more trapezoid 
        print('found a crossover')
        delta=abs(f(xd)-f(xd+h))
        print(delta)
        print(n*h)
        if delta>h*n:#checking discontinuity
            print('This crossover is not smooth but a jump')
        elif f(xd)>0 and f(xd+h)<0:
            b1=(f(xd)/(f(xd)+abs(f(xd+h))))*h#getting the base of the triangle
            I1=(1/2)*f(xd)*b1+(1/2)*f(xd)*abs(h-b1)
            I=I+I1
        elif f(xd)<0 and f(xd+h)>0:
            b2=(abs(f(xd))/(abs(f(xd))+f(xd+h)))*h#getting the base of the triangle
            I2=(1/2)*f(xd)*b2+(1/2)*f(xd)*abs(h-b2)
            I=I+I2
    xd=xd+h
print('Integrated value :'+str(I))    
