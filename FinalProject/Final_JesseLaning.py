import numpy as np
import scipy as sp
import scipy.integrate as spint
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time


gridm = np.zeros((5, 5, 2))
# Froude number
Fr = 1.0
Fr2 = Fr**2
# fluid mass density
rho = np.ones(gridm.shape)

dt = 1/1000
n_steps = 1000

for i in range(gridm.shape[0]):
    for j in range(gridm.shape[1]):
        gridm[i][j][0] = 1


def trace(x, y, grid):
    if x == 0:
        x = x + 1
    if x == grid.shape[0] - 1:
        x = x - 1
    if y == 0:
        y = y + 1
    if y == grid.shape[1] - 1:
        y = y - 1
    dx2 = ((grid[x-1][y][0] - grid[x+1][y][0]) / 2)**2
    dy2 = ((grid[x][y-1][1] - grid[x][y+1][1]) / 2)**2

    dxdy = ((grid[x][y-1][0] - grid[x][y+1][0]) / 2)
    dydx = ((grid[x-1][y][1] - grid[x+1][y][1]) / 2)

    return dx2 + dy2 + 2 * dxdy * dydx


def integral_ij(i, j, tmat, grid):
    sum = [0, 0]
    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            if not (x == i and y == j):
                difx = i - x
                dify = j - y
                mag2 = difx**2 + dify**2
                t = tmat[x][y] / mag2
                sum[0] = sum[0] + t[0] * difx
                sum[1] = sum[1] + t[1] * dify
    return sum


def div_check(tmat, grid):
    for i in range(grid.shape[0]):
        tmat[i][0] = tmat[i][1]
        tmat[i][grid.shape[1] - 1] = tmat[i][grid.shape[1] - 2]
    for j in range(grid.shape[1]):
        tmat[0][j] = tmat[1][j]
        tmat[grid.shape[0] - 1][j] = tmat[grid.shape[0] - 2][j]
    return tmat


def f_extij(i, j):
    return [0, -4.9]


def f_ext(grid) -> np.ndarray:
    f = np.zeros(grid.shape)
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            feij = f_extij(i, j)
            f[i][j][0] = feij[0]
            f[i][j][1] = feij[1]
    return f


def grad_p(grid) -> np.ndarray:
    tmat = np.zeros(grid.shape)
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            tmat[i][j] = trace(i, j, grid)

    tmat = div_check(tmat, grid)

    integral = np.zeros(grid.shape)

    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            iij = integral_ij(i, j, tmat, grid)
            integral[i][j][0] = iij[0]
            integral[i][j][1] = iij[1]
            # integral[i][j][0] = 100
            # integral[i][j][0] = 100

    return -integral / (2 * np.pi)


def u_dot_grad_uij(i, j, grid):
    if i == 0:
        i = i + 1
    if i == grid.shape[0] - 1:
        i = i - 1
    if j == 0:
        j = j + 1
    if j == grid.shape[1] - 1:
        j = j - 1
    duxdx = (grid[i-1][j][0] - grid[i+1][j][0]) / 2
    duxdy = (grid[i][j-1][0] - grid[i][j+1][0]) / 2
    udgux = grid[i][j][0] * duxdx + grid[i][j][1] * duxdy

    duydx = (grid[i-1][j][1] - grid[i+1][j][1]) / 2
    duydy = (grid[i][j-1][1] - grid[i][j+1][1]) / 2
    udguy = grid[i][j][0] * duydx + grid[i][j][1] * duydy

    return [udgux, udguy]


def u_dot_grad_u(grid) -> np.ndarray:
    udgu = np.zeros(grid.shape)
    for i in range(grid.shape[0]):
        for j in range(grid.shape[1]):
            t = u_dot_grad_uij(i, j, grid)
            udgu[i][j][0] = t[0]
            udgu[i][j][1] = t[1]
    print(np.sum(udgu[:][1:]))
    return udgu


def dudt(grid):
    udgu = u_dot_grad_u(grid)
    gp = grad_p(grid)
    f = f_ext(grid) / Fr2

    # print(udgu[3][3], gp[3][3], f[0][0])

    return udgu + gp + f


def apply_boundary(grid):
    for i in range(grid.shape[0]):
        grid[i][0][0] = grid[i][1][0]
        if(grid[i][1][1] < 0):
            grid[i][0][1] = -grid[i][1][1]
        else:
            grid[i][0][1] = 0

        # grid[i][grid.shape[1] - 1][0] = grid[i][grid.shape[1] - 2][0]
        # if(grid[i][grid.shape[1] - 2][1] > 0):
        #     grid[i][grid.shape[1] - 1][1] = -grid[i][grid.shape[1] - 2][1]
        # else:
        #     grid[i][grid.shape[1] - 1][1] = 0

        # grid[2][2] = 0
        # if(grid[1][2][0] > 0):
        #     grid[2][2][0] -= grid[1][2][0]
        # if(grid[2][1][1] < 0):
        #     grid[2][2][1] -= grid[2][1][1]
    return grid


t = np.zeros(np.hstack((n_steps, gridm.shape)))

t[0] = gridm
for i in range(1, n_steps):
    #t[i - 1] = apply_boundary(t[i - 1])
    t[i] = t[i - 1] + dudt(t[i - 1])*dt

#
#
#
# plot
#
#
#

x = np.arange(0, gridm.shape[0], 1)
y = np.arange(0, gridm.shape[1], 1)

X, Y = np.meshgrid(x, y)
X = np.hstack(X)
Y = np.hstack(Y)
pts = [np.hstack(np.transpose(t[0])[0]),
       np.hstack(np.transpose(t[0])[1])]
fig, sp = plt.subplots(1, 1)
sp.set_xlim(-1, gridm.shape[0])
sp.set_ylim(-1, gridm.shape[1])
Q = sp.quiver(X, Y, pts[0], pts[1])


def update_plot(num, Q, t):
    num = num % n_steps
    pts[0] = np.hstack(np.transpose(t[num])[0])
    pts[1] = np.hstack(np.transpose(t[num])[1])
    Q.set_UVC(pts[0], pts[1])


anim = animation.FuncAnimation(
    fig, update_plot, fargs=(Q, t), interval=50, blit=False)

fig.tight_layout()
plt.show()
