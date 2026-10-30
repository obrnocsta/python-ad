#inicio = int(input("inicio: "))
#fim = int(input("fim: "))

#for numero in range(inicio, fim + 1):
for numero in range(1, 1001):
	if numero % 3== 0 and numero % 5 == 0:
		print("FizzBuzz")
	elif numero % 3 == 0:
		print("Fizz")
	elif numero % 5 == 0:
		print("Buzz")
	else:
		print(numero)
