import numpy as np
from scipy.linalg import solve
"""
2x+3y+4z=3
2x+6y+8z=5
4x+9y-4z=4
"""

a=np.array([[2,3,4], [2,6,8], [4,9,-4]])
b=np.array([3,5,4])
x=solve(a,b)
print("La solución del sistema es: ", x)

