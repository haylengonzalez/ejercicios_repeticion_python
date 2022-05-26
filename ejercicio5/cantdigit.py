"""Ejercicio N°5
Programa para calcular la cantidad de digitos de un número"""

print("------------------------------------")
print("--------Cantidad Digitos------------")
print("------------------------------------")

# input

A=int(input("digite el valor de A: "))

# processing

Z=int(len(str(A)))

# output

print(str(A) + " tiene " + str(Z) + " digitos.")
