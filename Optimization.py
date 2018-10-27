# -*- coding: utf-8 -*-
"""

Optimizing routines for non-linear programming problems (Karush-Kuhn-Tucker).


"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
from math import sqrt, sin

## Final Exam GRA6035

# max f(x,y) =x^2y^2 s.t. x^2 + y^2 + x^2y^2 >= 3
def objective(x):
   return x[0]**2*x[1]**2

def constraint(x):
    return x[0]**2 + x[1]**2 + x[0]**2*x[1]**2-3.0

# Unitial guesses. Since the function contains squared terms, change signs and
# redo optimization to catch potentially multiple solutions
x0 = np.zeros(2)
x0[0] = 0.5
x0[1] = 0.5


# Run optimization routine
b = (-sqrt(3),sqrt(3))
bnds = (b, b)
con = {'type': 'ineq', 'fun': constraint} 
solution = minimize(objective,x0,method='SLSQP',\
                    bounds=bnds,constraints=con,options={'disp': True})
x = solution.x

print('Solution::')
print('x = ' + str(x[0]))
print('y = ' + str(x[1]))


## Final Exam GRA6035

# min f(x,y) = x^2 + y^2 s.t. xy >= 4

def objective(x):
   return -1*(x[0]**2 + x[1]**2)

def constraint(x):
    return -1*x[0]*x[1]+4.0

# Unitial guesses. Since the function contains squared terms, change signs and
# redo optimization to catch potentially multiple solutions
x0 = np.zeros(2)
x0[0] = 0.5
x0[1] = 0.5

# Run optimization routine
b = (-4,4)
bnds = (b, b)
con = {'type': 'ineq', 'fun': constraint} 
solution = minimize(objective,x0,method='SLSQP',\
                    bounds=bnds,constraints=con,options={'disp': True})
x = solution.x


print('Solution::')
print('x = ' + str(x[0]))
print('y = ' + str(x[1]))


