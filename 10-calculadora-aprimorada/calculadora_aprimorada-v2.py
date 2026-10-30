import math

def somarmultiplosnumeros(numeros):
	return math.fsum(numeros)

def multiplicarmultiplosnumeros(numeros):
	return math.prod(numeros)

def ehpar(numero):
	return numero % 2 == 0

def ehinteiro(numero):
	return isinstance(numero, int)

print(somarmultiplosnumeros([5, 10, 15]))
print(somarmultiplosnumeros([0.5, -4, 2]))
print(multiplicarmultiplosnumeros([2, 5]))
print(multiplicarmultiplosnumeros([-1, 3, 2.5]))
print(ehpar(8))
print(ehpar(5))
print(ehpar(2.5))
print(ehinteiro(10))
print(ehinteiro(-6))
print(ehinteiro(4.2))
