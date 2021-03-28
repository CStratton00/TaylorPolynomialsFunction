"""
Collin Stratton
CST-305
Topic 6 Project 6: Numeric Computations with Taylor Polynomials
Dr. Ricardo Citro

For this project, this program is modeling the solutions from Part 1, a and b and the solution
to Part 2. The models are displayed used matplotlib to visualize the data graphically.

Implementation approach:
- Solve the math problems by hand (see documentation)
- Create functions to model the solution
- Define arrays to store values over a space
- Create a for loop to input all the values into arrays
- Graph the data
"""

# Packages used: time, numpy, matplotlib, scipy
import numpy as np                  # import numpy for array space
import matplotlib.pyplot as plt     # import matplotlib for graphing functions
from scipy.special import factorial as fact
from scipy.integrate import odeint  # import scipy to use the ordinary differencial equation integral function

# Part 1a
def p1a(x):                                     # function for the solution for Part 1a
    y0 = 1                                      # value for y0 given and inputed into taylor series
    y1 = x                                      # value for y1 given and inputed into taylor series
    y2 = -1 / 2 * pow(x, 2)                     # value for y2 solved and inputed into taylor series
    y3 = 1 / 3 * pow(x, 3)                      # value for y3 solved and inputed into taylor series
    y4 = -1 / 8 * pow(x, 4)                     # value for y4 solved and inputed into taylor series
    y5 = 14 / fact(5) * pow(x, 5)               # value for y5 solved and inputed into taylor series
    y6 = -2 / fact(6) * pow(x, 6)               # value for y6 solved and inputed into taylor series
    return  y0 + y1 + y2 + y3 + y4 + y5 + y6    # return the summation of the y values to solve

# Part 1b
def p1b(x):                                     # function for the solution for Part 1a
    y0 = 0                                      # value for y0 given and inputed into taylor series
    y1 = -1 / fact(1) * x                       # value for y1 given and inputed into taylor series
    y2 = 1 / fact(2) * pow(x, 2)                # value for y2 solved and inputed into taylor series
    y3 = -1 / fact(3) * pow(x, 3)               # value for y3 solved and inputed into taylor series
    y4 = 2 / fact(4) * pow(x, 4)                # value for y4 solved and inputed into taylor series
    y5 = -5 / fact(5) * pow(x, 5)               # value for y5 solved and inputed into taylor series
    y6 = 16 / fact(6) * pow(x, 6)               # value for y6 solved and inputed into taylor series
    return  y0 + y1 + y2 + y3 + y4 + y5 + y6    # return the summation of the y values to solve

# Part 2
def p2(x, a0, a1):  # function for the solution of Part 2
    # function was split in 2 to make the equation more compact
    # split was based on what is multiplied by a0 and a1
    i = a0 * (1 - (1 / 2) * pow(x, 2) + (1 / 6) * pow(x, 3) + (1 / 12) * pow(x, 4) - \
        (1 / 20) * pow(x, 5) - (1 / 180) * pow(x, 6) - (1 / 3360) * pow(x, 8))
    j = a1 * (x - (1 / 2) * pow(x, 2) - (1 / 6) * pow(x, 3) + (1 / 6) * pow(x, 4) - \
        (1 / 36) * pow(x, 6) + (1 / 252) * pow(x, 7) + (1 / 336) * pow(x, 8))
    return i + j    # return the solution of the two haves

dt = 0.02                               # step size
num_steps = 10000                       # total number of steps

xs = np.linspace(-100, 100, num_steps)  # create of the x space between -100 and 100
ys1a = np.empty(num_steps)              # create and empty space for the values of Part 1a
ys1b = np.empty(num_steps)              # create and empty space for the values of Part 1b
ys2 = np.empty(num_steps)               # create and empty space for the values of Part 2

for i in range(-5000, 5000):            # for loop to enter values into arrays
    ys1a[i] = p1a(i * dt)               # input values for part 1a
    ys1b[i] = p1b(i * dt)               # input values for part 1b
    ys2[i] = p2(i * dt, 2, 2)           # input values for part 2 with given inputs for a0 and a1


plt.title("Taylor Series Part 1a")  # set the title of the graph
plt.xlabel("x")                     # set the x label on the graph
plt.ylabel("y")                     # set the y label on the graph
plt.plot(xs, ys1a)                  # plot the graph
plt.show()                          # displays the graph

plt.title("Taylor Series Part 1b")  # set the title of the graph
plt.xlabel("x")                     # set the x label on the graph
plt.ylabel("y")                     # set the y label on the graph
plt.plot(xs, ys1b)                  # plot the graph
plt.show()                          # displays the graph

plt.title("Taylor Series Part 2")   # set the title of the graph
plt.xlabel("x")                     # set the x label on the graph
plt.ylabel("y")                     # set the y label on the graph
plt.plot(xs, ys2)                   # plot the graph
plt.show()                          # displays the graph
