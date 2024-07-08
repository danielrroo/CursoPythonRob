import numpy as np
a = [[16/13, 16/ 13], [1, -1]]
b = [72000, 8500]
x = np.linalg.solve(a, b)
print("La solución del sistema es: ", x)
import numpy as np
a = [[1, 1, 1], [1, -1, 0], [3, 3, -13]]
b = [72000, 8500, 0]
x = np.linalg.solve(a, b)
print("La solución del sistema es: ", x)
