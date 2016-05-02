import numpy as np
import random as rd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

G = 4.302*(10**-3) #pc (km/s)^2 / Msun
divpot = 0
N = 100
vel = 200 # km/s
pos = 16000 # pc
stepsize = 100 #s
rd.seed(10)
x = np.array([rd.uniform(-pos,pos) for i in range(N)])
y = np.array([rd.uniform(-pos,pos) for i in range(N)])
z = np.array([rd.uniform(-pos,pos) for i in range(N)])
vx = np.array([rd.uniform(-vel,vel) for i in range(N)])
vy = np.array([rd.uniform(-vel,vel) for i in range(N)])
vz = np.array([rd.uniform(-vel,vel) for i in range(N)])
mass = np.ones(len(x))

coords = np.array(list(zip(x,y,z)))
velocities = np.array(list(zip(vx,vy,vz)))

def force(m1, m2, p1, p2, divpot):
    t = G*m1*m2*(p1-p2)
    b = np.linalg.norm(p1-p2)**3
    return t/b - divpot

import pdb
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(coords[:,0], coords[:,1], coords[:,2], s=0.1)

while(True):
    for i in range(len(coords)):
        Fi = np.zeros(3)
        for j in range(len(coords)):
            if i != j:
                Fi += force(mass[i], mass[j], coords[i], coords[j], divpot)
        velocities[i]+=stepsize*Fi
        coords[i]+=stepsize*velocities[i]
        ax.scatter(coords[i,0], coords[i,1], coords[i,2], s=0.1)
    plt.show()
    pdb.set_trace()
