def somarmultiplosnumeros(numeros):
	resultado = 0
	for numero in numeros:
		resultado += numero
	return resultado

def multiplicarmultiplosnumeros(numeros):
	resultado = 1
	for numero in numeros:
		resultado *= numero
	return resultado

def ehpar(numero):
	return numero % 2 == 0

def ehinteiro(numero):
	return isinstance(numero, int)

print(somarmultiplosnumeros([5, 10, 15])) # 30
print(somarmultiplosnumeros([0.5, -4, 2])) # -1.5
print(multiplicarmultiplosnumeros([2, 5])) # 10
print(multiplicarmultiplosnumeros([-1, 3, 2.5])) # -7.5
print(ehpar(8)) # True
print(ehpar(5)) # False
print(ehpar(2.5)) # False
print(ehinteiro(10)) # True
print(ehinteiro(-6)) # True
print(ehinteiro(4.2)) # False
