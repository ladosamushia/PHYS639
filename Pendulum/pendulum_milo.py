import numpy as np
import matplotlib.pyplot as plt


#variables
q = 0       #dampening force const
g = 9.8     # gravity
L = 5       # length of pendulum
th = np.deg2rad(30)     # initial angle of pendelum in degrees
th1 = 0                 # initial speed of pendulum dth/dt0
t0 = 0                  # initial time
dt = 0.001

om = np.sqrt(g/L)

theta = np.array([])    # store theta values (th) at i
time = np.array([])     # store time values (t0) at i


# use for Fext in part 3
Fmax = 1
Omega = om

#loop and store (t,th) i times
for i in range(0,10000):
    Fext = Fmax*np.sin(Omega*t0) # Use in part (3)
    th2 = (-g/L)*np.sin(th) - q*th1 + Fext    # d2th/dth02 --> for (1) the simple pendulum, make q and Fmax equal to zero. For (2) the damped pendulum, set Fmax to 0
    th1 += th2*dt
    th += th1*dt
    t0 += dt
    theta = np.append(theta, th)
    time = np.append(time, t0)

#    print(t,t0,th2,th1,th,dt)

plt.plot(time,theta)

