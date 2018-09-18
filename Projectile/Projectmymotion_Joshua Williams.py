import numpy as np
import matplotlib.pyplot as plt

REarth = 6371000.0
x = 0
y = 0
vx = 100
vy = 100
g = -9.81
t = 0
dt = 0.001
xarr=np.array([x])
yarr=np.array([y])

while y > 0 or t == 0:
    x += vx * dt #new x,y
    y += vy * dt
    vy += g * dt#only vy changes here
    t += dt
    x_arr=np.append(xarr,x)
    y_arr=np.append(yarr,y)

print('Distance: %.2f' %(x))
print()
#hand calculations say this distance should be about 550m(very roughly calculated)
#which is close to this computed value
plt.figure(1)
plt.title('Work with me now')
plt.plot(xarr,yarr)
plt.xlabel('X Range (m)')
plt.ylabel('Y Range (m)')
plt.show
#plot not plotting correctly, nevertheless the code produces the calculated distance.
__________________________________________________


#proj. motion 2
#add air resistance
import numpy as np
import matplotlib.pyplot as plt
#from 1
x = 0
y = 0
vx = 100
vy = 100
g = -9.81
t = 0
dt = 0.001
xarr=np.array([x])
yarr=np.array([y])

while y > 0 or t == 0:
    m=1#mass(kg) let equal to 1 because easy
    theta = (45*np.pi)/180
    x += vx * dt
    y += vy * dt
    x_arr=np.append(xarr,x)
    y_arr=np.append(yarr,y)
    t += dt
    v = (vx**2 + vy**2)**.5 #total vel. from kinematic eqs
    fdrag = m * (-.00004*(v**2))
    fxdrag= fdrag*np.cos(theta)
    fydrag= fdrag*np.sin(theta)
    vy += (g*dt) + (fydrag*dt)
    vx += -fxdrag * dt
    
print('Hor. distance', x)

plt.plot('Trajectory with drag')
plt.plot(xarr,yarr)
plt.xlabel('X Range (m)')
plt.ylabel('Y Range (m)')
#result is less than the previous problem, which is expected
#plot is still not working
___________________________________________________

#changing gravity
import numpy as np
import matplotlib.pyplot as plt

x = 0
y = 0
vx = 100
vy = 100
t = 0
dt = 0.001

def fdragx(vx, vy, y):
    return -0.00004 * vx * np.sqrt(vx ** 2 + vy ** 2) * (1 - 2.2E-5 * y) ** (5 / 2)

def fdragy(vx, vy, y):
    return -0.00004 * vy * np.sqrt(vx ** 2 + vy ** 2) * (1 - 2.2E-5 * y) ** (5 / 2)

def g(y):
    return -(6.67408E-11) * (5.972E24) / ((y + 6.3781E6) ** 2)

while y > 0 or t == 0:
    m=1#mass(kg) let equal to 1 because easy
    theta = (45*np.pi)/180
    x += vx * dt
    y += vy * dt
    t += dt
    vy += (g(y) + fdragy(vx,vy,y)) * dt
    vx += -fdragx(vx,vy,y) * dt
    
print ('Trajectory w/drag and changing gravity')
print('distance: %.2f' %(x))
print()
#We would expect the distance to increase.
#The distance did increase, but by a wide margin.
#I am uncertain if the distance would increase that much, but is feasible.
