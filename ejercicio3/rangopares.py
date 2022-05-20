"""Ejercicio N°3
Programa para calcular la cantidad de números pares en un rango numerico"""

print("-----------------------------------------")
print("---------Cantidad Números Pares----------")
print("-----------------------------------------")

# input

A=int(input("digite el valor inicial del rango: "))
B=int(input("digite el valor final del rango: "))

# processing

if A<B:
    cant_pares=0
    rango=A
    while rango<B:
        rango=rango+1
        p=rango%2
        if p==0:
            cant_pares=cant_pares+1
    print("La cantidad de números pares en ese rango es de " + str(cant_pares))
else:
    print("El valor inicial no puede ser mayor al valor final.")