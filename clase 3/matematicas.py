def factorial (n):
    acum = 1
    for i in range (1,n+1):
        acum *=i
    return acum
def factorial2(n):
    if n ==0:
        return 1
    return n * factorial2(n-1)

#fibonachi

def fibo2(n):
    if n in (1,2):
        return 1
    return fibo2(n-1)+fibo2(n-2)

#contar sublistas

def contar_sub(lista):
    if lista == []:
        return 0
    return len(lista[0]) + contar_sub(lista[1:])

def suma_lista(lista):
    if lista ==[]:
        return 0
    return lista [0] + suma_lista(lista[1:])

def suma_sublistas(lista):
    if lista == []:
        return 0
    return suma_lista(lista[0])+ suma_sublistas(lista[1:])

# el usuario ingresa un numero, del cual se crea una lista del tamaño de ese numero con numeros aleatorios, luego debe adivinar uno de esos numeros 

import random 
print ("ingrese un numero")
n = input() 
def juego (n):
    lista = []
    for x in range(n):
       lista.append(random.randint(2,100))
    return lista

print juego (n)
print ("adivina el numero")
y = input()
def adivinanza (y):
    if y in juego(n):
        print ("ganaste")
        break
    else:
        print ("intenta de nuevo")
              

    
    
