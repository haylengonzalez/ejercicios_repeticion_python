"""Ejercicio N°4
Programa que obtiene la cantidad de los primeros N números múltiplos de 5."""

print("------------------------------------------------")
print("---------- CANTIDAD DE MÚLTIPLOS DE 5 ----------")
print("------------------------------------------------")

# input

A=int(input("digite el valor inicial del rango: "))
B=int(input("digite el valor final del rango: "))

# processing

if A<B:
    rango=0
    cant_m5=0
    while rango<B:
        rango=rango+1
        m=rango%5
        if m==0:
            cant_m5=cant_m5+1
    print("Entre " + str(A) + " y " + str(B) + " hay " + str(cant_m5) + " multiplos de 5")
else:
    print("El valor inicial no puede ser mayor al valor final")