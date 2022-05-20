"""Ejercicio N°2
Programa para calcular la cantidad de número que hay en un rango numerico""" 

print("------------------------------")
print("--------Rango Numerico--------")
print("------------------------------")

# input

A=int(input("digite el valor inicial del rango: "))
B=int(input("digite el valor final del rango: "))
cant_num=0
rango=A+1

# processing

if A>B:
    print("El valor inicial no puede ser mayor al valor final. ")
else:
    while rango<B:
        cant_num=cant_num+1
        rango=rango+1
    print("Entre " + str(A) + " y " + str (B) + " hay " + str(cant_num) + " números.")