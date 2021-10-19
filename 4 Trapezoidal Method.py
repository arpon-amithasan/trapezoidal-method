import numpy as np
import math
import matplotlib as mpl
import matplotlib.pyplot as plt


def f(t, y, eqn):          # Equation Inputs (Has to be configured within the code below)

    # 1) t = independent variable
    # 2) y = dependent variable
    # 3) eqn is only for selecting which equation to execute
    # 4) add/remove equations as necessary
    # 5) adjust value of m in the main() function accordingly

    if eqn == 0:
        # x0 = right hand side of equation 0
        yp0 = t * y
        return yp0
    else:
        return 0   # idiot-proofing


def main():     # Main driver function
    m: int = 1  # number of variables or equations
    print("Solver is currently configured for", m, "equations which are predefined in the code.")

    print("Specify start point")    # time duration
    a = float(input())
    print("Specify end point")
    b = float(input())

    print("Step size")
    h = float(input())  # step size

    t = np.arange(start=a, stop=b, step=h, dtype=float)  # time array
    n = len(t)

    y_app = np.ones([m, n])  # array for approximations

    print("Input initial conditions")   # initial conditions
    for i in range(0, m):
        print("y (", i, ", 0 ) = ?")
        y_app[i, 0] = float(input())

    print("How many guesses per node?")
    g = int(input())
    x = np.zeros([m, g])  # Make array for guessing

    for i in range(1, n):  # loop time nodes

        for j in range(0, m):    # loop equations
            x[j, 0] = y_app[j, i - 1] + h * f(t[i-1], y_app[j, i-1], j)   # using y[j, i-1], we calculate x[j, 0] = 0th guess of y[j,i]

        for p in range(1, g):    # loop guesses
            for q in range(0,m):    # loop equations
                x[q, p] = y_app[q, i-1] + 0.5 * h * (f(t[i-1], y_app[q, i-1], q) + f(t[i], x[q, p-1], q))   # Trapezoidal method

        for k in range(0, m):
            y_app[k, i] = x[k, g-1]     # taking last guess as approximate value

    plt.plot(t, y_app[0, :], label = "Equation 0")  # plotting y
    plt.title("Coupled ODE system")
    plt.xlabel("independent variable")
    plt.ylabel("dependent variable")
    plt.legend()    # showing legend
    plt.show()      # showing plot


main()
