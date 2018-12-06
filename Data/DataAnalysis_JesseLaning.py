import scipy.integrate
import scipy.interpolate
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches


def hessian(x, i, j, da, de):
    dade = (x[i - 1][j - 1] + x[i + 1][j + 1] -
            x[i - 1][j + 1] - x[i + 1][j - 1]) / (4 * da * de)

    daa = (x[i + 1][j] + x[i - 1][j] - 2 * x[i][j]) / (da*da)
    dee = (x[i][j + 1] + x[i][j - 1] - 2 * x[i][j]) / (de*de)

    H = np.empty((2, 2))
    H[0][0] = daa
    H[0][1] = dade
    H[1][0] = dade
    H[1][1] = dee

    return -H


def calc(z, D, err, func):
    # A
    WM = np.linspace(0.75, -.25, 100)
    # E0
    WL = np.linspace(6.5, 7.5, 100)

    minX = np.Inf
    minwm = 0
    minwl = 0

    mini = 0
    minj = 0

    Xs = np.zeros((len(WM), len(WL)))
    Ds = np.zeros(len(z))
    minDs = np.zeros(len(z))

    for im in range(len(WM)):
        wm = WM[im]
        for jl in range(len(WL)):
            wl = WL[jl]
            for i in range(len(z)):
                Ds[i] = func(wm, wl, z[i])
            tx = np.sum((D-Ds)**2/err**2)
            Xs[im][jl] = tx
            if tx < minX:
                mini = im
                minj = jl
                minX = tx
                minwm = wm
                minwl = wl
                minDs = np.copy(Ds)

    # -X^2/2
    log_likleyhood = -Xs/2

    H = hessian(log_likleyhood, mini, minj, WM[1] - WM[0], WL[1] - WL[0])
    C = np.linalg.inv(H)

    return WM, WL, minwm, minwl, Xs, minX, minDs, C


def doplot(z, D, err, func, WM, WL, minwm, minwl, Xs, minX, minDs, C):
    plt.figure()

    e = np.sqrt(C.diagonal())
    ea = e[0]
    ee = e[1]

    t = r'Min $X^2$ = ' + str(round(minX, 4)) + ' | A = ' + \
        str(round(minwm, 4)) + r' | $E_0$ = ' + str(round(minwl, 4))
    plt.title(t)

    ax = plt.subplot2grid((1, 2), (0, 0), xlabel='A',
                          ylabel=r'$E_0$', title=r'A vs $E_0$')
    ax.set_xlim(np.min(WM), np.max(WM))
    ax.set_ylim(np.min(WL), np.max(WL))
    X, Y = np.meshgrid(WM, WL)
    ax.contour(X, Y, Xs, colors='k')
    im = ax.pcolormesh(X, Y, Xs)
    # plt.colorbar(im, ax=ax)
    ax.scatter([minwm], [minwl], marker='.', c='r', label=r'Min $X^2$')
    ax.annotate(r'A = ' + str(round(minwm, 3)) + r'$\pm$' + str(round(ea, 3)) +
                r', $E_0$ = ' + str(round(minwl, 3)) + r'$\pm$' + str(round(ee, 3)), xy=(minwm, minwl), xytext=(-100, 5), textcoords='offset points', color='w')

    Dx = np.zeros(200)
    X = np.linspace(np.min(z), np.max(z), Dx.shape[0])

    for i in range(Dx.shape[0]):
        Dx[i] = func(minwm, minwl, X[i])

    ay = plt.subplot2grid((1, 2), (0, 1), title=r'E vs $N_i$ | A=' + str(round(minwm, 3)) +
                          r' | $E_0$=' + str(round(minwl, 3)) + r' | $X^2$=' + str(round(minX, 3)) +
                          ' | Cross-Correlation = ' + str(round(C[0][1], 3)),
                          xlabel='E', ylabel=r'$N_i$')
    ay.plot(X, Dx, '--', label='Simulated')
    ay.errorbar(z, D, err, fmt='.', label='Input')
    ay.errorbar(z, minDs, xerr=ee, yerr=ea, fmt='.', label='Calculated')
    handles = ay.get_legend_handles_labels()[0]
    handles.append(mpatches.Patch(
        color='none', label=r'$\sigma_A$=' + str(round(ea, 3))))
    handles.append(mpatches.Patch(
        color='none', label=r'$\sigma_E$=' + str(round(ee, 3))))
    ay.legend(handles=handles)
    plt.show()

def model_selection():
    random_data = np.zeros((100, 100))

data1 = np.loadtxt("hw9/DataAnalysis.txt")
data1 = data1[np.argsort(data1[:, 0])]
data = np.transpose(data1)
z = data[0]
D = data[1]
err = data[2]


def func(A, E0, z):
    return 1 + A * np.exp(-(E0-z)**2)


v = calc(z, D, err, func)
WM, WL, minwm, minwl, Xs, minX, minDs, C = v

doplot(z, D, err, func, *v)
