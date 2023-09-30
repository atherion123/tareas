from math import sqrt
import random

def primo(n):
    if (n==1):
        return False
    elif (n==2):
        return True;
    else:
        for x in range(2,n):
            if(n % x==0):
                return False
        return True

def nextprime(n):
    while True:
        n=n+1
        for i in range (2,int(n/2)):
            if n%i==0:
                break
        else:
            return n

def mediana(x, y, z):
    numeros = [x, y, z]

    numeros.sort()

    mediana = numeros[1]

    return mediana

def contraseña():
    longitud = random.randint(7, 10)
    resultado = ""

    for i in range(longitud):
        resultado = resultado + chr(random.randint(33, 126))

    return resultado

def hipotenusa(lado1,lado2):
  c = sqrt(lado1 ** 2 + lado2 ** 2)

  return c