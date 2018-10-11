import numpy as np
import cv2
import numpy.random as random  
def step(s,ch):
    if ch==1:
        s=s+[0,-1]
    if ch==2:
        s=s+[-1,1]
    if ch==3:
        s=s+[0,1]
    if ch==4:
        s=s+[1,1]
    if ch==5:
        s=s+[1,0]
    if ch==6:
        s=s+[1,-1]
    if ch==7:
        s=s+[0,-1]
    if ch==8:
        s=s+[-1,-1]
    return s
def add_box(bx,pos):
    pos=pos+100#(0,0) is at (100,100) 
    bx[int(pos[0]),int(pos[1])]=bx[int(pos[0]),int(pos[1])]+1
    return bx
def check_roll(pos):
    if abs(pos[0])<=99 and abs(pos[1])<=99:
        c=np.array([1,2,3,4,5,6,7,8])
        ch=random.choice(c)
    if pos[0]>=100 and abs(pos[1])<=99:#horizontal bound(right)
        c=np.array([1,2,3,8,7])
        ch=random.choice(c)
    if pos[0]<=-100 and abs(pos[1])<=99:#horizontal bound(left)
        c=np.array([3,4,5,6,7])
        ch=random.choice(c)
    if pos[1]>=100 and abs(pos[0])<=99:#vertical bound(top)
        c=np.array([1,8,7,5,6])
        ch=random.choice(c)
    if pos[1]<=-100 and abs(pos[0])<=99:#vertical bound(down)
        c=np.array([1,2,3,4,5])
        ch=random.choice(c)    
    if pos[0]>=100 and pos[1]>=100:#corner
        c=np.array([1,8,7])
        ch=random.choice(c)
    if pos[0]>=100 and pos[1]<=-100:#corner
        c=np.array([1,2,3])
        ch=random.choice(c)    
    if pos[0]<=-100 and pos[1]<=-100:#corner
        c=np.array([3,4,5])
        ch=random.choice(c)  
    if pos[0]<=-100 and pos[1]>=100:#corner
        c=np.array([5,7,6])
        ch=random.choice(c)    
    return ch
Nstep=100
t=np.linspace(0,10,Nstep)
n=400#particles
l=201#box lenght

pos=np.zeros((n,2))#tracking position of particle at each step
print(pos)
print(pos[1,:])
for k in range(0,Nstep):
    box=np.zeros((l,l))    
    for i in range(0,n):
        if k==0:
            box=add_box(box,pos[i,:])
        else:
            ch=check_roll(pos[i,:])#checking if particle hits side of the container
            pos[i,:]=step(pos[i,:],ch)
            box=add_box(box,pos[i,:])
            
    #show distributions at each step 
    print(box)  
    boxr=cv2.resize(box, (960, 540)) 
    #rgb_img = cv2.cvtColor(boxr, cv2.CV_GRAY2RGB)
    #boxc = cv2.applyColorMap(boxr, cv2.COLORMAP_JET)
    cv2.imshow('g',boxr)

    if cv2.waitKey(500):
        continue
cv2.destroyAllWindows()
#import numpy as np
#import cv2
#from matplotlib import pyplot as plt

#img = cv2.imread('messi5.jpg',0)
#plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
#plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
#plt.show()
