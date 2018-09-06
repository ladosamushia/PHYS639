import math as ma 
import matplotlib.pyplot as plt
#define the input function 
def f(x):
    y=ma.exp(-x-1)/(x+1)
    return y
root=[]
xi=-2#initial bound
xf=7#final bound
n=1000# defines the accuracy 
h=(abs(xf-xi))/n #marching step size
xd=xi

while xd <= xf :#this will maje xd march till xf
    if (f(xd)*f(xd+h))>0:#condition to there is any cross over y=0 line
        xd=xd+h
    else: 
        print('found a crossover')
        delta=abs(f(xd)-f(xd+h))
        print(delta)
        print(n*h)
        if delta>h*n:#checking discontinuity
            print('This crossover is not a root but a jump at '+str(xd))
        else :
            root.append(xd)
        xd=xd+h        
if (len(root) != 0) :
    print('root somewhere near:'+str(root))
else:
    print('no root found here in this bounds')    