import numpy as np
# Crear una matriz 1D NumPy
array_1d = np.array([1, 2, 3, 4, 5])

print("1D Array:")
print(array_1d)

# Crear matriz 2D
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

print("\n2D Array:")
print(array_2d)


#Ejercico 2
print("corte")

print(array_1d[1:4])
print(array_1d[2:6])

#Ejercicio 3
array_3d = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(array_3d[(array_3d > 4) & (array_3d < 6)])

#Ejercicio 4
