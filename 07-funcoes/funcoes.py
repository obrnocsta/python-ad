# função sem parâmetros e sem retorno
def mostrar_autor():
	print("Desenvolvido por: Bruno Costa")

mostrar_autor()

# função com parâmetro e sem retorno
def mostrar_turma(turma):
	print(f"Turma: {turma}")

mostrar_turma("AD05")

# função com parâmetro e com retorno
def somar(a, b):
	return a + b

n1 = int(input("Número 1: "))
n2 = int(input("Número 2: "))

r = somar(n1, n2)

print(f"A soma de {n1} + {n2} = {r}")
