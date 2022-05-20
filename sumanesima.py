"""Ejercicio1 N°1
Programa para los primeros n primeros números naturles """

print("-----------------------------------------")
print("--------Suma Primeros Enesimos-----------")
print("-----------------------------------------")

#input

n=int(input("digite el valor de n: "))
resultado=0
cant_num=0
#prossecing


while cant_num<n:
    cant_num+=1
    resultado=resultado+cant_num


#output
print(" La suma de los primeros " + str(n) + " números naturles es igual a " + str(resultado))