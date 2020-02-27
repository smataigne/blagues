from numpy import *
import matplotlib.pyplot as plt
import matplotlib.animation as anim


def waveSolve(beta, nx, nt, c, L, U0):
    
    F = zeros((nt, nx))
    F[0, 1:-1] = U0
    
    Un = F[0, :]
    k = linspace(1, nx-2, nx-2, dtype = "int")
    F[1, k] = U0 + beta**2*(Un[k+1]+Un[k-1]-2*Un[k])
    
    for i in range(2, nt):
        Un = F[i-1, :]
        Un_1 = F[i-2, :]
        F[i, k] = 2*Un[k] - Un_1[k] + beta*(Un[k+1]+Un[k-1]-2*Un[k])
    
    return F
    

nx = 30
nt = 5

dx = 1/nx
dt = 1/nt
c = 1
beta = c*dt/dx
print("/!\   beta={} <= 1".format(beta))

c = L = 0

x = linspace(-pi,pi,nx)
U0 = sin(x[1:-1])
U = waveSolve(beta, nx, nt, c, L, U0)
plt.figure()
plt.subplot(1,1,1)
plt.ylim = (-5.0,5.0)
plt.xlim = (-3.0,3.0)
for i in range(nt):
    plt.plot(x, U[i])
    plt.pause(0.1)
"""
line, = plt.plot([],[]) 
def animate(i): 
    line.set_data(x, waveSolve(beta, nx, i+2, c, L, U0)[i])
    return line,
def init():
    line.set_data([],[])
    return line,
anim.FuncAnimation(plt.figure(), animate, init_func=init, frames=100, blit=True, interval=20, repeat=False)
"""
plt.show()