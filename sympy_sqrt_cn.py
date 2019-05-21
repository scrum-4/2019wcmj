from sympy import *
import math

z = -(1/3)-(math.pi/7)*I
x, y = symbols('x y', real=True)
result = solve((x+I*y)**2 - z, (x, y))
print(result)