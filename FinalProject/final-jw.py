#final project-Joshua Williams
#I want to find range, launch angle, max altitude, flight time, etc. of an Icbm
import os
os.environ['PROJ_LIB'] = r'C:\Users\Skynet\Anaconda3\pkgs\proj4-5.2.0-hfa6e2cd_1001\Library\share'
from mpl_toolkits.basemap import Basemap #Basemap relies on a pkge call pyproj which is a pain to get to work without errors
import matplotlib.pyplot as plt
import numpy as np
import warnings
import math
import matplotlib.cbook
warnings.filterwarnings("ignore",category=matplotlib.cbook.mplDeprecation)
#simple Conceptualization
#For any two points on the earth consider the slice of the earth passing through both points and the earths center
#allows simple computations, but need to convert equations to polar coordinates
#Should essentially follow an elliptical path.
#list of constants
n=1000
g0=9.81
G=6.67*10**-11
M=5.97*10**24#mass of earth
R=6.371*10**6
m0=float(input('Enter mass of dry vehicle:'))
print('Dry vehicle mass:',m0)
mf=float(input('Enter mass of fuel:'))
print('Fuel Mass:', mf)
m=mf+m0
print('Total Mass of vehicle:', m)
print('Common values for vex range from 1000 to 4000m/s')
vex=float(input('Enter Velocity of exhaust:'))
v0=vex*(np.log(m/m0))
print(v0)
beta=float(input('Enter launch angle:'))
h=0
#let r be the height h above the surface added to the earths radius.
def r(h):
    return R+h
    
def g(h):
    return G*M/(r)**2
alpha=2*g0*R/(v0**2)
print('yer a is',alpha)
def Y(r):
    return r/R
H=-R+R*((alpha**2-4*(alpha-1)*(np.cos(beta*np.pi/180))**2)**.5)/(2*(alpha-1))
print(H)
def dtaudy(Y):#time to impact. Can't find a clean way to resolve beta via computer.
    return 2*R/v0*(Y)/(Y**2*(1-alpha)+alpha*Y-np.cos(beta*np.pi/180)**2)**.5
N=1000#applying trapezoidal rule to get tau
a=1
b=1+H/R
dN=(b-a)/N
tau=.5*dtaudy(a)+.5*dtaudy(b)
for k in range(1,N):
    tau+=dtaudy(a+k*dN)
Maxrange=dN*tau*v0*np.cos(beta*np.pi/180)
print('Time to impact:', dN*tau)
print(Maxrange)

#For some reason I am getting a negative answers for H and tau.
#Too many things are going wrong simultaneously and too little time to fix.

#ashes from previous document
#I messed up the derivation of a more generalized equation for missile motion, could have been really cool.
#Worked for very specific initial conditions, but once changed would get non-elliptic.
#I really should have fiddled around with the code to make sure it worked, but it is too late now, and I might have been a little too ambitious
    #equation of motion
##F=m(t)g=2m(t)(wxv)+m(t)wxrxw+T+Fa
##Fa=fd(v)+fl(v)=-.5p*Cd*A*|v|*v
##ma=mg-2m*cross(w,v)+m*cross(np.cross(w,r),w)+T-.5p(r-Re)Cd*A*v*np.norm(v)
# n=500
# dv=g-2*np.cross(w,v)+T-1/(2*M)
# r=np.array(x,y,z)#radial dist.
# w=np.array(0,0,wz)#Earth's angualr velocity
# T=np.array()

#Don't know how to directly plot pos(t) onto maps so I generate a list of points and map each point onto map
# fig = plt.figure(num=None, figsize=(12, 8) )
# m = Basemap(projection='merc',llcrnrlat=-80,urcrnrlat=80,llcrnrlon=-180,urcrnrlon=180,resolution='c')
# m.drawcoastlines()
# plt.title("Mercator Projection")
# plt.show()#flat map

# fig = plt.figure(num=None, figsize=(12, 8) )
# m = Basemap(projection='merc',llcrnrlat=-80,urcrnrlat=80,llcrnrlon=-180,urcrnrlon=180,resolution='c')
# m.drawcoastlines()
# m.fillcontinents(color='tan',lake_color='lightblue')
# # draw parallels and meridians.
# m.drawparallels(np.arange(-90.,91.,30.),labels=[True,True,False,False],dashes=[2,2])
# m.drawmeridians(np.arange(-180.,181.,60.),labels=[False,False,False,True],dashes=[2,2])
# m.drawmapboundary(fill_color='lightblue')
# plt.title("Mercator Projection")#coloured flat map

# fig = plt.figure(num=None, figsize=(12, 8) )
# m = Basemap(projection='moll',lon_0=0,resolution='c')    
# m.drawcoastlines()
# m.drawstates()
# m.fillcontinents(color='tan',lake_color='lightblue')
# # draw parallels and meridians.
# m.drawparallels(np.arange(-90.,91.,30.),labels=[True,True,False,False],dashes=[2,2])
# m.drawmeridians(np.arange(-180.,181.,60.),labels=[False,False,False,False],dashes=[2,2])
# m.drawmapboundary(fill_color='lightblue')
# plt.title("Mollweide Projection");
##I want to plot the path of the missile on atleast one of the mercator projections and on bluemarble

# plt.figure(figsize=(8, 8))
# m = Basemap(projection='ortho', resolution=None, lat_0=0, lon_0=0)
# m.bluemarble(scale=0.5);#proper globe