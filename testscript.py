import math

def seno(num):
	res= math.sin(num)
	return res

def coseno(num):
    res = math.cos(num)
    return res


num = int(input("Ingrese un numero: "))
base = int(input("Ingrese el valor de la base: "))

print("La base mide %s" %base)
print(coseno(num))

